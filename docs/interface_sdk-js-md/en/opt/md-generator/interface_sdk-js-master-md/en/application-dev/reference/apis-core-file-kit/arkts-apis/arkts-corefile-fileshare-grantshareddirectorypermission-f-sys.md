# grantSharedDirectoryPermission (System API)

## Modules to Import

```TypeScript
```

## grantSharedDirectoryPermission

```TypeScript
function grantSharedDirectoryPermission(): Promise<void>
```

Provides a permission grant for application-shared directories

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_SHARED_FILE

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileShare-function grantSharedDirectoryPermission(): Promise<void>--><!--Device-fileShare-function grantSharedDirectoryPermission(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 13900001 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

async function grantSharedDirectoryPermission() {
  try {
    fileShare.grantSharedDirectoryPermission().then(() => {
      console.info('grantSharedDirectoryPermission success');
    }).catch((err: BusinessError) => {
      console.error(`grantSharedDirectoryPermission err: ${JSON.stringify(err)}`);
    });
  } catch (error) {
    console.error(`grantSharedDirectoryPermission error, Code: ${error.code}, message: ${error.message}`);
  }
}
```
