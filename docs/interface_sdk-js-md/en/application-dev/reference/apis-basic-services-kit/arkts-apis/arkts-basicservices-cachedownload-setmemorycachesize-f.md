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

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bytes | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
