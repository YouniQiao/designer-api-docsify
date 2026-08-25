# getExternalStorageDir (System API)

## Modules to Import

```TypeScript
import { Environment } from 'kits/@kit.CoreFileKit';
```

## getExternalStorageDir

```TypeScript
function getExternalStorageDir(): string
```

Obtains the sandbox path of the root directory of an external storage card. This API is available only to the devices with the SystemCapability.FileManagement.File.Environment.FolderObtain system capability.

**Since:** 11

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

**System capability:** SystemCapability.FileManagement.File.Environment.FolderObtain

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 13900042 |
