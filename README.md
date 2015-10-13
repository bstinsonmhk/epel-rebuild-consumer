# A Fedmsg Consumer for rebuilding packages from EPEL
This is a very simple consumer meant to catch messages from Fedora's Fedmsg bus and pick out EPEL builds. 

The goal is to use this as a trigger to update and rebuild dependencies in the CentOS Community Build System.
