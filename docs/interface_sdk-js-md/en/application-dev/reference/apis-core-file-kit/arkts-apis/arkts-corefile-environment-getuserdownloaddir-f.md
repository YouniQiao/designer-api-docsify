# getUserDownloadDir

## Modules to Import

```TypeScript
import { Environment } from 'kits/@kit.CoreFileKit';
```

## getUserDownloadDir

```TypeScript
function getUserDownloadDir(): string
```

Obtains the sandbox path of the pre-authorized **Download** directory.

**Since:** 11

**Required permissions:** 
- API version 11: ohos.permission.READ_WRITE_DOWNLOAD_DIRECTORY

**System capability:** SystemCapability.FileManagement.File.Environment.FolderObtain

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 13900042 |
