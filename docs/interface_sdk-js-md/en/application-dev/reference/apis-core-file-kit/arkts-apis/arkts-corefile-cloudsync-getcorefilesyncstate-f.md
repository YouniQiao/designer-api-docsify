# getCoreFileSyncState

## Modules to Import

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## getCoreFileSyncState

```TypeScript
function getCoreFileSyncState(uri: string): FileState
```

Obtains the upload sync state of a cloud file. This API returns the result synchronously.

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FileState](arkts-corefile-cloudsync-filestate-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900002 |
| 13900004 |
| 13900010 |
| 13900012 |
| 13900020 |
| 13900031 |
| 14000002 |
| 22400005 |
