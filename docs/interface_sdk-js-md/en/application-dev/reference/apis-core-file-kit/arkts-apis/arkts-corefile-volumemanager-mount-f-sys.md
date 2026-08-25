# mount (System API)

## Modules to Import

```TypeScript
import { volumeManager } from 'kits/@kit.CoreFileKit';
```

## mount

```TypeScript
function mount(volumeId: string, callback: AsyncCallback<void>): void
```

Mounts a volume. This API uses an asynchronous callback to return the result. Currently, only the FAT, exFAT, ext4 and NTFS file systems are supported.

**Since:** 9

**Required permissions:** ohos.permission.MOUNT_UNMOUNT_MANAGER

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600001 |
| 13600002 |
| 13600003 |
| 13600005 |
| 13600008 |
| 13900042 |


## mount

```TypeScript
function mount(volumeId: string): Promise<void>
```

Mounts a volume. This API uses a promise to return the result. Currently, only the FAT, exFAT, ext4 and NTFS file systems are supported.

**Since:** 9

**Required permissions:** ohos.permission.MOUNT_UNMOUNT_MANAGER

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600001 |
| 13600002 |
| 13600003 |
| 13600005 |
| 13600008 |
| 13900042 |
