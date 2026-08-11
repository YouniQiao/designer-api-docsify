# setMemoryCacheSize

## Modules to Import

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## setMemoryCacheSize

```TypeScript
function setMemoryCacheSize(bytes: number): void
```

Sets the upper limit of the memory cache size for the **cacheDownload** component.

- When this API is used to adjust the cache size, the LRU mode is used by default to clear redundant cached data   
in the memory.  
- This API returns the result synchronously, without blocking the calling thread.

**Since:** 18

<!--Device-cacheDownload-function setMemoryCacheSize(bytes: long): void--><!--Device-cacheDownload-function setMemoryCacheSize(bytes: long): void-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bytes | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { cacheDownload, BusinessError } from '@kit.BasicServicesKit';

try {
  // Set the upper limit of the memory cache size. 
  cacheDownload.setMemoryCacheSize(10 * 1024 * 1024);
} catch (err) {
  console.error(`Failed to set memory cache size. err code: ${err.code}, err message: ${err.message}`);
}
```
