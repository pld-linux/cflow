Summary:	Show C language call structure
Summary(pl.UTF-8):	Pokazywanie struktury wywołań C
Summary(pt_BR.UTF-8):	Mostra a estrutura de chamadas de funções em fontes de linguagem C
Name:		cflow
Version:	2.0
Release:	3.1
License:	Public Domain
Group:		Development/Tools
Source0:	http://www.ibiblio.org/pub/Linux/devel/lang/c/%{name}-%{version}.tar.gz
# Source0-md5:	09d6131980aa770289938f71401e8976
Source1:	%{name}.conf
Patch0:		%{name}-%{version}-config.patch
Requires:	gcc
Requires:	mktemp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Show C language call structure.

%description -l pl.UTF-8
Pokazywanie struktury wywołań C.

%description -l pt_BR.UTF-8
Mostra a estrutura de chamadas de funções em fontes de linguagem C

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} PRCC_LOC=%{_bindir}/prcc PRCG_LOC=%{_bindir}/prcg

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{_sourcedir}/%{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README TODO %{name}.lsm examples
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/prcc
%attr(755,root,root) %{_bindir}/prcg
%{_mandir}/man1/%{name}*
