Usage
-----

Make a git repository

    $ mkdir -p .git/objects
    $ mkdir -p .git/refs
    $ mkdir 'ref: refs/heads/master' > .git/HEAD

Move to the repository

    $ cd .git

blob

    $ echo 'Hello, World!' | python blob.py
    8ab686eafeb1f44702738c8b0f24f2567c36da6d

tree

    $ python tree.py greet 8ab686eafeb1f44702738c8b0f24f2567c36da6d
    c97aabb481c72e9e51f7b3afdf93b7a362a17748

commit

    $ python commit.py c97aabb481c72e9e51f7b3afdf93b7a362a17748
    c553507ff28583dd64a106ee1f91924d4fc41ef1

See Also
---------

* ["Git Internal" slide (keynote)](https://github.com/npcode/git-internal)

License
-------

This software is distributed under the [BSD License](http://www.opensource.org/licenses/bsd-license.php).
