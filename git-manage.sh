rm -rf /usr/bin/git/
rm /etc/paths.d/git
rm /etc/manpaths.d/git
pkgutil --forget --pkgs=GitOSX\.Installer\.git[A-Za-z0-9]*\.[a-z]*.pkg



/usr/local/git/uninstall.sh