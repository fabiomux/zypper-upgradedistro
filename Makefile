MAKEFLAGS += -s
clean:
	@rm *.tgz
	@echo 'Cleanup done!'
tgz:
	@tar --transform "s|bin|zypper-upgradedistro|" \
	     --transform "s|plugin|zypper-upgradedistro|" \
	     -czvf zypper-upgradedistro-$(shell grep 'Version: [0-9]' './bin/upgradedistro' | cut -f 3 -d ' ').tgz ./bin ./plugin
	@echo 'Archive ready!'
install_script:
	@sudo install -m 755 ./bin/upgradedistro /usr/local/bin/
	@echo 'Script installed!'
install_plugin:
	@sudo install -m 755 ./plugin/zypper-upgradedistro /usr/lib/zypper/commands/
	@sudo install -m 644 ./plugin/zypper-upgradedistro.8 /usr/share/man/man8/
	@echo 'Plugin installed!'
install: install_script install_plugin
	@echo 'Installation completed!'
uninstall_script:
	@sudo rm /usr/local/bin/upgradedistro || true
	@echo 'Script uninstalled!'
uninstall_plugin:
	@sudo rm /usr/lib/zypper/commands/zypper-upgradedistro || true
	@sudo rm /usr/share/man/man8/zypper-upgradedistro.8.gz || true
	@echo 'Plugin uninstalled!'
uninstall: uninstall_script uninstall_plugin
	@echo 'Uninstallation completed!'

