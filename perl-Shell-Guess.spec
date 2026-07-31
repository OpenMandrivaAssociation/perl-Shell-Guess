%define upstream_name Shell-Guess
%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    0.10
Release:    1

Summary:    Make an educated guess about the shell in use
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Shell/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
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
%autosetup -n Shell-Guess-0.10

%build
perl Makefile.PL INSTALLDIRS=vendor

%make_build

%install
%make_install

%files
%doc Changes INSTALL LICENSE META.json META.yml README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/*
