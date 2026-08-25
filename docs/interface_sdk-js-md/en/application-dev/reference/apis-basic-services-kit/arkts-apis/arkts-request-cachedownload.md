# @ohos.request.cacheDownload(Download and Cache)

The **request** module provides applications with the basic capabilities of file upload and download and background transfer proxy.  
- The child component **cacheDownload** provides the basic capability of caching application resources in advance. - **cacheDownload** uses the HTTP to download data and caches data resources to the application memory or specified files in the application sandbox directory. - The cached data can be used by specific ArkUI components (such as **Image**) to improve resource loading efficiency. Check whether the ArkUI components support this function by referring to the ArkUI component topics.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Request.FileTransferAgent

## Modules to Import

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancel(Download and Cache)](arkts-basicservices-cachedownload-cancel-f.md) |
| [clearFileCache(Download and Cache)](arkts-basicservices-cachedownload-clearfilecache-f.md) |
| [clearMemoryCache(Download and Cache)](arkts-basicservices-cachedownload-clearmemorycache-f.md) |
| [download(Download and Cache)](arkts-basicservices-cachedownload-download-f.md) |
| [getDownloadInfo(Download and Cache)](arkts-basicservices-cachedownload-getdownloadinfo-f.md) |
| [offDownloadError(Download and Cache)](arkts-basicservices-cachedownload-offdownloaderror-f.md) |
| [offDownloadSuccess(Download and Cache)](arkts-basicservices-cachedownload-offdownloadsuccess-f.md) |
| [onDownloadError(Download and Cache)](arkts-basicservices-cachedownload-ondownloaderror-f.md) |
| [onDownloadSuccess(Download and Cache)](arkts-basicservices-cachedownload-ondownloadsuccess-f.md) |
| [setDownloadInfoListSize(Download and Cache)](arkts-basicservices-cachedownload-setdownloadinfolistsize-f.md) |
| [setFileCacheSize(Download and Cache)](arkts-basicservices-cachedownload-setfilecachesize-f.md) |
| [setGlobalRetryOptions(Download and Cache)](arkts-basicservices-cachedownload-setglobalretryoptions-f.md) |
| [setGlobalTimeoutOptions(Download and Cache)](arkts-basicservices-cachedownload-setglobaltimeoutoptions-f.md) |
| [setMemoryCacheSize(Download and Cache)](arkts-basicservices-cachedownload-setmemorycachesize-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CacheDownloadOptions(Download and Cache)](arkts-basicservices-cachedownload-cachedownloadoptions-i.md) |
| [DownloadError(Download and Cache)](arkts-basicservices-cachedownload-downloaderror-i.md) |
| [DownloadInfo(Download and Cache)](arkts-basicservices-cachedownload-downloadinfo-i.md) |
| [NetworkInfo(Download and Cache)](arkts-basicservices-cachedownload-networkinfo-i.md) |
| [PerformanceInfo(Download and Cache)](arkts-basicservices-cachedownload-performanceinfo-i.md) |
| [ResourceInfo(Download and Cache)](arkts-basicservices-cachedownload-resourceinfo-i.md) |
| [RetryOptions(Download and Cache)](arkts-basicservices-cachedownload-retryoptions-i.md) |
| [TimeoutOptions(Download and Cache)](arkts-basicservices-cachedownload-timeoutoptions-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CacheStrategy(Download and Cache)](arkts-basicservices-cachedownload-cachestrategy-e.md) |
| [ErrorCode(Download and Cache)](arkts-basicservices-cachedownload-errorcode-e.md) |
| [SslType(Download and Cache)](arkts-basicservices-cachedownload-ssltype-e.md) |
