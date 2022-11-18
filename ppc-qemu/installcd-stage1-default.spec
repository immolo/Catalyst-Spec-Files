subarch: ppc
target: livecd-stage1
version_stamp: 2022-11-18
rel_type: default
interpreter: /usr/bin/qemu-ppc
profile: default/linux/ppc/17.0
snapshot: 2002.11.18
source_subpath: default/stage3-ppc-openrc-20221111T024809Z
compression_mode: pixz
portage_confdir: /home/immolo/Catalyst-Spec-Files/releases/portage/isos-qemu
common_flags: -Os -mcpu=powerpc -mtune=powerpc -pipe
livecd/use:
	compile-locales
	fbcon
	ipv6
	livecd
	modules
	ncurses
	nls
	nptl
	pam
	readline
	socks5
	ssl
	unicode
	xml

livecd/packages:
	app-admin/pwgen
	app-admin/syslog-ng
	app-arch/unzip
	app-crypt/gnupg
	app-laptop/pbbuttonsd
	app-misc/livecd-tools
	app-misc/screen
	app-misc/neofetch
	app-portage/cpuid2cpuflags
	app-portage/mirrorselect
	app-text/wgetpaste
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-dialup/mingetty
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	#net-fs/cifs-utils
	net-fs/nfs-utils
	net-irc/irssi
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/openssh
	net-misc/rdate
	net-misc/rsync
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-apps/busybox
	sys-apps/ethtool
	sys-apps/fxload
	sys-apps/hdparm
	sys-apps/ibm-powerpc-utils
	sys-apps/iproute2
	sys-apps/lm-sensors
	sys-apps/memtester
	sys-apps/pcmciautils
	sys-apps/powerpc-utils
#	PPC musl issue with sg3_utils
#	sys-apps/sdparm
	sys-auth/ssh-import-id
	sys-block/parted
	sys-boot/grub
	sys-firmware/b43-firmware
	sys-firmware/b43legacy-firmware
	sys-fs/bcache-tools
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/hfsplusutils
	sys-fs/hfsutils
	sys-fs/iprutils
#	PPC Musl issue
#	sys-fs/jfsutils
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/ntfs3g
#	Musl ppc issue
#	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-libs/gpm
	www-client/links