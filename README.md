Shell tools
===========
Install by:
* Symlink ~/bin to the tools/bin directory
* Source the bin/activate file from a startup script

ipa2asm
-------
Extract assembly from ipa file, requires otool & c++filt.

        $ ipa2asm app.ipa >app.asm

cdup
----
cd by going up until a directory is found

        $ cdup project/*august
