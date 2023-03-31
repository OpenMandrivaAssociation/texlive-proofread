Name:		texlive-proofread
Version:	61719
Release:	2
Summary:	Commands for inserting annotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/proofread
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proofread.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proofread.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proofread.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines a few LaTeX commands that may be useful
when you proofread a LaTeX document. They allow you to easily
highlight text and add comments in the margin. Vim escape
sequences are provided for inserting or removing these LaTeX
commands in the source. Options are provided for displaying the
document with extra line spacing, and for displaying it in
either corrected or uncorrected state, both without margin
notes. The package is based on code for a text highlighting
command that was published by Antal Spector-Zabusky on
https://tex.stackexchange.com/questions/5959. The main file,
proofread.dtx, is self-extracting, so you can generate the
style file by compiling proofread.dtx with pdfLaTeX. This
package is based on the soul package; so if you plan to
highlight non-ASCII characters, you must compile your source
with either XeTeX- or LuaTeX-based compilers.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/proofread
%{_texmfdistdir}/tex/latex/proofread
%doc %{_texmfdistdir}/doc/latex/proofread

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
