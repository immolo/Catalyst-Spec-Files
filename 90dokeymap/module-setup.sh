#!/bin/sh

check() {
	return 0
}

depends() {
	return 0
}

install() {
	inst_hook cmdline 90 "$moddir/parse-cmdline.sh"
	inst_hook pre-mount 90 "$moddir/choose-keymap.sh"
}
