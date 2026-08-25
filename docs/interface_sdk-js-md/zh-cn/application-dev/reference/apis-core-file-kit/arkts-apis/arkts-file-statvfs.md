# @ohos.file.statvfs(@ohos.file.statvfs (文件系统空间统计))

该模块向应用程序提供获取文件系统总字节数、空闲字节数的ArkTS接口。通过该模块，开发者可以实时掌握文件系统存储状况，避免因存储空间不足导致的应用崩溃，提升用户体验和系统稳定性。使用场景包括：文件下载前检查存储空间、应用安装前进行磁盘空间预估、缓存管理中的空间监控等。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
import { statfs } from 'kits/@kit.CoreFileKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getFreeSize(@ohos.file.statvfs (文件系统空间统计))](arkts-corefile-statfs-getfreesize-f.md) |
| [getFreeSize(@ohos.file.statvfs (文件系统空间统计))](arkts-corefile-statfs-getfreesize-f.md) |
| [getFreeSizeSync(@ohos.file.statvfs (文件系统空间统计))](arkts-corefile-statfs-getfreesizesync-f.md) |
| [getTotalSize(@ohos.file.statvfs (文件系统空间统计))](arkts-corefile-statfs-gettotalsize-f.md) |
| [getTotalSize(@ohos.file.statvfs (文件系统空间统计))](arkts-corefile-statfs-gettotalsize-f.md) |
| [getTotalSizeSync(@ohos.file.statvfs (文件系统空间统计))](arkts-corefile-statfs-gettotalsizesync-f.md) |
