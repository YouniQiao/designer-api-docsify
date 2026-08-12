# cancel

## Modules to Import

```TypeScript
import { cacheDownload } from '@kit.BasicServicesKit';
```

## cancel

```TypeScript
function cancel(url: string): void
```

Cancels an ongoing download task based on the URL. The saved memory cache and file cache are not affected.

- If there is no download task with the specified URL, this API does not take effect.  
- When this API is used for synchronous execution, the calling thread is not blocked.

**Since:** 18

<!--Device-cacheDownload-function cancel(url: string): void--><!--Device-cacheDownload-function cancel(url: string): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { cacheDownload, BusinessError } from '@kit.BasicServicesKit';

// Provide configuration options for the download task.
let options: cacheDownload.CacheDownloadOptions = {};

try {
  // Download the resource. If the download is successful, the resource will be cached to the specified file in the application memory or sandbox directory. 
  cacheDownload.download("https://www.example.com", options);
} catch (err) {
  console.error(`Failed to download the resource. err code: ${err.code}, err message: ${err.message}`);
}

// Other service logic is omitted here.

try {
  // Cancel the download task when it is not required. The cached data is not affected.
  cacheDownload.cancel("https://www.example.com");
} catch (err) {
  console.error(`Failed to cancel the task. err code: ${err.code}, err message: ${err.message}`);
}
```
