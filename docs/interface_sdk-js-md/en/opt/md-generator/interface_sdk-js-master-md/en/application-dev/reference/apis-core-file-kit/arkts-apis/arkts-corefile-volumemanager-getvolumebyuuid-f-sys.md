# getVolumeByUuid (System API)

## Modules to Import

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## getVolumeByUuid

```TypeScript
function getVolumeByUuid(uuid: string, callback: AsyncCallback<Volume>): void
```

Obtains information about a volume based on the UUID. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-volumeManager-function getVolumeByUuid(uuid: string, callback: AsyncCallback<Volume>): void--><!--Device-volumeManager-function getVolumeByUuid(uuid: string, callback: AsyncCallback<Volume>): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uuid | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Volume](arkts-corefile-volumemanager-volume-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600008 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900042 |


## getVolumeByUuid

```TypeScript
function getVolumeByUuid(uuid: string): Promise<Volume>
```

Obtains information about a volume based on the universally unique identifier (UUID). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-volumeManager-function getVolumeByUuid(uuid: string): Promise<Volume>--><!--Device-volumeManager-function getVolumeByUuid(uuid: string): Promise<Volume>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uuid | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Volume](arkts-corefile-volumemanager-volume-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600008 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900042 |
