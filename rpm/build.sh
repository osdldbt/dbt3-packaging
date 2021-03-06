#!/bin/bash -eux

# DBT-3 version
VERSION="1.11.0"
TAG="v$VERSION"

dnf update -y
dnf install -y rpm-build redhat-rpm-config yum-utils curl unzip cmake make

yum-builddep -y /workspace/rpm/dbt3.spec

(cd /workspace && curl -OL https://github.com/osdldbt/dbt3/archive/refs/tags/${TAG}.tar.gz)

rpmbuild \
	--clean \
	--define "pkgversion ${VERSION}" \
	--define "_topdir ${PWD}/tmp/rpm" \
	--define "_sourcedir ${PWD}/workspace" \
	-bb /workspace/rpm/dbt3.spec

rm /workspace/${TAG}.tar.gz
mkdir -p ${PWD}/workspace/rpm/build/
cp ${PWD}/tmp/rpm/RPMS/*/*.rpm ${PWD}/workspace/rpm/build/.
chown ${1}:${2} -R ${PWD}/workspace/rpm/build/
ls -lha ${PWD}/workspace/rpm/build/*.rpm
