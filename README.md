<table><tr>
<td><a href="https://gcr.io"><img src="https://avatars2.githubusercontent.com/u/1342004?s=200&v=4" height="120"/></a></td>
<td><a href="https://gcr.io"><img src="https://avatars2.githubusercontent.com/u/21046548?s=400&v=4" height="120"/></a></td>
<td><a href="https://bazel.build"><img src="https://bazel.build/images/bazel-icon.svg" height="120"/></a></td>
</tr></table>

# `containerregistry` 

A set of Python libraries and tools for interacting with a Docker Registry.

Bazel users see <a href="https://github.com/bazelbuild/rules_docker">rules_docker</a>, which relies heavily on these tools.

## puller.par

```sh
$ bazel run @containerregistry//:puller.par -- --help
```

```
usage: puller.par [-h] [--name NAME] [--directory DIRECTORY]
                  [--stderrthreshold STDERRTHRESHOLD]

Pull images from a Docker Registry, faaaaast.

optional arguments:
  -h, --help            show this help message and exit
  --name NAME           The name of the docker image to pull and save.
                        Supports fully-qualified tag or digest references.
  --directory DIRECTORY
                        Where to save the image's files.
  --stderrthreshold STDERRTHRESHOLD
                        Write log events at or above this level to stderr.
```

## pusher.par

```sh
$ bazel run @containerregistry//:pusher.par -- --help
```

```
usage: pusher.par [-h] [--name NAME] [--tarball TARBALL] [--config CONFIG]
                  [--digest DIGEST] [--layer LAYER]
                  [--stamp-info-file STAMP_INFO_FILE] [--oci]
                  [--stderrthreshold STDERRTHRESHOLD]

Push images to a Docker Registry, faaaaaast.

optional arguments:
  -h, --help            show this help message and exit
  --name NAME           The name of the docker image to push.
  --tarball TARBALL     An optional legacy base image tarball.
  --config CONFIG       The path to the file storing the image config.
  --digest DIGEST       The list of layer digest filenames in order.
  --layer LAYER         The list of layer filenames in order.
  --stamp-info-file STAMP_INFO_FILE
                        A list of files from which to read substitutions to
                        make in the provided --name, e.g. {BUILD_USER}
  --oci                 Push the image with an OCI Manifest.
  --stderrthreshold STDERRTHRESHOLD
                        Write log events at or above this level to stderr.
```

## importer.par

```
$ bazel run @containerregistry//:importer.par -- --help
```

```
usage: importer.par [-h] [--tarball TARBALL] [--format {tar,tar.gz}]
                    [--directory DIRECTORY]
                    [--stderrthreshold STDERRTHRESHOLD]

Import images from a tarball into our faaaaaast format.

optional arguments:
  -h, --help            show this help message and exit
  --tarball TARBALL     The tarball containing the docker image to rewrite
                        into our fast on-disk format.
  --format {tar,tar.gz}
                        The form in which to save layers.
  --directory DIRECTORY
                        Where to save the image's files.
  --stderrthreshold STDERRTHRESHOLD
                        Write log events at or above this level to stderr.
```

## flatten.par

```sh
$ bazel run @containerregistry//:flatten.par -- --help
```

```
usage: flatten.par [-h] [--tarball TARBALL] [--config CONFIG]
                   [--digest DIGEST] [--layer LAYER]
                   [--uncompressed_layer UNCOMPRESSED_LAYER]
                   [--diff_id DIFF_ID] [--filesystem FILESYSTEM]
                   [--metadata METADATA] [--stderrthreshold STDERRTHRESHOLD]

Flatten container images.

optional arguments:
  -h, --help            show this help message and exit
  --tarball TARBALL     An optional legacy base image tarball.
  --config CONFIG       The path to the file storing the image config.
  --digest DIGEST       The list of layer digest filenames in order.
  --layer LAYER         The list of compressed layer filenames in order.
  --uncompressed_layer UNCOMPRESSED_LAYER
                        The list of uncompressed layer filenames in order.
  --diff_id DIFF_ID     The list of diff_ids in order.
  --filesystem FILESYSTEM
                        The name of where to write the filesystem tarball.
  --metadata METADATA   The name of where to write the container startup
                        metadata.
  --stderrthreshold STDERRTHRESHOLD
                        Write log events at or above this level to stderr.
```

## appender.par

```sh
$ bazel run @containerregistry//:appender.par -- --help
```

```
usage: appender.par [-h] [--src-image SRC_IMAGE] [--tarball TARBALL]
                    [--dst-image DST_IMAGE]
                    [--stderrthreshold STDERRTHRESHOLD]

Append tarballs to an image in a Docker Registry.

optional arguments:
  -h, --help            show this help message and exit
  --src-image SRC_IMAGE
                        The name of the docker image to append to.
  --tarball TARBALL     The tarball to append.
  --dst-image DST_IMAGE
                        The name of the new image.
  --stderrthreshold STDERRTHRESHOLD
                        Write log events at or above this level to stderr.

```
