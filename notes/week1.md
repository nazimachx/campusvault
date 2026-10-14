
6.18.54.1-microsoft-standard-WSL2

--------------------------------------------------------

PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
VERSION="26.04.1 LTS (Resolute Raccoon)"
VERSION_CODENAME=resolute
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=resolute
LOGO=ubuntu-logo

--------------------------------------------------------------------------------------------

nazim
uid=1000(nazim) gid=1000(nazim) groups=1000(nazim),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users)

--------------------------------------------------------------------------------------------------------------

USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0  24344 15552 ?        Ss   11:56   0:00 /sbin/init
root           2  0.0  0.0   3804  2508 ?        Sl   11:56   0:00 /init
root           3  0.0  0.0   3664  2136 ?        S    11:56   0:00 init-watcher
root           8  0.0  0.0   3804  2276 ?        Sl   11:56   0:00 plan9 --control-socket 7 --log-level 4 --ser>
root          45  0.0  0.1  50676 17696 ?        S<s  11:56   0:00 /usr/lib/systemd/systemd-journald
systemd+      80  0.0  0.0  22416 14452 ?        Ss   11:56   0:00 /usr/lib/systemd/systemd-resolved
root          86  0.0  0.0  35224 12548 ?        Ss   11:56   0:00 /usr/lib/systemd/systemd-udevd
root         107  0.0  0.0   2888  1948 ?        Ss   11:56   0:00 /bin/sh /usr/lib/systemd/scripts/chronyd-sta>
root         108  0.0  0.0   4472  3092 ?        Ss   11:56   0:00 /usr/sbin/cron -f -P
message+     109  0.0  0.0   8824  5456 ?        Ss   11:56   0:00 @dbus-daemon --system --address=systemd: --n>
root         121  0.0  0.1  44096 29772 ?        Ss   11:56   0:00 /usr/bin/python3 /usr/bin/networkd-dispatche>
root         171  0.0  0.0  18444  9432 ?        Ss   11:56   0:00 /usr/lib/systemd/systemd-logind
syslog       198  0.0  0.0 220548  5720 ?        Ssl  11:56   0:00 /usr/sbin/rsyslogd -n -iNONE
root         218  0.0  0.0   5492  2772 tty1     Ss+  11:56   0:00 /usr/sbin/agetty --noreset --noclear --issue>

--------------------------------------------------------------------------------------------------------------->

State        Recv-Q        Send-Q                Local Address:Port               Peer Address:Port       Proce>
LISTEN       0             4096                     127.0.0.54:53                      0.0.0.0:*
LISTEN       0             1000                 10.255.255.254:53                      0.0.0.0:*
LISTEN       0             4096                  127.0.0.53%lo:53                      0.0.0.0:*

--------------------------------------------------------------------------------------------------------------->

               total        used        free      shared  buff/cache   available
Mem:            15Gi       771Mi        14Gi        57Mi       235Mi        14Gi
Swap:          4.0Gi          0B       4.0Gi
22
