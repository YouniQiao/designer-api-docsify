# getCoreFileSyncState

## Modules to Import

```TypeScript
```

## getCoreFileSyncState

```TypeScript
function getCoreFileSyncState(uri: string): FileState
```

Obtains the upload sync state of a cloud file. This API returns the result synchronously.

**Since:** 23

<!--Device-cloudSync-function getCoreFileSyncState(uri: string): FileState--><!--Device-cloudSync-function getCoreFileSyncState(uri: string): FileState-End-->

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
| 13900004 |
| 13900020 |
| 22400005 |
| 13900002 |
| 14000002 |
| 13900012 |
| 13900031 |
| 13600001 |
| 13900010 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
try {
  let state = cloudSync.getCoreFileSyncState(uri);
} catch (err) {
  let error:BusinessError = err as BusinessError;
  console.error(`getCoreFileSyncState failed with error ${error.code}, message is ${error.message}`);
}
```
