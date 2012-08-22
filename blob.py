#!/bin/env python
import os, sys, sha, zlib

content = sys.stdin.read()
type = 'blob'

object = '%s %d\0%s' % (type, len(content), content)
sha1sum = sha.new(object).hexdigest()
container = 'objects/%s' % sha1sum[:2]
if not os.path.exists(container):
    os.mkdir(container)

open('%s/%s' % (container, sha1sum[2:]), 'w').write(zlib.compress(object))

print sha1sum
