# getUserDesktopDir

## Modules to Import

```TypeScript
import { Environment } from 'kits/@kit.CoreFileKit';
```

## getUserDesktopDir

```TypeScript
function getUserDesktopDir(): string
```

获取当前用户预授权桌面目录的沙箱路径。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 11: ohos.permission.READ_WRITE_DESKTOP_DIRECTORY

<!--Device-Environment-function getUserDesktopDir(): string--><!--Device-Environment-function getUserDesktopDir(): string-End-->

**System capability:** SystemCapability.FileManagement.File.Environment.FolderObtain

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回当前用户预授权桌面目录的沙箱路径。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken.<br>**Applicable version:** 11 and later |
| 13900042 | Unknown error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
function getUserDesktopDirExample() {
  try {
    let path = Environment.getUserDesktopDir();
    console.info(`Succeeded in getUserDesktopDir, path is ${path}`);
  } catch (err) {
    console.error(`Failed to getUserDesktopDir. Code: ${err.code}, message: ${err.message}`);
  }
}
```

