# @ohos.request.cacheDownload

The **request** module provides applications with the basic capabilities of file upload and download and background transfer proxy. - The child component **cacheDownload** provides the basic capability of caching application resources in advance. - **cacheDownload** uses the HTTP to download data and caches data resources to the application memory or specified files in the application sandbox directory. - The cached data can be used by specific ArkUI components (such as **Image**) to improve resource loading efficiency. Check whether the ArkUI components support this function by referring to the ArkUI component topics.

**Since:** 23

<!--Device-unnamed-declare namespace cacheDownload--><!--Device-unnamed-declare namespace cacheDownload-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancel](arkts-basicservices-cachedownload-cancel-f.md#cancel) |
| [clearFileCache](arkts-basicservices-cachedownload-clearfilecache-f.md#clearfilecache) |
| [clearMemoryCache](arkts-basicservices-cachedownload-clearmemorycache-f.md#clearmemorycache) |
| [download](arkts-basicservices-cachedownload-download-f.md#download) |
| [getDownloadInfo](arkts-basicservices-cachedownload-getdownloadinfo-f.md#getdownloadinfo) |
| [offDownloadError](arkts-basicservices-cachedownload-offdownloaderror-f.md#offdownloaderror) |
| [offDownloadSuccess](arkts-basicservices-cachedownload-offdownloadsuccess-f.md#offdownloadsuccess) |
| [onDownloadError](arkts-basicservices-cachedownload-ondownloaderror-f.md#ondownloaderror) |
| [onDownloadSuccess](arkts-basicservices-cachedownload-ondownloadsuccess-f.md#ondownloadsuccess) |
| [setDownloadInfoListSize](arkts-basicservices-cachedownload-setdownloadinfolistsize-f.md#setdownloadinfolistsize) |
| [setFileCacheSize](arkts-basicservices-cachedownload-setfilecachesize-f.md#setfilecachesize) |
| [setGlobalRetryOptions](arkts-basicservices-cachedownload-setglobalretryoptions-f.md#setglobalretryoptions) |
| [setGlobalTimeoutOptions](arkts-basicservices-cachedownload-setglobaltimeoutoptions-f.md#setglobaltimeoutoptions) |
| [setMemoryCacheSize](arkts-basicservices-cachedownload-setmemorycachesize-f.md#setmemorycachesize) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CacheDownloadOptions](arkts-basicservices-cachedownload-cachedownloadoptions-i.md) |
| [DownloadError](arkts-basicservices-cachedownload-downloaderror-i.md) |
| [DownloadInfo](arkts-basicservices-cachedownload-downloadinfo-i.md) |
| [NetworkInfo](arkts-basicservices-cachedownload-networkinfo-i.md) |
| [PerformanceInfo](arkts-basicservices-cachedownload-performanceinfo-i.md) |
| [ResourceInfo](arkts-basicservices-cachedownload-resourceinfo-i.md) |
| [RetryOptions](arkts-basicservices-cachedownload-retryoptions-i.md) |
| [TimeoutOptions](arkts-basicservices-cachedownload-timeoutoptions-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CacheStrategy](arkts-basicservices-cachedownload-cachestrategy-e.md) |
| [ErrorCode](arkts-basicservices-cachedownload-errorcode-e.md) |
| [SslType](arkts-basicservices-cachedownload-ssltype-e.md) |
