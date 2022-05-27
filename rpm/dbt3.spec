%global debug_package %{nil}
%{!?pkgrevision: %global pkgrevision 1}
%{!?pgversion: %global pgversion 14}
%global pkgname dbt3
%define installpath /usr/bin
%define _unpackaged_files_terminate_build 0

Name:          %{pkgname}
Version:       %{pkgversion}
Release:       %{pkgrevision}%{?dist}
Summary:       Fair Use TPC Benchmark(TM) H kit
License:       The Artistic License
Source:        v%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Fair Use TPC Benchmark(TM) H kit

%prep
%setup -q -n dbt3-%{version}

%build
PKG_CONFIG_PATH="/usr/pgsql-%{pgversion}/lib/pkgconfig" PATH=$PATH:/usr/pgsql-%{pgversion}/bin cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/%{installpath}/..
make

%install
%{__install} -d %{buildroot}/%{installpath}
make install

%files
%{installpath}/dbt3-compare-results
%{installpath}/dbt3-generate-report
%{installpath}/dbt3-get-config
%{installpath}/dbt3-load-test
%{installpath}/dbt3-monetdb-create-db
%{installpath}/dbt3-monetdb-create-tables
%{installpath}/dbt3-monetdb-dbstat
%{installpath}/dbt3-monetdb-drop-tables
%{installpath}/dbt3-monetdb-get-query-time
%{installpath}/dbt3-monetdb-get-version
%{installpath}/dbt3-monetdb-load-data
%{installpath}/dbt3-monetdb-rf1
%{installpath}/dbt3-monetdb-rf2
%{installpath}/dbt3-monetdb-start-db
%{installpath}/dbt3-monetdb-stop-db
%{installpath}/dbt3-monetdb-time-statistics
%{installpath}/dbt3-mysql-create-db
%{installpath}/dbt3-mysql-create-tables
%{installpath}/dbt3-mysql-dbstat
%{installpath}/dbt3-mysql-drop-db
%{installpath}/dbt3-mysql-drop-tables
%{installpath}/dbt3-mysql-get-query-time
%{installpath}/dbt3-mysql-get-version
%{installpath}/dbt3-mysql-load-data
%{installpath}/dbt3-mysql-rf1
%{installpath}/dbt3-mysql-rf2
%{installpath}/dbt3-mysql-start-db
%{installpath}/dbt3-mysql-stop-db
%{installpath}/dbt3-mysql-time-statistics
%{installpath}/dbt3-pgsql-create-db
%{installpath}/dbt3-pgsql-create-tables
%{installpath}/dbt3-pgsql-dbstat
%{installpath}/dbt3-pgsql-drop-db
%{installpath}/dbt3-pgsql-drop-tables
%{installpath}/dbt3-pgsql-get-query-time
%{installpath}/dbt3-pgsql-get-version
%{installpath}/dbt3-pgsql-load-data
%{installpath}/dbt3-pgsql-plan-disaster
%{installpath}/dbt3-pgsql-report
%{installpath}/dbt3-pgsql-rf1
%{installpath}/dbt3-pgsql-rf2
%{installpath}/dbt3-pgsql-start-db
%{installpath}/dbt3-pgsql-stop-db
%{installpath}/dbt3-pgsql-time-statistics
%{installpath}/dbt3-pgxl-create-db
%{installpath}/dbt3-pgxl-create-tables
%{installpath}/dbt3-pgxl-dbstat
%{installpath}/dbt3-pgxl-drop-tables
%{installpath}/dbt3-pgxl-load-data
%{installpath}/dbt3-pgxl-start-db
%{installpath}/dbt3-pgxl-stop-db
%{installpath}/dbt3-pgxl-time-statistics
%{installpath}/dbt3-plot-results
%{installpath}/dbt3-post-process
%{installpath}/dbt3-power-score
%{installpath}/dbt3-power-test
%{installpath}/dbt3-run-workload
%{installpath}/dbt3-sysstats
%{installpath}/dbt3-throughput-score
%{installpath}/dbt3-throughput-stream
%{installpath}/dbt3-throughput-stream-wrapper
%{installpath}/dbt3-throughput-test
%{installpath}/dbt3-virtuoso-create-db
%{installpath}/dbt3-virtuoso-create-tables
%{installpath}/dbt3-virtuoso-dbstat
%{installpath}/dbt3-virtuoso-drop-tables
%{installpath}/dbt3-virtuoso-get-query-time
%{installpath}/dbt3-virtuoso-get-version
%{installpath}/dbt3-virtuoso-load-data
%{installpath}/dbt3-virtuoso-load-test
%{installpath}/dbt3-virtuoso-rf1
%{installpath}/dbt3-virtuoso-rf2
%{installpath}/dbt3-virtuoso-start-db
%{installpath}/dbt3-virtuoso-stop-db
%{installpath}/dbt3-virtuoso-time-statistics

%changelog
* Fri Oct 15 2021 Julien Tachoires <julmon@gmail.com> - master-1
- Initial packaging
