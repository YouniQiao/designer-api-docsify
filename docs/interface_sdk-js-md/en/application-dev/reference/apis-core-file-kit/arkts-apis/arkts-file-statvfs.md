# @ohos.file.statvfs

该模块提供文件系统相关存储信息的功能：向应用程序提供获取文件系统总字节数、空闲字节数的JS接口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace statfs--><!--Device-unnamed-declare namespace statfs-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { statfs } from 'kits/@kit.CoreFileKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getFreeSize](arkts-corefile-statfs-getfreesize-f.md#getfreesize) | 异步方法获取指定文件系统空闲字节数，以Promise形式返回结果。 |
| [getFreeSize](arkts-corefile-statfs-getfreesize-f.md#getfreesize-1) | 异步方法获取指定文件系统空闲字节数，使用callback形式返回结果。 |
| [getFreeSizeSync](arkts-corefile-statfs-getfreesizesync-f.md#getfreesizesync) | 以同步方法获取指定文件系统空闲字节数。 |
| [getTotalSize](arkts-corefile-statfs-gettotalsize-f.md#gettotalsize) | 异步方法获取指定文件系统总字节数，以Promise形式返回结果。 |
| [getTotalSize](arkts-corefile-statfs-gettotalsize-f.md#gettotalsize-1) | 异步方法获取指定文件系统总字节数，使用callback形式返回结果。 |
| [getTotalSizeSync](arkts-corefile-statfs-gettotalsizesync-f.md#gettotalsizesync) | 以同步方法获取指定文件系统总字节数。 |

