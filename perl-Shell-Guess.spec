%define upstream_name Shell-Guess
%define upstream_version 0.09

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Make an educated guess about the shell in use
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Shell/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.940.0
BuildArch:  noarch

%description
Shell::Guess makes a reasonably aggressive attempt to determine the
shell being employed by the user, either the shell that executed the
perl script directly (the "running" shell), or the users' login shell
(the "login" shell). It does this by a variety of means available to
it, depending on the platform that it is running on.

%prep
%autosetup -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make_build

%install
%make_install

%files
%doc Changes INSTALL LICENSE META.json META.yml README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/*
