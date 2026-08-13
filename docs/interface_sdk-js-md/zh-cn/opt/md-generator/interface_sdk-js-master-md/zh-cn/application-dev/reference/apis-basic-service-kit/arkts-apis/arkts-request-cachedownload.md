# @ohos.request.cacheDownload

request部件主要给应用提供上传下载文件、后台传输代理的基础能力。 - request的cacheDownload子组件主要给应用提供应用资源提前缓存的基础能力。 - cacheDownload组件使用HTTP协议进行数据下载，并将数据资源缓存至应用内存或应用沙箱目录的指定文件中。 - 这些缓存数据可以被特定的ArkUI组件（例如：Image组件）使用，从而提升资源加载效率。请查看ArkUI组件文档确定组件是否支持该功能。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace cacheDownload--><!--Device-unnamed-declare namespace cacheDownload-End-->

**系统能力：** SystemCapability.Request.FileTransferAgent

## 汇总

### 函数

| 名称 |
| --- |
| [cancel](arkts-basicservices-cachedownload-cancel-f.md#cancel) |
| [clearFileCache](arkts-basicservices-cachedownload-clearfilecache-f.md#clearFileCache) |
| [clearMemoryCache](arkts-basicservices-cachedownload-clearmemorycache-f.md#clearMemoryCache) |
| [download](arkts-basicservices-cachedownload-download-f.md#download) |
| [getDownloadInfo](arkts-basicservices-cachedownload-getdownloadinfo-f.md#getDownloadInfo) |
| [offDownloadError](arkts-basicservices-cachedownload-offdownloaderror-f.md#offDownloadError) |
| [offDownloadSuccess](arkts-basicservices-cachedownload-offdownloadsuccess-f.md#offDownloadSuccess) |
| [onDownloadError](arkts-basicservices-cachedownload-ondownloaderror-f.md#onDownloadError) |
| [onDownloadSuccess](arkts-basicservices-cachedownload-ondownloadsuccess-f.md#onDownloadSuccess) |
| [setDownloadInfoListSize](arkts-basicservices-cachedownload-setdownloadinfolistsize-f.md#setDownloadInfoListSize) |
| [setFileCacheSize](arkts-basicservices-cachedownload-setfilecachesize-f.md#setFileCacheSize) |
| [setGlobalRetryOptions](arkts-basicservices-cachedownload-setglobalretryoptions-f.md#setGlobalRetryOptions) |
| [setGlobalTimeoutOptions](arkts-basicservices-cachedownload-setglobaltimeoutoptions-f.md#setGlobalTimeoutOptions) |
| [setMemoryCacheSize](arkts-basicservices-cachedownload-setmemorycachesize-f.md#setMemoryCacheSize) |

### 接口

| 名称 |
| --- |
| [CacheDownloadOptions](arkts-basicservices-cachedownload-cachedownloadoptions-i.md) |
| [DownloadError](arkts-basicservices-cachedownload-downloaderror-i.md) |
| [DownloadInfo](arkts-basicservices-cachedownload-downloadinfo-i.md) |
| [NetworkInfo](arkts-basicservices-cachedownload-networkinfo-i.md) |
| [PerformanceInfo](arkts-basicservices-cachedownload-performanceinfo-i.md) |
| [ResourceInfo](arkts-basicservices-cachedownload-resourceinfo-i.md) |
| [RetryOptions](arkts-basicservices-cachedownload-retryoptions-i.md) |
| [TimeoutOptions](arkts-basicservices-cachedownload-timeoutoptions-i.md) |

### 枚举

| 名称 |
| --- |
| [CacheStrategy](arkts-basicservices-cachedownload-cachestrategy-e.md) |
| [ErrorCode](arkts-basicservices-cachedownload-errorcode-e.md) |
| [SslType](arkts-basicservices-cachedownload-ssltype-e.md) |
