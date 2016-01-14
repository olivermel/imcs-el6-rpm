<<<<<<< HEAD
RPM Spec file for the imcs 

**Description**: In-Memory Columnar Store extension for PostgreSQL

## Dependencies

Currently, only RHEL and CentOS 6.5 have been tested.  Other dependencies are installed
via the boostrap.sh script.

## Installation

### Build the RPM using Vagrant

1. Once the repo has been cloned, run "vagrant up" to create the bulid VM
2. Run "vagrant ssh" to connect
3. CD to ~/rpmbuild
4. Run "rpmbuild -ba SPECS/imcs.spec"

### Build the RPM on a server
1. Once the repo has been cloned, run "sh ./bootstrap.sh"
2. CD to ~/rpmbuild
3. Run "rpmbuild -ba SPECS/imcs.spec"

### Install the RPM

Install the built RPM by running "sudo yum install RPMS/x86_64/imcs.rpm"

## Configuration

Edit the SPEC file to make changes to the build configuration.

## Usage

imcs will be installed in /usr/bin

=======
# imcs-el6-rpm
RPM Package for the In-Memory Column Store for Postgres
>>>>>>> efa75090b0450a293eb235fdd3c53daf12e0ba06
