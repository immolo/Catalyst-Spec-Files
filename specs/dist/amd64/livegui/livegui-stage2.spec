subarch: amd64
version_stamp: plasma-dist
target: livecd-stage2
rel_type: default
profile: default/linux/amd64/23.0/desktop/plasma
snapshot_treeish: 5988dd0d35f8de593e7cd55d607b2e3743642b52
source_subpath: default/livecd-stage1-amd64-plasma-dist
portage_confdir: /home/immolo/releng/releases/portage/livegui

livecd/bootargs: overlayfs nodhcp secureconsole
livecd/depclean: no
livecd/fstype: squashfs
livecd/iso: livegui-amd64-dm.iso
livecd/type: gentoo-release-livecd
livecd/volid: Gentoo amd64 LiveGUI Dist Kernel

livecd/fsscript: /home/immolo/releng/releases/specs/amd64/livegui/files/fsscript-stage2.sh
livecd/rcadd: udev|sysinit udev-mount|sysinit acpid|default dbus|default gpm|default NetworkManager|default elogind|boot
livecd/unmerge: net-misc/netifrc

livecd/empty:
	/var/db/repos
	/usr/src

boot/kernel: gentoo fallback

boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/dracut_args: --xz --no-hostonly -a dmsquash-live -a mdraid -o btrfs -o crypt -o i18n -o usrmount -o lunmask -o qemu o qemu-net -o nvdimm -o multipath -i /lib/keymaps /lib/keymaps -I busybox

boot/kernel/fallback/sources: gentoo-sources
boot/kernel/fallback/config: /home/immolo/releng/releases/kconfig/amd64/amd64-6.6.21.config
