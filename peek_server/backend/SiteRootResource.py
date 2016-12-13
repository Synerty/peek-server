import os

from peek_server.PeekServerConfig import peekServerConfig
from peek_server.server.sw_upload.PeekSwUploadResource import PeekSwUploadResource
from txhttputil.site.FileUnderlayResource import FileUnderlayResource
from vortex.VortexResource import VortexResource

root = FileUnderlayResource()

# Setup properties for serving the site
root.enableSinglePageApplication()

# This dist dir is automatically generated, but check it's parent
buildDir = peekServerConfig.feDistDir
buildDirParent = os.path.dirname(buildDir)
if not os.path.isdir(buildDirParent):
    raise NotADirectoryError(buildDirParent)

# Make the dist dir, otherwise addFileSystemRoot throws an exception.
# It rebuilds at a later date
os.makedirs(buildDir, exist_ok=True)

root.addFileSystemRoot(buildDir)

# Add the vortex
root.putChild(b'vortex', VortexResource())

# Add the
root.putChild(b'peek_server.update.platform',
              PeekSwUploadResource(PeekSwUploadResource.UPDATE_TYPE_PLATFORM))

root.putChild(b'peek_server.update.papp',
              PeekSwUploadResource(PeekSwUploadResource.UPDATE_TYPE_PAPP))