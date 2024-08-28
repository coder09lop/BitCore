#!/bin/bash



DiskImage="disck.img"
DiskImageSize=1024*1024*1024



BootLoader="BootLoader.sh"
BootLoaderSize=1024*1024



if [ ! -f "$DISK_IMAGE" ]; then
  dd if=/dev/zero of="$DISK_IMAGE" bs=512 count=1
  dd if="$BOOTLOADER" of="$DISK_IMAGE" bs=512 count=1 conv=notrunc
fi

qemu-system-x86_x64 -hda "$DiskImage" -m 256 -vnc :0