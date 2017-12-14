# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This package facilitates retries for HTTP/REST requests to the registry."""



import httplib
import time

import httplib2

DEFAULT_SOURCE_TRANSPORT_CALLABLE = httplib2.Http
DEFAULT_MAX_RETRIES = 2
DEFAULT_BACKOFF_FACTOR = 0.5
RETRYABLE_EXCEPTION_TYPES = [httplib.IncompleteRead]


def _ShouldRetry(err):
  for exception_type in RETRYABLE_EXCEPTION_TYPES:
    if isinstance(err, exception_type):
      return True

  return False


class Factory(object):
  """A factory for creating RetryTransports."""

  def __init__(self):
    self.kwargs = {}

  def WithSourceTransport(self, source_transport):
    self.kwargs['source_transport'] = source_transport
    return self

  def WithMaxRetries(self, max_retries):
    self.kwargs['max_retries'] = max_retries
    return self

  def WithBackoffFactor(self, backoff_factor):
    self.kwargs['backoff_factor'] = backoff_factor
    return self

  def WithShouldRetryFunction(self, should_retry_fn):
    self.kwargs['should_retry_fn'] = should_retry_fn
    return self

  def Build(self):
    """Returns a RetryTransport constructed with the given values.
    """
    return RetryTransport(**self.kwargs)


class RetryTransport(httplib2.Http):
  """A wrapper for the given transport which automatically retries errors.
  """

  def __init__(self,
               source_transport = None,
               max_retries = DEFAULT_MAX_RETRIES,
               backoff_factor = DEFAULT_BACKOFF_FACTOR,
               should_retry_fn = _ShouldRetry):
    self._transport = source_transport or DEFAULT_SOURCE_TRANSPORT_CALLABLE()
    self._max_retries = max_retries
    self._backoff_factor = backoff_factor
    self._should_retry = should_retry_fn

  def request(self, *args, **kwargs):
    """Does the request, exponentially backing off and retrying as appropriate.

    Backoff is backoff_factor * (2 ^ (retry #)) seconds.
    Args:
      *args: The sequence of positional arguments to forward to the
        source transport.
      **kwargs: The keyword arguments to forward to the source transport.

    Returns:
      The response of the HTTP request, and its contents.
    """
    retries = 0
    while True:
      try:
        return self._transport.request(*args, **kwargs)
      except Exception as err:  # pylint: disable=broad-except
        if retries >= self._max_retries or not self._should_retry(err):
          raise

        retries += 1
        time.sleep(self._backoff_factor * (2**retries))
        continue
