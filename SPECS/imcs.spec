##########################
# Set global SPEC variables
############################
%global _version 1.06

%define pg_dir /usr/pgsql-9.4

###############
# Set metadata
###############

Name:    imcs
Version: %{_version}
Release: 1%{?dist}
Summary: In-memory Columnar Store extension for PostgreSQL

Group:   Development/Tools
License: Apache License
URL:     https://github.com/knizhnik/imcs
Source:  https://github.com/knizhnik/imcs/archive/master.tar.gz
Obsoletes: imcs <= 1.05
Provides: imcs = 1.06

%description
Columnar store or vertical representation of data allows to achieve better performance in comparison with classical horizontal representation due to three factors:

        1. Reducing size of fetched data: only columns involved in query are accessed.
        2. Vector operations. Applying an operator to set of values (tile) makes it possible to minimize interpretation cost.
           Also SIMD instructions of modern processors accelerate execution of vector operations.
        3. Compression of data. Certainly compression can also be used for all the records, but independent compression of each
           column can give much better results without significant extra CPU overhead.

#####################
# Build requirements
#####################
BuildRoot: %(mktemp -ud %{_tmppath}/build/%{name}-%{version}-%{release}-XXXXXX)


########################################################
# PREP and SETUP
# The prep directive removes existing build directory
# and extracts source code so we have a fresh code base
# -n defines the name of the directory
#######################################################

%prep

#%setup -q -n %{name}-%{version}
%setup -n imcs-master

###########################################################
# BUILD
# The build directive does initial prep for building,
# then runs the configure script and then make to compile.
# Compiled code is placed in %{buildroot}
###########################################################

%build
CFLAGS="-O3 -Wall -Wno-format-security"
LDFLAGS="-pthread"

###########################################################
# INSTALL
# This directive is where the code is actually installed
# in the %{buildroot} folder in preparation for packaging.
###########################################################

echo $PWD

#%%configure


#make %{?_smp_mflags}
make USE_PGXS=1


%install
%make_install






%files

%{pg_dir}/lib/imcs.so
%{pg_dir}/share/extension/imcs--1.1.sql
%{pg_dir}/share/extension/imcs.control


%doc



%changelog

