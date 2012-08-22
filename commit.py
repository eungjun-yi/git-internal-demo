#!/bin/env python
import os, sys, sha, zlib, time

treeid = sys.argv[1]

branch = open('HEAD').read()[5:].strip()
if os.path.exists(branch):
    parentid = open(branch).read().strip()
else:
    parentid = None

unixtime = str(int(time.time()))
content = 'tree %s\n' % treeid
if parentid:
    content += 'parent %s\n' % parentid
content += """author Yi EungJun <semtlenori@gmail.com> %s +0900
committer Yi EungJun <semtlenori@gmail.com> %s + 0900

test commit""" % (unixtime, unixtime)

type = 'commit'

object = '%s %d\0%s' % (type, len(content), content)
sha1sum = sha.new(object).hexdigest()
container = 'objects/%s' % sha1sum[:2]
if not os.path.exists(container):
    os.mkdir(container)

open('%s/%s' % (container, sha1sum[2:]), 'w').write(zlib.compress(object))
if not os.path.exists('refs/heads'):
    os.mkdir('refs/heads')
open(open('HEAD').read()[5:].strip(), 'w').write(sha1sum)

print sha1sum
