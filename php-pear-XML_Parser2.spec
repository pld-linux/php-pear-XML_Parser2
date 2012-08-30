# $Revision: 1.31 $, $Date: 2011/04/10 20:45:35 $
%define		status		beta
%define		pearname	XML_Parser2
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - XML parsing class based on PHP's bundled expat
Name:		php-pear-XML_Parser2
Version:	0.1.0
Release:	2
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	9f02b81fa8e45d63be15156f9b0088b9
URL:		http://pear.php.net/package/XML_Parser2/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-pear
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an XML parser based on PHPs built-in xml extension. It
supports two basic modes of operation: "func" and "event". In "func"
mode, it will look for a function named after each element
(xmltag_ELEMENT for start tags and xmltag_ELEMENT_ for end tags), and
in "event" mode it uses a set of generic callbacks.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv docs/XML_Parser2/examples .

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/Parser2.php
%{php_pear_dir}/XML/Parser2
%{php_pear_dir}/data/XML_Parser2
%{_examplesdir}/%{name}-%{version}
