Name: cflow
Version: 2.0
Release: 2cl
Summary: Show C language call structure
Summary(pt_BR): Mostra a estrutura de chamadas de funções em fontes de linguagem C
Summary(es): Show C language call structure
License: Public Domain
Group: Development
Group(pt_BR): Desenvolvimento
Group(es): Desarrollo
Source0: http://www.ibiblio.org/pub/Linux/devel/lang/c/%{name}-%{version}.tar.gz
Source1: %{name}.conf
Patch: %{name}-%{version}-config.patch
Requires: gcc, mktemp
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Show C language call structure

%description -l pt_BR
Mostra a estrutura de chamadas de funções em fontes de linguagem C

%description -l es
Show C language call structure

%prep
%setup -q
%patch -p1

%build
make PRCC_LOC=%{_bindir}/prcc PRCG_LOC=%{_bindir}/prcg

%install
mkdir -p %{buildroot}/{%{_bindir},%{_sysconfdir},%{_mandir}/man1}
make PREFIX=%{buildroot}/%{_prefix} install
cp %{name}.1 %{buildroot}/%{_mandir}/man1
cp %{_sourcedir}/%{name}.conf %{buildroot}/%{_sysconfdir}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc INSTALL README TODO %{name}.lsm examples
%{_mandir}/man1/%{name}*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%defattr(0755,root,root)
%{_bindir}/%{name}
%{_bindir}/prcc
%{_bindir}/prcg

%changelog
* Tue Aug 28 2001 Claudio Matsuoka <claudio@conectiva.com>
+ cflow-2.0-2cl
- fixed source url
- fixed three (!) typos in a single line of the supplied config file ;)
- changed YACC setting in the supplied config file to "yacc"
- set config file to noreplace for policy compliance
- a plain rebuild seemed to fix the broken prcc of 2.0-1cl

* Thu Nov  2 2000 Arnaldo Carvalho de Melo <acme@conectiva.com>
+ cflow-2.0-1cl
- initial packaging for Conectiva Linux
