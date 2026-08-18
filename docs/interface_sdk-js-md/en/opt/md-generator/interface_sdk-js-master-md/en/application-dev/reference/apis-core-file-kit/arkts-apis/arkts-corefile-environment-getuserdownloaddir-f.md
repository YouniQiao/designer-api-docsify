# getUserDownloadDir

## Modules to Import

```TypeScript
```

## getUserDownloadDir

```TypeScript
function getUserDownloadDir(): string
```

Obtains the sandbox path of the pre-authorized **Download** directory.

**Since:** 23

**Required permissions:** 
- API version 11: ohos.permission.READ_WRITE_DOWNLOAD_DIRECTORY

<!--Device-Environment-function getUserDownloadDir(): string--><!--Device-Environment-function getUserDownloadDir(): string-End-->

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
function getUserDownloadDirExample() {
  try {
    let path = Environment.getUserDownloadDir();
    console.info(`Succeeded in getUserDownloadDir, path is ${path}`);
  } catch (err) {
    console.error(`Failed to getUserDownloadDir. Code: ${err.code}, message: ${err.message}`);
  }
}
```
