# add (System API)

## Modules to Import

```TypeScript
import { recent } from 'kits/@kit.CoreFileKit';
```

## add

```TypeScript
function add(uri: string): void
```

Adds the file of the specified URI to the recent file list.

**Since:** 10

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-recent-function add(uri: string): void--><!--Device-recent-function add(uri: string): void-End-->

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
let uri = 'file://docs/storage/Users/currentUser/<publicPath>';
recent.add(uri);
```
