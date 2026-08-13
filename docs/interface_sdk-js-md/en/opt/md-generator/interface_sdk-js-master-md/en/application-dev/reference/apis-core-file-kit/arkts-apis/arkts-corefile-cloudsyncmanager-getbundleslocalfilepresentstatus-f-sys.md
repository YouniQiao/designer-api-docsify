# getBundlesLocalFilePresentStatus (System API)

## Modules to Import

```TypeScript
import { cloudSyncManager } from '@kit.CoreFileKit';
```

## getBundlesLocalFilePresentStatus

```TypeScript
function getBundlesLocalFilePresentStatus(bundleNames: Array<string>): Promise<Array<LocalFilePresentStatus>>
```

Obtains the existence status of local files for multiple applications and checks whether there are files that have not been uploaded to the cloud in the cloud storage space. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-cloudSyncManager-function getBundlesLocalFilePresentStatus(bundleNames: Array<string>): Promise<Array<LocalFilePresentStatus>>--><!--Device-cloudSyncManager-function getBundlesLocalFilePresentStatus(bundleNames: Array<string>): Promise<Array<LocalFilePresentStatus>>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleNames | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[LocalFilePresentStatus](arkts-corefile-cloudsyncmanager-localfilepresentstatus-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 22400005 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900010 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundles: Array<string> = ['com.example.app1', 'com.example.app2'];
cloudSyncManager.getBundlesLocalFilePresentStatus(bundles).then((results: Array<cloudSyncManager.LocalFilePresentStatus>) => {
  results.forEach((item) => {
    console.info(`bundle: ${item.bundleName}, hasLocalUncloudedFiles: ${item.isLocalFilePresent}`);
  });
}).catch((err: BusinessError) => {
  console.error(`getBundlesLocalFilePresentStatus failed, code: ${err.code}, message: ${err.message}`);
});
```
