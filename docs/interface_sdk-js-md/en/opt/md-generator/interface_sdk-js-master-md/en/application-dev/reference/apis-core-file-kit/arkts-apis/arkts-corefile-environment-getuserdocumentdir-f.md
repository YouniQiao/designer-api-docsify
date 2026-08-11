# getUserDocumentDir

## Modules to Import

```TypeScript
import { Environment } from 'kits/@kit.CoreFileKit';
```

## getUserDocumentDir

```TypeScript
function getUserDocumentDir(): string
```

Obtains the sandbox path of the pre-authorized **Document** directory.

**Since:** 11

**Required permissions:** 
- API version 11: ohos.permission.READ_WRITE_DOCUMENTS_DIRECTORY

<!--Device-Environment-function getUserDocumentDir(): string--><!--Device-Environment-function getUserDocumentDir(): string-End-->

**System capability:** SystemCapability.FileManagement.File.Environment.FolderObtain

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 13900042 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
function getUserDocumentDirExample() {
  try {
    let path = Environment.getUserDocumentDir();
    console.info(`Succeeded in getUserDocumentDir, path is ${path}`);
  } catch (err) {
    console.error(`Failed to getUserDocumentDir. Code: ${err.code}, message: ${err.message}`);
  }
}
```
