rm -rf /usr/bin/git/
rm /etc/paths.d/git
rm /etc/manpaths.d/git
pkgutil --forget --pkgs=GitOSX\.Installer\.git[A-Za-z0-9]*\.[a-z]*.pkg



/usr/local/git/uninstall.sh

# have to update the sourcetree git global config if you switch the account (in preference-> account setting--> preference)