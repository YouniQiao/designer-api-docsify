# getUserHomeDir (System API)

## Modules to Import

```TypeScript
```

## getUserHomeDir

```TypeScript
function getUserHomeDir(): string
```

Obtains the sandbox path of the built-in card directory of the current user. This API is available only to the devices with the SystemCapability.FileManagement.File.Environment.FolderObtain system capability.

**Since:** 23

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-Environment-function getUserHomeDir(): string--><!--Device-Environment-function getUserHomeDir(): string-End-->

**System capability:** SystemCapability.FileManagement.File.Environment.FolderObtain

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900042 |
