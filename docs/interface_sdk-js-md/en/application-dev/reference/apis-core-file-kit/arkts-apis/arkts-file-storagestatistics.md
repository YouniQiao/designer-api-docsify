# @ohos.file.storageStatistics

The **storageStatistics** module provides APIs for obtaining storage space information, including the space of built-in and plug-in memory cards, space occupied by different types of data, and space of application data.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace storageStatistics--><!--Device-unnamed-declare namespace storageStatistics-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

## Modules to Import

```TypeScript
import { storageStatistics } from 'storageStatistics';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getCurrentBundleInodes](arkts-corefile-storagestatistics-getcurrentbundleinodes-f.md#getCurrentBundleInodes) | Get the current bundle inodes. |
| [getCurrentBundleStats](arkts-corefile-storagestatistics-getcurrentbundlestats-f.md#getCurrentBundleStats) | Obtains the storage space (in bytes) of this application. This API uses an asynchronous callback to return the result. |
| [getCurrentBundleStats](arkts-corefile-storagestatistics-getcurrentbundlestats-f.md#getCurrentBundleStats) | Obtains the storage space (in bytes) of this application. This API uses a promise to return the result. |
| [getFreeInodes](arkts-corefile-storagestatistics-getfreeinodes-f.md#getFreeInodes) | Get the free inodes. |
| [getFreeSize](arkts-corefile-storagestatistics-getfreesize-f.md#getFreeSize) | Get the free size. |
| [getTotalInodes](arkts-corefile-storagestatistics-gettotalinodes-f.md#getTotalInodes) | Get the total inodes. |
| [getTotalSize](arkts-corefile-storagestatistics-gettotalsize-f.md#getTotalSize) | Get the total size. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getAllExtBundleStats](arkts-corefile-storagestatistics-getallextbundlestats-f-sys.md#getAllExtBundleStats) | Obtains the space usage of all system applications or system services of a specified user. This API uses a promise to return the result. |
| [getBundleStats](arkts-corefile-storagestatistics-getbundlestats-f-sys.md#getBundleStats) | Obtains the storage space of an application, in bytes. This API uses an asynchronous callback to return the result. |
| [getBundleStats](arkts-corefile-storagestatistics-getbundlestats-f-sys.md#getBundleStats-(System-API)) | Obtains the storage space of an application, in bytes. This API uses a promise to return the result. |
| [getExtBundleStats](arkts-corefile-storagestatistics-getextbundlestats-f-sys.md#getExtBundleStats) | Obtains the space usage of a specified user, system application bundle name, or system service name. This API uses a promise to return the result. |
| [getFreeSize](arkts-corefile-storagestatistics-getfreesize-f-sys.md#getFreeSize) | Obtains the available space (in bytes) of the built-in storage. This API uses an asynchronous callback to return the result. |
| [getFreeSizeOfVolume](arkts-corefile-storagestatistics-getfreesizeofvolume-f-sys.md#getFreeSizeOfVolume) | Get the free size of volume. |
| [getFreeSizeOfVolume](arkts-corefile-storagestatistics-getfreesizeofvolume-f-sys.md#getFreeSizeOfVolume-(System-API)) | Get the free size of volume. |
| [getFreeSizeSync](arkts-corefile-storagestatistics-getfreesizesync-f-sys.md#getFreeSizeSync) | Obtains the available space of the built-in storage, in bytes. This API returns the result synchronously. |
| [getSystemDataSize](arkts-corefile-storagestatistics-getsystemdatasize-f-sys.md#getSystemDataSize) | Get the system data size. |
| [getSystemSize](arkts-corefile-storagestatistics-getsystemsize-f-sys.md#getSystemSize) | Get the system size. |
| [getSystemSize](arkts-corefile-storagestatistics-getsystemsize-f-sys.md#getSystemSize-(System-API)) | Get the system size. |
| [getTotalSize](arkts-corefile-storagestatistics-gettotalsize-f-sys.md#getTotalSize) | Obtains the total size (in bytes) of the built-in storage. This API uses an asynchronous callback to return the result. |
| [getTotalSizeOfVolume](arkts-corefile-storagestatistics-gettotalsizeofvolume-f-sys.md#getTotalSizeOfVolume) | Get the total size of volume. |
| [getTotalSizeOfVolume](arkts-corefile-storagestatistics-gettotalsizeofvolume-f-sys.md#getTotalSizeOfVolume-(System-API)) | Get the total size of volume. |
| [getTotalSizeSync](arkts-corefile-storagestatistics-gettotalsizesync-f-sys.md#getTotalSizeSync) | Obtains the total space of the built-in storage, in bytes. This API returns the result synchronously. |
| [getUserStorageStats](arkts-corefile-storagestatistics-getuserstoragestats-f-sys.md#getUserStorageStats) | Obtains the storage statistics of this user, in bytes. This API uses a promise to return the result. |
| [getUserStorageStats](arkts-corefile-storagestatistics-getuserstoragestats-f-sys.md#getUserStorageStats-(System-API)) | Obtains the storage statistics of this user, in bytes. This API uses an asynchronous callback to return the result. |
| [getUserStorageStats](arkts-corefile-storagestatistics-getuserstoragestats-f-sys.md#getUserStorageStats-(System-API)) | Obtains the storage statistics of the specified user, in bytes. This API uses a promise to return the result. |
| [getUserStorageStats](arkts-corefile-storagestatistics-getuserstoragestats-f-sys.md#getUserStorageStats-(System-API)) | Obtains the storage statistics of the specified user, in bytes. This API uses an asynchronous callback to return the result. |
| [listUserdataDirInfo](arkts-corefile-storagestatistics-listuserdatadirinfo-f-sys.md#listUserdataDirInfo) | Queries the space usage of the **\/data** directory on the user device. This API uses a promise to return the result. |
| [setExtBundleStats](arkts-corefile-storagestatistics-setextbundlestats-f-sys.md#setExtBundleStats) | Reports the space usage of system applications or system services. This API uses a promise to return the result. > **NOTE：**> > If the value of **flag** in **stats** is **false**, the value of **businessName** must be the bundle name of an > application. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [BundleStats](arkts-corefile-storagestatistics-bundlestats-i.md) | Get the bundle statistics. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ExtBundleStats](arkts-corefile-storagestatistics-extbundlestats-i-sys.md) | Details the space usage of system applications or system services. |
| [StorageStats](arkts-corefile-storagestatistics-storagestats-i-sys.md) | Get the user storage statistics. |
| [UserdataDirInfo](arkts-corefile-storagestatistics-userdatadirinfo-i-sys.md) | Details the space usage of the **\/data** directory on the user device. |
<!--DelEnd-->

