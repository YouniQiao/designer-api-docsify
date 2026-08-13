# getTotalSizeOfVolume (System API)

## Modules to Import

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
```

## getTotalSizeOfVolume

```TypeScript
function getTotalSizeOfVolume(volumeUuid: string, callback: AsyncCallback<number>): void
```

Get the total size of volume.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getTotalSizeOfVolume(volumeUuid: string, callback: AsyncCallback<long>): void--><!--Device-storageStatistics-function getTotalSizeOfVolume(volumeUuid: string, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeUuid | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600008 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900042 |

## Examples

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

volumeManager.getAllVolumes().then((volumes: Array<volumeManager.Volume>) => {
  if (volumes == null || volumes.length <= 0) {
    console.error("volumes is null or length is invalid");
    return;
  }
  let uuid: string = volumes[0].uuid;
  storageStatistics.getTotalSizeOfVolume(uuid, (error: BusinessError, number: number) => {
    if (error) {
      console.error("getTotalSizeOfVolume failed with error:" + JSON.stringify(error));
    } else {
      // Do something.
      console.info("getTotalSizeOfVolume successfully:" + number);
    }
  });
}).catch((err: BusinessError) => {
  console.error("getAllVolumes failed with error:" + JSON.stringify(err));
});
```


## getTotalSizeOfVolume

```TypeScript
function getTotalSizeOfVolume(volumeUuid: string): Promise<number>
```

Get the total size of volume.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getTotalSizeOfVolume(volumeUuid: string): Promise<long>--><!--Device-storageStatistics-function getTotalSizeOfVolume(volumeUuid: string): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeUuid | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600008 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900042 |

## Examples

```TypeScript
import { volumeManager } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

volumeManager.getAllVolumes().then((volumes: Array<volumeManager.Volume>) => {
  if (volumes == null || volumes.length <= 0) {
    console.error("volumes is null or length is invalid");
    return;
  }
  let uuid: string = volumes[0].uuid;
  storageStatistics.getTotalSizeOfVolume(uuid).then((number: number) => {
    console.info("getTotalSizeOfVolume successfully:" + number);
  }).catch((err: BusinessError) => {
    console.error("getTotalSizeOfVolume failed with error:" + JSON.stringify(err));
  });
}).catch((err: BusinessError) => {
  console.error("getAllVolumes failed with error:" + JSON.stringify(err));
});
```
