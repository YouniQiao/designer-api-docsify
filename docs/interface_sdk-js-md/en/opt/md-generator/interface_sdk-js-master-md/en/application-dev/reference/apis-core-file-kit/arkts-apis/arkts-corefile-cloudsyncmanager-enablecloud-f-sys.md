# enableCloud (System API)

## Modules to Import

```TypeScript
import { cloudSyncManager } from '@kit.CoreFileKit';
```

## enableCloud

```TypeScript
function enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>
```

Enables device-cloud sync. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-cloudSyncManager-function enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>--><!--Device-cloudSyncManager-function enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| switches | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountId: string = "testAccount";
let switches: Record<string, boolean> = {
  'com.example.bundleName1': true,
  'com.example.bundleName2': false
}
cloudSyncManager.enableCloud(accountId, switches).then(() => {
  console.info("enableCloud successfully.");
}).catch((err: BusinessError) => {
  console.error("enableCloud failed with error message: " + err.message + ", error code: " + err.code);
});
```


## enableCloud

```TypeScript
function enableCloud(
    accountId: string,
    switches: Record<string, boolean>,
    callback: AsyncCallback<void>
  ): void
```

Enables device-cloud sync. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.CLOUDFILE_SYNC_MANAGER

<!--Device-cloudSyncManager-function enableCloud(    accountId: string,    switches: Record<string, boolean>,    callback: AsyncCallback<void>  ): void--><!--Device-cloudSyncManager-function enableCloud(    accountId: string,    switches: Record<string, boolean>,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| switches | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, boolean&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountId: string = "testAccount";
let switches: Record<string, boolean> = {
  'com.example.bundleName1': true,
  'com.example.bundleName2': false
}
cloudSyncManager.enableCloud(accountId, switches, (err: BusinessError) => {
  if (err) {
    console.error("enableCloud failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("enableCloud successfully");
  }
});
```
