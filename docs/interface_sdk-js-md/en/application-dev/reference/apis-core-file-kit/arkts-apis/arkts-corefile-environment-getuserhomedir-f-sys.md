# getUserHomeDir (System API)

## Modules to Import

```TypeScript
import { Environment } from 'kits/@kit.CoreFileKit';
```

## getUserHomeDir

```TypeScript
function getUserHomeDir(): string
```

获取当前用户下应用沙箱路径的内卡目录，该接口仅对具有该系统能力的设备开放。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-Environment-function getUserHomeDir(): string--><!--Device-Environment-function getUserHomeDir(): string-End-->

**System capability:** SystemCapability.FileManagement.File.Environment.FolderObtain

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回当前用户下应用沙箱路径的内卡目录。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 13900042 | Unknown error. |

