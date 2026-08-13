# unmount (System API)

## Modules to Import

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
```

## unmount

```TypeScript
function unmount(volumeId: string, callback: AsyncCallback<void>): void
```

Unmounts a volume. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MOUNT_UNMOUNT_MANAGER

<!--Device-volumeManager-function unmount(volumeId: string, callback: AsyncCallback<void>): void--><!--Device-volumeManager-function unmount(volumeId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600008 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600005 |
| 13600004 |
| 13600002 |
| 13600001 |
| 13900042 |


## unmount

```TypeScript
function unmount(volumeId: string): Promise<void>
```

Unmounts a volume. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MOUNT_UNMOUNT_MANAGER

<!--Device-volumeManager-function unmount(volumeId: string): Promise<void>--><!--Device-volumeManager-function unmount(volumeId: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600008 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600005 |
| 13600004 |
| 13600002 |
| 13600001 |
| 13900042 |
