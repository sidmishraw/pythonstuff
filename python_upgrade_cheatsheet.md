### Upgrading python3 through homebrew
> `brew upgrade python3`


### How brew broke the symlinks for python3 after upgrade?
```
sidmishraw@Sidharths-MBP ~> brew info python3
python3: stable 3.6.1 (bottled), HEAD
Interpreted, interactive, object-oriented programming language
https://www.python.org/
/usr/local/Cellar/python3/3.6.0 (3,705 files, 57MB) *
  Poured from bottle on 2017-02-04 at 19:32:53
From: https://github.com/Homebrew/homebrew-core/blob/master/Formula/python3.rb
==> Dependencies
Build: pkg-config ✔, sphinx-doc ✘
Required: openssl ✔
Recommended: readline ✔, sqlite ✘, gdbm ✘, xz ✔
Optional: homebrew/dupes/tcl-tk ✘, sphinx-doc ✘
==> Options
--with-quicktest
	Run `make quicktest` after the build
--with-sphinx-doc
	Build HTML documentation
--with-tcl-tk
	Use Homebrew's Tk instead of macOS Tk (has optional Cocoa and threads support)
--without-gdbm
	Build without gdbm support
--without-readline
	Build without readline support
--without-sqlite
	Build without sqlite support
--without-xz
	Build without xz support
--HEAD
	Install HEAD version
==> Caveats
Pip, setuptools, and wheel have been installed. To update them
  pip3 install --upgrade pip setuptools wheel

You can install Python packages with
  pip3 install <package>

They will install into the site-package directory
  /usr/local/lib/python3.6/site-packages

See: http://docs.brew.sh/Homebrew-and-Python.html
sidmishraw@Sidharths-MBP ~> python3 --version
Python 3.6.0
sidmishraw@Sidharths-MBP ~> brew upgrade python3
==> Upgrading 1 outdated package, with result:
python3 3.6.1
==> Upgrading python3 
==> Installing dependencies for python3: sqlite, gdbm
==> Installing python3 dependency: sqlite
==> Downloading https://homebrew.bintray.com/bottles/sqlite-3.17.0.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring sqlite-3.17.0.sierra.bottle.tar.gz
==> Caveats
Homebrew has detected an existing SQLite history file that was created
with the editline library. The current version of this formula is
built with Readline. To back up and convert your history file so that
it can be used with Readline, run:

  sed -i~ 's/\\040/ /g' ~/.sqlite_history

before using the `sqlite` command-line tool again. Otherwise, your
history will be lost.

This formula is keg-only, which means it was not symlinked into /usr/local.

macOS provides an older sqlite3.

If you need to have this software first in your PATH run:
  echo 'export PATH="/usr/local/opt/sqlite/bin:$PATH"' >> ~/.bash_profile

For compilers to find this software you may need to set:
    LDFLAGS:  -L/usr/local/opt/sqlite/lib
    CPPFLAGS: -I/usr/local/opt/sqlite/include
For pkg-config to find this software you may need to set:
    PKG_CONFIG_PATH: /usr/local/opt/sqlite/lib/pkgconfig

==> Summary
🍺  /usr/local/Cellar/sqlite/3.17.0: 11 files, 2.9MB
==> Installing python3 dependency: gdbm
==> Downloading https://homebrew.bintray.com/bottles/gdbm-1.13.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring gdbm-1.13.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/gdbm/1.13: 19 files, 554.4KB
==> Installing python3 
==> Downloading https://homebrew.bintray.com/bottles/python3-3.6.1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring python3-3.6.1.sierra.bottle.tar.gz
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /usr/local
Could not symlink share/man/man1/python3.1
Target /usr/local/share/man/man1/python3.1
already exists. You may want to remove it:
  rm '/usr/local/share/man/man1/python3.1'

To force the link and overwrite all conflicting files:
  brew link --overwrite python3

To list all files that would be deleted:
  brew link --overwrite --dry-run python3

Possible conflicting files are:
/usr/local/share/man/man1/python3.1 -> /usr/local/share/man/man1/python3.5.1
/usr/local/lib/pkgconfig/python3.pc -> /usr/local/lib/pkgconfig/python-3.5.pc
==> Using the sandbox
==> /usr/local/Cellar/python3/3.6.1/bin/python3 -s setup.py --no-user-cfg install --force --verbose --install-scripts=/usr/local/
==> /usr/local/Cellar/python3/3.6.1/bin/python3 -s setup.py --no-user-cfg install --force --verbose --install-scripts=/usr/local/
==> /usr/local/Cellar/python3/3.6.1/bin/python3 -s setup.py --no-user-cfg install --force --verbose --install-scripts=/usr/local/
==> Caveats
Pip, setuptools, and wheel have been installed. To update them
  pip3 install --upgrade pip setuptools wheel

You can install Python packages with
  pip3 install <package>

They will install into the site-package directory
  /usr/local/lib/python3.6/site-packages

See: http://docs.brew.sh/Homebrew-and-Python.html
==> Summary
🍺  /usr/local/Cellar/python3/3.6.1: 3,600 files, 55.8MB
sidmishraw@Sidharths-MBP ~> python3 --version
fish: Unknown command 'python3'
```






### Symlinking manually:

Initial mappings:
```
Sidharths-MBP:python3 sidmishraw$ ls -ali /usr/local/bin/ | grep python*
1059566 lrwxr-xr-x    1 sidmishraw  admin    34 Feb  4 19:30 2to3-2 -> ../Cellar/python/2.7.13/bin/2to3-2
1059567 lrwxr-xr-x    1 sidmishraw  admin    36 Feb  4 19:30 2to3-2.7 -> ../Cellar/python/2.7.13/bin/2to3-2.7
1060997 lrwxr-xr-x    1 sidmishraw  admin    40 Feb  4 19:30 easy_install -> ../Cellar/python/2.7.13/bin/easy_install
1060998 lrwxr-xr-x    1 sidmishraw  admin    44 Feb  4 19:30 easy_install-2.7 -> ../Cellar/python/2.7.13/bin/easy_install-2.7
2863229 lrwxr-xr-x    1 sidmishraw  admin    44 Mar 25 12:39 easy_install-3.6 -> ../Cellar/python3/3.6.1/bin/easy_install-3.6
1059568 lrwxr-xr-x    1 sidmishraw  admin    32 Feb  4 19:30 idle -> ../Cellar/python/2.7.13/bin/idle
1059569 lrwxr-xr-x    1 sidmishraw  admin    33 Feb  4 19:30 idle2 -> ../Cellar/python/2.7.13/bin/idle2
1059570 lrwxr-xr-x    1 sidmishraw  admin    35 Feb  4 19:30 idle2.7 -> ../Cellar/python/2.7.13/bin/idle2.7
1060994 lrwxr-xr-x    1 sidmishraw  admin    31 Feb  4 19:30 pip -> ../Cellar/python/2.7.13/bin/pip
1060995 lrwxr-xr-x    1 sidmishraw  admin    32 Feb  4 19:30 pip2 -> ../Cellar/python/2.7.13/bin/pip2
1060996 lrwxr-xr-x    1 sidmishraw  admin    34 Feb  4 19:30 pip2.7 -> ../Cellar/python/2.7.13/bin/pip2.7
2863227 lrwxr-xr-x    1 sidmishraw  admin    32 Mar 25 12:39 pip3 -> ../Cellar/python3/3.6.1/bin/pip3
2863228 lrwxr-xr-x    1 sidmishraw  admin    34 Mar 25 12:39 pip3.6 -> ../Cellar/python3/3.6.1/bin/pip3.6
1059571 lrwxr-xr-x    1 sidmishraw  admin    33 Feb  4 19:30 pydoc -> ../Cellar/python/2.7.13/bin/pydoc
1059572 lrwxr-xr-x    1 sidmishraw  admin    34 Feb  4 19:30 pydoc2 -> ../Cellar/python/2.7.13/bin/pydoc2
1059573 lrwxr-xr-x    1 sidmishraw  admin    36 Feb  4 19:30 pydoc2.7 -> ../Cellar/python/2.7.13/bin/pydoc2.7
1059574 lrwxr-xr-x    1 sidmishraw  admin    34 Feb  4 19:30 python -> ../Cellar/python/2.7.13/bin/python
2857354 lrwxr-xr-x    1 sidmishraw  admin    38 Mar 25 12:37 python-build -> ../Cellar/pyenv/1.0.9/bin/python-build
1059575 lrwxr-xr-x    1 sidmishraw  admin    41 Feb  4 19:30 python-config -> ../Cellar/python/2.7.13/bin/python-config
1059576 lrwxr-xr-x    1 sidmishraw  admin    35 Feb  4 19:30 python2 -> ../Cellar/python/2.7.13/bin/python2
1059577 lrwxr-xr-x    1 sidmishraw  admin    42 Feb  4 19:30 python2-config -> ../Cellar/python/2.7.13/bin/python2-config
1059578 lrwxr-xr-x    1 sidmishraw  admin    37 Feb  4 19:30 python2.7 -> ../Cellar/python/2.7.13/bin/python2.7
1059579 lrwxr-xr-x    1 sidmishraw  admin    44 Feb  4 19:30 python2.7-config -> ../Cellar/python/2.7.13/bin/python2.7-config
1940761 lrwxr-xr-x    1 sidmishraw  admin    53 Feb 23 11:05 python3.5.2 -> /Users/sidmishraw/.pyenv/versions/3.5.2/bin/python3.5
1059580 lrwxr-xr-x    1 sidmishraw  admin    35 Feb  4 19:30 pythonw -> ../Cellar/python/2.7.13/bin/pythonw
1059581 lrwxr-xr-x    1 sidmishraw  admin    36 Feb  4 19:30 pythonw2 -> ../Cellar/python/2.7.13/bin/pythonw2
1059582 lrwxr-xr-x    1 sidmishraw  admin    38 Feb  4 19:30 pythonw2.7 -> ../Cellar/python/2.7.13/bin/pythonw2.7
1059583 lrwxr-xr-x    1 sidmishraw  admin    36 Feb  4 19:30 smtpd.py -> ../Cellar/python/2.7.13/bin/smtpd.py
1059584 lrwxr-xr-x    1 sidmishraw  admin    39 Feb  4 19:30 smtpd2.7.py -> ../Cellar/python/2.7.13/bin/smtpd2.7.py
1059585 lrwxr-xr-x    1 sidmishraw  admin    37 Feb  4 19:30 smtpd2.py -> ../Cellar/python/2.7.13/bin/smtpd2.py
1060999 lrwxr-xr-x    1 sidmishraw  admin    33 Feb  4 19:30 wheel -> ../Cellar/python/2.7.13/bin/wheel
2863230 lrwxr-xr-x    1 sidmishraw  admin    34 Mar 25 12:39 wheel3 -> ../Cellar/python3/3.6.1/bin/wheel3
```

File in `/usr/local/bin` to update the symlinks for:
1. easy_install-3.6
2. idle
3. pip3
4. pydoc3
5. python3
6. pythonw3
7. python3.6-config
8. smtpd3.py (if there)
9. wheel3
10. 2to3-3.6
11. pyvenv


`
Note - If the above files don't exist, then make them. Create symlinks with '<name>x.y.z' [name is the filename and x.y.z are
python version digits. for eg - python3.6.0 for python 3.6.0]
`

### When symlinking using homebrew:

```
Sidharths-MBP:python3 sidmishraw$ brew unlink --verbose python3
Unlinking /usr/local/Cellar/python3/3.6.1... 
rm /usr/local/bin/2to3-3.6
rm /usr/local/bin/easy_install-3.6
rm /usr/local/bin/idle3
rm /usr/local/bin/idle3.6
rm /usr/local/bin/pip3
rm /usr/local/bin/pip3.6
rm /usr/local/bin/pydoc3
rm /usr/local/bin/pydoc3.6
rm /usr/local/bin/python3
rm /usr/local/bin/python3-config
rm /usr/local/bin/python3.6
rm /usr/local/bin/python3.6-config
rm /usr/local/bin/python3.6m
rm /usr/local/bin/python3.6m-config
rm /usr/local/bin/pyvenv
rm /usr/local/bin/pyvenv-3.6
rm /usr/local/bin/wheel3
rm /usr/local/lib/pkgconfig/python-3.6.pc
rm /usr/local/lib/pkgconfig/python-3.6m.pc
rm /usr/local/lib/pkgconfig/python3.pc
rm /usr/local/share/man/man1/python3.1
rm /usr/local/share/man/man1/python3.6.1
rm /usr/local/Frameworks/Python.framework/Versions/3.6
23 symlinks removed
Sidharths-MBP:python3 sidmishraw$ brew link --verbose python3
Linking /usr/local/Cellar/python3/3.6.1... 
ln -s ../Cellar/python3/3.6.1/bin/2to3-3.6 2to3-3.6
ln -s ../Cellar/python3/3.6.1/bin/easy_install-3.6 easy_install-3.6
ln -s ../Cellar/python3/3.6.1/bin/idle3 idle3
ln -s ../Cellar/python3/3.6.1/bin/idle3.6 idle3.6
ln -s ../Cellar/python3/3.6.1/bin/pip3 pip3
ln -s ../Cellar/python3/3.6.1/bin/pip3.6 pip3.6
ln -s ../Cellar/python3/3.6.1/bin/pydoc3 pydoc3
ln -s ../Cellar/python3/3.6.1/bin/pydoc3.6 pydoc3.6
ln -s ../Cellar/python3/3.6.1/bin/python3 python3
ln -s ../Cellar/python3/3.6.1/bin/python3-config python3-config
ln -s ../Cellar/python3/3.6.1/bin/python3.6 python3.6
ln -s ../Cellar/python3/3.6.1/bin/python3.6-config python3.6-config
ln -s ../Cellar/python3/3.6.1/bin/python3.6m python3.6m
ln -s ../Cellar/python3/3.6.1/bin/python3.6m-config python3.6m-config
ln -s ../Cellar/python3/3.6.1/bin/pyvenv pyvenv
ln -s ../Cellar/python3/3.6.1/bin/pyvenv-3.6 pyvenv-3.6
ln -s ../Cellar/python3/3.6.1/bin/wheel3 wheel3
ln -s ../../../Cellar/python3/3.6.1/share/man/man1/python3.1 python3.1
ln -s ../../../Cellar/python3/3.6.1/share/man/man1/python3.6.1 python3.6.1
ln -s ../../Cellar/python3/3.6.1/lib/pkgconfig/python-3.6.pc python-3.6.pc
ln -s ../../Cellar/python3/3.6.1/lib/pkgconfig/python-3.6m.pc python-3.6m.pc
ln -s ../../Cellar/python3/3.6.1/lib/pkgconfig/python3.pc python3.pc
ln -s ../../../Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6 3.6
23 symlinks created
Sidharths-MBP:python3 sidmishraw$ 
```

### Stuff to check for after the upgrade of python:
1. Check if pip has the packages you needed. [virtualenv is the most important one]
