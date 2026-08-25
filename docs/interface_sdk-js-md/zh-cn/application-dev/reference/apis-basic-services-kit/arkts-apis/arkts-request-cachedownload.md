# @ohos.request.cacheDownload(缓存下载)

request部件主要给应用提供上传下载文件、后台传输代理的基础能力。  
- request的cacheDownload子组件主要给应用提供应用资源提前缓存的基础能力。 - cacheDownload组件使用HTTP协议进行数据下载，并将数据资源缓存至应用内存或应用沙箱目录的指定文件中。 - 这些缓存数据可以被特定的ArkUI组件（例如：Image组件）使用，从而提升资源加载效率。请查看ArkUI组件文档确定组件是否支持该功能。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Request.FileTransferAgent

## 导入模块

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [cancel(缓存下载)](arkts-basicservices-cachedownload-cancel-f.md) |
| [clearFileCache(缓存下载)](arkts-basicservices-cachedownload-clearfilecache-f.md) |
| [clearMemoryCache(缓存下载)](arkts-basicservices-cachedownload-clearmemorycache-f.md) |
| [download(缓存下载)](arkts-basicservices-cachedownload-download-f.md) |
| [getDownloadInfo(缓存下载)](arkts-basicservices-cachedownload-getdownloadinfo-f.md) |
| [offDownloadError(缓存下载)](arkts-basicservices-cachedownload-offdownloaderror-f.md) |
| [offDownloadSuccess(缓存下载)](arkts-basicservices-cachedownload-offdownloadsuccess-f.md) |
| [onDownloadError(缓存下载)](arkts-basicservices-cachedownload-ondownloaderror-f.md) |
| [onDownloadSuccess(缓存下载)](arkts-basicservices-cachedownload-ondownloadsuccess-f.md) |
| [setDownloadInfoListSize(缓存下载)](arkts-basicservices-cachedownload-setdownloadinfolistsize-f.md) |
| [setFileCacheSize(缓存下载)](arkts-basicservices-cachedownload-setfilecachesize-f.md) |
| [setGlobalRetryOptions(缓存下载)](arkts-basicservices-cachedownload-setglobalretryoptions-f.md) |
| [setGlobalTimeoutOptions(缓存下载)](arkts-basicservices-cachedownload-setglobaltimeoutoptions-f.md) |
| [setMemoryCacheSize(缓存下载)](arkts-basicservices-cachedownload-setmemorycachesize-f.md) |

### 接口

| 名称 |
| --- |
| [CacheDownloadOptions(缓存下载)](arkts-basicservices-cachedownload-cachedownloadoptions-i.md) |
| [DownloadError(缓存下载)](arkts-basicservices-cachedownload-downloaderror-i.md) |
| [DownloadInfo(缓存下载)](arkts-basicservices-cachedownload-downloadinfo-i.md) |
| [NetworkInfo(缓存下载)](arkts-basicservices-cachedownload-networkinfo-i.md) |
| [PerformanceInfo(缓存下载)](arkts-basicservices-cachedownload-performanceinfo-i.md) |
| [ResourceInfo(缓存下载)](arkts-basicservices-cachedownload-resourceinfo-i.md) |
| [RetryOptions(缓存下载)](arkts-basicservices-cachedownload-retryoptions-i.md) |
| [TimeoutOptions(缓存下载)](arkts-basicservices-cachedownload-timeoutoptions-i.md) |

### 枚举

| 名称 |
| --- |
| [CacheStrategy(缓存下载)](arkts-basicservices-cachedownload-cachestrategy-e.md) |
| [ErrorCode(缓存下载)](arkts-basicservices-cachedownload-errorcode-e.md) |
| [SslType(缓存下载)](arkts-basicservices-cachedownload-ssltype-e.md) |
