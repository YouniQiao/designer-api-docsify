# @ohos.file.storageStatistics

该模块提供空间查询相关的常用功能：包括对内置存储和外置存储卡的空间查询、对应用分类数据统计的查询、 对应用数据的查询、对文件系统inode资源（总量、剩余量及当前应用占用量）的查询等。适用于存储空间管理、 系统监控、应用存储优化等场景，帮助开发者实时掌握设备存储和inode资源使用情况，合理规划存储策略， 避免因存储空间或inode资源不足导致应用异常。

**起始版本：** 8

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

## 导入模块

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getCurrentBundleInodes](arkts-corefile-storagestatistics-getcurrentbundleinodes-f.md) |
| [getCurrentBundleStats](arkts-corefile-storagestatistics-getcurrentbundlestats-f.md) |
| [getCurrentBundleStats](arkts-corefile-storagestatistics-getcurrentbundlestats-f.md) |
| [getFreeInodes](arkts-corefile-storagestatistics-getfreeinodes-f.md) |
| [getFreeSize](arkts-corefile-storagestatistics-getfreesize-f.md) |
| [getFreeSize](arkts-corefile-storagestatistics-getfreesize-f.md) |
| [getFreeSizeSync](arkts-corefile-storagestatistics-getfreesizesync-f.md) |
| [getTotalInodes](arkts-corefile-storagestatistics-gettotalinodes-f.md) |
| [getTotalSize](arkts-corefile-storagestatistics-gettotalsize-f.md) |
| [getTotalSize](arkts-corefile-storagestatistics-gettotalsize-f.md) |
| [getTotalSizeSync](arkts-corefile-storagestatistics-gettotalsizesync-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getAllExtBundleStats](arkts-corefile-storagestatistics-getallextbundlestats-f-sys.md) |
| [getBundleStats](arkts-corefile-storagestatistics-getbundlestats-f-sys.md) |
| [getBundleStats](arkts-corefile-storagestatistics-getbundlestats-f-sys.md) |
| [getExtBundleStats](arkts-corefile-storagestatistics-getextbundlestats-f-sys.md) |
| [getFreeSizeOfVolume](arkts-corefile-storagestatistics-getfreesizeofvolume-f-sys.md) |
| [getFreeSizeOfVolume](arkts-corefile-storagestatistics-getfreesizeofvolume-f-sys.md) |
| [getSystemDataSize](arkts-corefile-storagestatistics-getsystemdatasize-f-sys.md) |
| [getSystemSize](arkts-corefile-storagestatistics-getsystemsize-f-sys.md) |
| [getSystemSize](arkts-corefile-storagestatistics-getsystemsize-f-sys.md) |
| [getTotalSizeOfVolume](arkts-corefile-storagestatistics-gettotalsizeofvolume-f-sys.md) |
| [getTotalSizeOfVolume](arkts-corefile-storagestatistics-gettotalsizeofvolume-f-sys.md) |
| [getUserStorageStats](arkts-corefile-storagestatistics-getuserstoragestats-f-sys.md) |
| [getUserStorageStats](arkts-corefile-storagestatistics-getuserstoragestats-f-sys.md) |
| [getUserStorageStats](arkts-corefile-storagestatistics-getuserstoragestats-f-sys.md) |
| [getUserStorageStats](arkts-corefile-storagestatistics-getuserstoragestats-f-sys.md) |
| [listUserdataDirInfo](arkts-corefile-storagestatistics-listuserdatadirinfo-f-sys.md) |
| [setExtBundleStats](arkts-corefile-storagestatistics-setextbundlestats-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [BundleStats](arkts-corefile-storagestatistics-bundlestats-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ExtBundleStats](arkts-corefile-storagestatistics-extbundlestats-i-sys.md) |
| [StorageStats](arkts-corefile-storagestatistics-storagestats-i-sys.md) |
| [UserdataDirInfo](arkts-corefile-storagestatistics-userdatadirinfo-i-sys.md) |
<!--DelEnd-->
