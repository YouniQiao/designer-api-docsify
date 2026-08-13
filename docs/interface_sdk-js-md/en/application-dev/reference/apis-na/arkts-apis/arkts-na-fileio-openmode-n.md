# OpenMode

Enumerates the constants of the **mode** parameter used in **open()**, which specifies the file opening mode, such as **READ_ONLY**, **WRITE_ONLY**, **READ_WRITE**, or **CREATE**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-fileIo-namespace OpenMode--><!--Device-fileIo-namespace OpenMode-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Summary

### Constants

| Name | Description |
| --- | --- |
| [READ_ONLY](arkts-na-openmode-con.md#READ_ONLY) | Read only Permission. The value is 0o0. |
| [WRITE_ONLY](arkts-na-openmode-con.md#WRITE_ONLY) | Write only Permission. The value is 0o1. |
| [READ_WRITE](arkts-na-openmode-con.md#READ_WRITE) | Write and Read Permission. The value is 0o2. |
| [CREATE](arkts-na-openmode-con.md#CREATE) | If not exist, create file. The value is 0o100. |
| [TRUNC](arkts-na-openmode-con.md#TRUNC) | File truncate len 0. The value is 0o1000. |
| [APPEND](arkts-na-openmode-con.md#APPEND) | File append write. The value is 0o2000. |
| [NONBLOCK](arkts-na-openmode-con.md#NONBLOCK) | File open in nonblocking mode. The value is 0o4000. |
| [DIR](arkts-na-openmode-con.md#DIR) | File is Dir. The value is 0o200000. |
| [NOFOLLOW](arkts-na-openmode-con.md#NOFOLLOW) | File is not symbolic link. The value is 0o400000. |
| [SYNC](arkts-na-openmode-con.md#SYNC) | SYNC IO. The value is 0o4010000. |
| [UNCACHE](arkts-na-openmode-con.md#UNCACHE) | UNCACHE IO. The value is 0o10000000000. |

