# Adding dokeymap Support

Before proceeding, this requires some knowledge of Catalyst.

## Steps to Setup

**IMPORTANT** If you wish to use your own specs, make sure your dracut 
command-line args follow the ones I have in my spec files.

1. Rebuild Catalyst with the patch in `portage/patches` so it automatically adds `cdroot` to the boot args
2. Add `package.use` and `savedconfig` in `portage/` into the appropiate folders in Catalyst's portage confdir 
3. Make a stage1, I've added one to this repo for conveinience
4. Copy `90dokeymap` into the **stage1 chroot** at `/usr/lib/dracut/modules.d/`
5. Copy `keymaps` into the **stage1 chroot** at `/lib` 
6. Proceed with making a stage2, if you used the one provided, no editing is needed

## Directories in Detail

### portage

In the `portage/` directory there are the directories:

- package.use
- patches
- savedconfig

`package.use` is used to set `savedconfig` on sys-apps/busybox so we can use a custom config for it

`patches` contains a patch that will automatically append `cdroot` to dracut's boot args

`savedconfig` contains a config for sys-apps/busybox that will allow us to use `loadkmap`

### 90dokeymap

This is a dracut module that will display the list of keymaps and allows the user to select one

### keymaps

Taken from genkernel, this is the list of keymaps it has available

### specs

spec files I used to save time for testing.
