# OpenMode

Enumerates the constants of the **mode** parameter used in **open()**, which specifies the file opening mode, such as **READ_ONLY**, **WRITE_ONLY**, **READ_WRITE**, or **CREATE**.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-fileIo-namespace OpenMode--><!--Device-fileIo-namespace OpenMode-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
```

## Summary

### Constants

| Name | Description |
| --- | --- |
| [READ_ONLY](arkts-openmode-con.md#read_only) | Read only Permission. The value is 0o0. |
| [WRITE_ONLY](arkts-openmode-con.md#write_only) | Write only Permission. The value is 0o1. |
| [READ_WRITE](arkts-openmode-con.md#read_write) | Write and Read Permission. The value is 0o2. |
| [CREATE](arkts-openmode-con.md#create) | If not exist, create file. The value is 0o100. |
| [TRUNC](arkts-openmode-con.md#trunc) | File truncate len 0. The value is 0o1000. |
| [APPEND](arkts-openmode-con.md#append) | File append write. The value is 0o2000. |
| [NONBLOCK](arkts-openmode-con.md#nonblock) | File open in nonblocking mode. The value is 0o4000. |
| [DIR](arkts-openmode-con.md#dir) | File is Dir. The value is 0o200000. |
| [NOFOLLOW](arkts-openmode-con.md#nofollow) | File is not symbolic link. The value is 0o400000. |
| [SYNC](arkts-openmode-con.md#sync) | SYNC IO. The value is 0o4010000. |
| [UNCACHE](arkts-openmode-con.md#uncache) | UNCACHE IO. The value is 0o10000000000. |

