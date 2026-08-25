# partition (System API)

## Modules to Import

```TypeScript
import { volumeManager } from 'kits/@kit.CoreFileKit';
```

## partition

```TypeScript
function partition(diskId: string, type: number, callback: AsyncCallback<void>): void
```

Partitions a disk. This API uses an asynchronous callback to return the result. The system supports access to multi-partition disks. Currently, this API can partition a disk into only one partition.

**Since:** 9

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| diskId | string | Yes |
| type | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600001 |
| 13600008 |
| 13900042 |


## partition

```TypeScript
function partition(diskId: string, type: number): Promise<void>
```

Partitions a disk. This API uses a promise to return the result. The system supports access to multi-partition disks. Currently, this API can partition a disk into only one partition.

**Since:** 9

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| diskId | string | Yes |
| type | number | Yes |

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
| 13600008 |
| 13900042 |
