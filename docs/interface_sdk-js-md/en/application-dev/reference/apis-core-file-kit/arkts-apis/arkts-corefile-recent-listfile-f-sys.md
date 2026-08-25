# listFile (System API)

## Modules to Import

```TypeScript
import { recent } from 'kits/@kit.CoreFileKit';
```

## listFile

```TypeScript
function listFile(): Array<FileInfo>
```

Lists the files that are accessed recently.

**Since:** 10

**Deprecated since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;FileInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900002 |
| 13900020 |
| 13900042 |
