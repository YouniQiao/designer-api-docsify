# getUserDocumentDir

## getUserDocumentDir

```TypeScript
function getUserDocumentDir(): string
```

Obtains the sandbox path of the pre-authorized **Document** directory.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 11: ohos.permission.READ_WRITE_DOCUMENTS_DIRECTORY

<!--Device-Environment-function getUserDocumentDir(): string--><!--Device-Environment-function getUserDocumentDir(): string-End-->

**System capability:** SystemCapability.FileManagement.File.Environment.FolderObtain

**Return value:**

| Type | Description |
| --- | --- |
| string | Sandbox path of the **Documents** directory obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed, usually the result returned by VerifyAccessToken.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 11 and later |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| 13900042 | Unknown error. |

**Example**

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

