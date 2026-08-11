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

<!--Device-Environment-function getExternalStorageDir(): string--><!--Device-Environment-function getExternalStorageDir(): string-End-->

**System capability:** SystemCapability.FileManagement.File.Environment.FolderObtain

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900042 |
