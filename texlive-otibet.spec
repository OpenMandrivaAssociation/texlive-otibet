%global tl_name otibet
%global tl_revision 45777

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	support for Tibetan using Omega
Group:		Publishing
URL:		https://www.ctan.org/pkg/otibet
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/otibet.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/otibet.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/otibet.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
support for Tibetan using Omega

