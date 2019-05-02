Name:		texlive-otibet
Version:	20190228
Release:	1
Summary:	TeXLive otibet package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/otibet.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/otibet.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/otibet.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive otibet package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/ofm/public/otibet
%{_texmfdistdir}/fonts/ovf/public/otibet
%{_texmfdistdir}/fonts/ovp/public/otibet
%{_texmfdistdir}/fonts/source/public/otibet
%{_texmfdistdir}/fonts/tfm/public/otibet
%{_texmfdistdir}/omega/ocp/otibet
%{_texmfdistdir}/omega/otp/otibet
%{_texmfdistdir}/tex/latex/otibet
%doc %{_texmfdistdir}/doc/latex/otibet
#- source
%doc %{_texmfdistdir}/source/latex/otibet

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts omega tex doc source %{buildroot}%{_texmfdistdir}
