# partition (System API)

## Modules to Import

```TypeScript
import { volumeManager } from 'kits/@kit.CoreFileKit';
```

## partition

```TypeScript
function partition(diskId: string, type: int, callback: AsyncCallback<void>): void
```

Partitions a disk. This API uses an asynchronous callback to return the result. The system supports access to multi-partition disks. Currently, this API can partition a disk into only one partition.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

<!--Device-volumeManager-function partition(diskId: string, type: int, callback: AsyncCallback<void>): void--><!--Device-volumeManager-function partition(diskId: string, type: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| diskId | string | Yes | ID of the disk to partition. |
| type | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Partition type. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The input parameter is invalid.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 13600008 | No such object. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |


## partition

```TypeScript
function partition(diskId: string, type: int): Promise<void>
```

Partitions a disk. This API uses a promise to return the result. The system supports access to multi-partition disks. Currently, this API can partition a disk into only one partition.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

<!--Device-volumeManager-function partition(diskId: string, type: int): Promise<void>--><!--Device-volumeManager-function partition(diskId: string, type: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| diskId | string | Yes | ID of the disk to partition. |
| type | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Partition type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The input parameter is invalid.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 13600008 | No such object. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

