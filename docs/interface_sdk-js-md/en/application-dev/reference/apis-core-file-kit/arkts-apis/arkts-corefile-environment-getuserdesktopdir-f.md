# getUserDesktopDir

## Modules to Import

```TypeScript
import { Environment } from '@kit.CoreFileKit';
```

## getUserDesktopDir

```TypeScript
function getUserDesktopDir(): string
```

Obtains the sandbox path of the pre-authorized **Desktop** directory.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 11: ohos.permission.READ_WRITE_DESKTOP_DIRECTORY

<!--Device-Environment-function getUserDesktopDir(): string--><!--Device-Environment-function getUserDesktopDir(): string-End-->

**System capability:** SystemCapability.FileManagement.File.Environment.FolderObtain

**Return value:**

| Type | Description |
| --- | --- |
| string | Sandbox path of the **Desktop** directory obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed, usually the result returned by VerifyAccessToken.<br>**Applicable version:** 11 and later |
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

