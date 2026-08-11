# recover (System API)

## Modules to Import

```TypeScript
import { trash } from 'kits/@kit.CoreFileKit';
```

## recover

```TypeScript
function recover(uri: string): void
```

Recovers a file or directory from the trash.

**Since:** 10

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-trash-function recover(uri: string): void--><!--Device-trash-function recover(uri: string): void-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900002 |
| 13900042 |

## Examples

```TypeScript
let fileinfos = trash.listFile();
let uri = fileinfos[0].uri;
trash.recover(uri);
```
