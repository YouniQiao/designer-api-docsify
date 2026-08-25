# cancel

## Modules to Import

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## cancel

```TypeScript
function cancel(url: string): void
```

Cancels an ongoing download task based on the URL. The saved memory cache and file cache are not affected.  
- If there is no download task with the specified URL, this API does not take effect.  
- When this API is used for synchronous execution, the calling thread is not blocked.

**Since:** 18

**System capability:** SystemCapability.Request.FileTransferAgent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
