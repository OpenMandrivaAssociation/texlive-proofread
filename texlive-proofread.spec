%global tl_name proofread
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.04
Release:	%{tl_revision}.1
Summary:	Commands for inserting annotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/proofread
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/proofread.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/proofread.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/proofread.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines a few LaTeX commands that may be useful when you
proofread a LaTeX document. They allow you to easily highlight text and
add comments in the margin. Vim escape sequences are provided for
inserting or removing these LaTeX commands in the source. Options are
provided for displaying the document with extra line spacing, and for
displaying it in either corrected or uncorrected state, both without
margin notes. The package is based on code for a text highlighting
command that was published by Antal Spector-Zabusky on
https://tex.stackexchange.com/questions/5959. The main file,
proofread.dtx, is self-extracting, so you can generate the style file by
compiling proofread.dtx with pdfLaTeX. This package is based on the soul
package; so if you plan to highlight non-ASCII characters, you must
compile your source with either XeTeX- or LuaTeX-based compilers.

