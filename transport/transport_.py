import httplib2
import logging

DEFAULT_SOURCE_TRANSPORT_CALLABLE = httplib2.Http

class Factory(object):
  """A factory for creating httplib2.Http client instance."""

  def __init__(self, http_callable_transport = DEFAULT_SOURCE_TRANSPORT_CALLABLE):
    self.http_callable_transport = http_callable_transport

  def WithCaCert(self, ca_cert):
    def _apply_ca_cert(callable, ca_cert):
      def _with_ca_cert(*args, **kwargs):
          kwargs['ca_certs'] = ca_cert
          return callable(*args, **kwargs)
      return _with_ca_cert

    if ca_cert is not None:
      logging.info('Adding CA certificates of %s', ca_cert)
      self.http_callable_transport = _apply_ca_cert(self.http_callable_transport, ca_cert)
    return self

  def Build(self):
    """Returns a httplib2.Http client constructed with the given values.
    """
    return self.http_callable_transport()