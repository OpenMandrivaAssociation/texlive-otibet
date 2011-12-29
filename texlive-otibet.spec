# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-otibet
Version:	20111103
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
%{_texmfdistdir}/fonts/ofm/public/otibet/otibetan.ofm
%{_texmfdistdir}/fonts/ovf/public/otibet/otibetan.ovf
%{_texmfdistdir}/fonts/ovp/public/otibet/otibetan.ovp
%{_texmfdistdir}/fonts/source/public/otibet/bzrsetup.mf
%{_texmfdistdir}/fonts/source/public/otibet/tibetan.mf
%{_texmfdistdir}/fonts/tfm/public/otibet/tibetan.tfm
%{_texmfdistdir}/omega/ocp/otibet/tibadjusttsheg.ocp
%{_texmfdistdir}/omega/ocp/otibet/tibinunicode.ocp
%{_texmfdistdir}/omega/ocp/otibet/tibinwylie.ocp
%{_texmfdistdir}/omega/ocp/otibet/tibout.ocp
%{_texmfdistdir}/omega/ocp/otibet/tibspecial.ocp
%{_texmfdistdir}/omega/ocp/otibet/tibuniuni.ocp
%{_texmfdistdir}/omega/ocp/otibet/tibvowel.ocp
%{_texmfdistdir}/omega/otp/otibet/tibadjusttsheg.otp
%{_texmfdistdir}/omega/otp/otibet/tibetan-mule2uni-old.otp
%{_texmfdistdir}/omega/otp/otibet/tibetan-mule2uni.otp
%{_texmfdistdir}/omega/otp/otibet/tibinunicode.otp
%{_texmfdistdir}/omega/otp/otibet/tibinwylie.otp
%{_texmfdistdir}/omega/otp/otibet/tibout.otp
%{_texmfdistdir}/omega/otp/otibet/tibshow.otp
%{_texmfdistdir}/omega/otp/otibet/tibspecial.otp
%{_texmfdistdir}/omega/otp/otibet/tibuniuni.otp
%{_texmfdistdir}/omega/otp/otibet/tibvowel.otp
%{_texmfdistdir}/tex/latex/otibet/ot1tib.fd
%{_texmfdistdir}/tex/latex/otibet/otibet.sty
%{_texmfdistdir}/tex/latex/otibet/otibet.tex
%{_texmfdistdir}/tex/latex/otibet/t1tib.fd
%doc %{_texmfdistdir}/doc/latex/otibet/README
%doc %{_texmfdistdir}/doc/latex/otibet/allbasic-mule.tex
%doc %{_texmfdistdir}/doc/latex/otibet/allbasic.dvi
%doc %{_texmfdistdir}/doc/latex/otibet/allbasic.tex
%doc %{_texmfdistdir}/doc/latex/otibet/otibet-mule.tex
%doc %{_texmfdistdir}/doc/latex/otibet/testtib.tex
%doc %{_texmfdistdir}/doc/latex/otibet/tiblatex.dvi
%doc %{_texmfdistdir}/doc/latex/otibet/tiblatex.tex
%doc %{_texmfdistdir}/doc/latex/otibet/unidoc.dvi
%doc %{_texmfdistdir}/doc/latex/otibet/unidoc.tex
%doc %{_texmfdistdir}/doc/latex/otibet/yugpacan.dvi
%doc %{_texmfdistdir}/doc/latex/otibet/yugpacan.tex
#- source
%doc %{_texmfdistdir}/source/latex/otibet/Makefile
%doc %{_texmfdistdir}/source/latex/otibet/allbasic.odvi
%doc %{_texmfdistdir}/source/latex/otibet/convnum.scm
%doc %{_texmfdistdir}/source/latex/otibet/generate-otp.el
%doc %{_texmfdistdir}/source/latex/otibet/oct2otp.c
%doc %{_texmfdistdir}/source/latex/otibet/pl2ovp.scm
%doc %{_texmfdistdir}/source/latex/otibet/tibetan.pl
%doc %{_texmfdistdir}/source/latex/otibet/tiblatex.odvi
%doc %{_texmfdistdir}/source/latex/otibet/tibovp.scm
%doc %{_texmfdistdir}/source/latex/otibet/unidoc.odvi
%doc %{_texmfdistdir}/source/latex/otibet/yugpacan.odvi

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts omega tex doc source %{buildroot}%{_texmfdistdir}
