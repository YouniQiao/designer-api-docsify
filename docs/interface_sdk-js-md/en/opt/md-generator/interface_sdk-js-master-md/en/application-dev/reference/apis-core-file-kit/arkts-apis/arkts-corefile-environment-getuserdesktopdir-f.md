# getUserDesktopDir

## Modules to Import

```TypeScript
```

## getUserDesktopDir

```TypeScript
function getUserDesktopDir(): string
```

Obtains the sandbox path of the pre-authorized **Desktop** directory.

**Since:** 23

**Required permissions:** 
- API version 11: ohos.permission.READ_WRITE_DESKTOP_DIRECTORY

<!--Device-Environment-function getUserDesktopDir(): string--><!--Device-Environment-function getUserDesktopDir(): string-End-->

**System capability:** SystemCapability.FileManagement.File.Environment.FolderObtain

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 13900042 |

**Examples**

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
