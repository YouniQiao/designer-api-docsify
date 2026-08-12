# download

## Modules to Import

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
```

## download

```TypeScript
function download(url: string, options: CacheDownloadOptions): void
```

Downloads a task from a specified URL. If the transfer is successful, the data is downloaded to the memory cache and file cache.

- After automatically decompressing during HTTP transmission, the size of the target resource cannot exceed 20971  
520 bytes (20 MB). Otherwise, the resource fails to store in the memory cache or file cache.  
- When caching the downloaded data, if the data already exists in the destination URL, the new data will   
overwrite the old one.  
- In addition, the system determines whether to store the target resource in a specified location based on each   
cache type's size limit in **cacheDownload**. By default, the LRU mode is used to replace the existing cached data.  
- This API returns the result synchronously, without blocking the calling thread.

**Since:** 18

**Required permissions:** ohos.permission.INTERNET

<!--Device-cacheDownload-function download(url: string, options: CacheDownloadOptions): void--><!--Device-cacheDownload-function download(url: string, options: CacheDownloadOptions): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |
| options | [CacheDownloadOptions](arkts-basicservices-cachedownload-cachedownloadoptions-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { cacheDownload, BusinessError } from '@kit.BasicServicesKit';

// Provide configuration options for the download task.
let options: cacheDownload.CacheDownloadOptions = {
  headers: { 'Accept': 'application/json' },
  sslType: cacheDownload.SslType.TLS,
  caPath: '/path/to/ca.pem',
  cacheStrategy: cacheDownload.CacheStrategy.FORCE,
  retry: { maxRetryCount: 1 },
  timeout: {
    networkCheckTimeout: 20,
    httpTotalTimeout: 60,
  }
};

try {
  // Download the resource. If the download is successful, the resource will be cached to the specified file in the application memory or sandbox directory.
  cacheDownload.download("https://www.example.com", options);
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err.code}, err message: ${err.message}`);
}
```
