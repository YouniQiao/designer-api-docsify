# getAllVolumes (System API)

## Modules to Import

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## getAllVolumes

```TypeScript
function getAllVolumes(callback: AsyncCallback<Array<Volume>>): void
```

Obtains information about all volumes of this external storage device. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-volumeManager-function getAllVolumes(callback: AsyncCallback<Array<Volume>>): void--><!--Device-volumeManager-function getAllVolumes(callback: AsyncCallback<Array<Volume>>): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Volume](arkts-corefile-volumemanager-volume-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900042 |


## getAllVolumes

```TypeScript
function getAllVolumes(): Promise<Array<Volume>>
```

Obtains information about all volumes of this external storage device. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-volumeManager-function getAllVolumes(): Promise<Array<Volume>>--><!--Device-volumeManager-function getAllVolumes(): Promise<Array<Volume>>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Volume](arkts-corefile-volumemanager-volume-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900042 |
