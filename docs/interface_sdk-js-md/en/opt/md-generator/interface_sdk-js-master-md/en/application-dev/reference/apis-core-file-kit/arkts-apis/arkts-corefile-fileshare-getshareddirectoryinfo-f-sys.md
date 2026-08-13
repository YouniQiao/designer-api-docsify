# getSharedDirectoryInfo (System API)

## Modules to Import

```TypeScript
import { fileShare } from '@kit.CoreFileKit';
```

## getSharedDirectoryInfo

```TypeScript
function getSharedDirectoryInfo(): Promise<Array<SharedDirectoryInfo>>
```

Gets the shared sandbox directories of applications

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_SHARED_FILE

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileShare-function getSharedDirectoryInfo(): Promise<Array<SharedDirectoryInfo>>--><!--Device-fileShare-function getSharedDirectoryInfo(): Promise<Array<SharedDirectoryInfo>>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[SharedDirectoryInfo](arkts-corefile-fileshare-shareddirectoryinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 13900001 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900011 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

async function getSharedDirectoryInfo() {
  try {
    fileShare.getSharedDirectoryInfo().then((infos: Array<fileShare.SharedDirectoryInfo>) => {
      infos.forEach((info: fileShare.SharedDirectoryInfo) => {
        console.info(`bundleName=${info.bundleName} path=${info.path} mode=${info.permissionMode}`);
      });
    }).catch((err: BusinessError) => {
      console.error(`getSharedDirectoryInfo err: ${JSON.stringify(err)}`);
    });
  } catch (error) {
    console.error(`getSharedDirectoryInfo error, Code: ${error.code}, message: ${error.message}`);
  }
}
```
