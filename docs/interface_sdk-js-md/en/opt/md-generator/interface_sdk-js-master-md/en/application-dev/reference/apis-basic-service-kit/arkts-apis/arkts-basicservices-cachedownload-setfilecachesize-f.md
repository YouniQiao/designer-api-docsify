# setFileCacheSize

## Modules to Import

```TypeScript
```

## setFileCacheSize

```TypeScript
function setFileCacheSize(bytes: number): void
```

Sets the upper limit of the file cache size for the **cacheDownload** component. - When this API is used to adjust the cache size, the LRU mode is used by default to clear redundant cached data in the file. - If **bytes** is set to **0**, all cached files will be deleted. - This API returns the result synchronously, without blocking the calling thread.

**Since:** 23

<!--Device-cacheDownload-function setFileCacheSize(bytes: long): void--><!--Device-cacheDownload-function setFileCacheSize(bytes: long): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bytes | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

**Examples**

```TypeScript
import { cacheDownload, BusinessError } from '@kit.BasicServicesKit';

try {
  // Set the upper limit of the file cache size. 
  cacheDownload.setFileCacheSize(100 * 1024 * 1024);
} catch (err) {
  console.error(`Failed to set file cache size. err code: ${err.code}, err message: ${err.message}`);
}
```
