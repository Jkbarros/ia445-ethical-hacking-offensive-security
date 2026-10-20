# GetVMinfoV2.txt — VirtualBox lab inventory script

**Source:** [`GetVMinfoV2.txt`](../archive/canvas-submissions/GetVMinfoV2.txt)  
**Course:** IA 445 (EMU) · **Author:** Julio Barros

Batch helper to dump **VirtualBox** VM names, NAT networks, host-only interfaces, DHCP servers, running VMs, and per-VM NIC/OS details (course lab environment documentation).

```bat
"c:\Program Files\Oracle\VirtualBox\VBoxManage" list vms > test.txt
"c:\Program Files\Oracle\VirtualBox\VBoxManage" list natnets
"c:\Program Files\Oracle\VirtualBox\VBoxManage" list hostonlyifs
"c:\Program Files\Oracle\VirtualBox\VBoxManage" list dhcpservers
"c:\Program Files\Oracle\VirtualBox\VBoxManage" list runningvms
for /F "delims= " %%A in (test.txt) do call "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" showvminfo %%A | findstr "Name: NIC VRAM CPUs OS Location"
```

Requires a `test.txt` VM list (see comments in the original file). Run only against **your own** lab VMs.
