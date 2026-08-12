# unregisterChange

## Modules to Import

```TypeScript
import { cloudSync } from '@kit.CoreFileKit';
```

## unregisterChange

```TypeScript
function unregisterChange(uri: string): void
```

Unsubscribes from the change of a file.

**Since:** 12

<!--Device-cloudSync-function unregisterChange(uri: string): void--><!--Device-cloudSync-function unregisterChange(uri: string): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900001 |
| 13900002 |
| 14000002 |
| 13900012 |

## Examples

```TypeScript
import { fileUri } from '@kit.CoreFileKit';

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
let onCallback1 = (changeData: cloudSync.ChangeData) => {
  if (changeData.type == cloudSync.NotifyType.NOTIFY_ADDED) {
    // file has been added, do something
  } else if (changeData.type== cloudSync.NotifyType.NOTIFY_DELETED) {
    // file has been removed, do something
  }
}
cloudSync.registerChange(uri, false, onCallback1);
// Unregister the listener.
cloudSync.unregisterChange(uri);
```
