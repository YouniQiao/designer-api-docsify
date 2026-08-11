# getFreeSizeOfVolume (System API)

## Modules to Import

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## getFreeSizeOfVolume

```TypeScript
function getFreeSizeOfVolume(volumeUuid: string, callback: AsyncCallback<number>): void
```

Get the free size of volume.

**Since:** 8

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getFreeSizeOfVolume(volumeUuid: string, callback: AsyncCallback<long>): void--><!--Device-storageStatistics-function getFreeSizeOfVolume(volumeUuid: string, callback: AsyncCallback<long>): void-End-->

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
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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
  storageStatistics.getFreeSizeOfVolume(uuid, (error: BusinessError, number: number) => {
    if (error) {
      console.error("getFreeSizeOfVolume failed with error:" + JSON.stringify(error));
    } else {
      // Do something.
      console.info("getFreeSizeOfVolume successfully: " + number);
    }
  });
}).catch((err: BusinessError) => {
  console.error("getAllVolumes failed with error:" + JSON.stringify(err));
});
```


## getFreeSizeOfVolume

```TypeScript
function getFreeSizeOfVolume(volumeUuid: string): Promise<number>
```

Get the free size of volume.

**Since:** 8

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getFreeSizeOfVolume(volumeUuid: string): Promise<long>--><!--Device-storageStatistics-function getFreeSizeOfVolume(volumeUuid: string): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeUuid | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
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
  storageStatistics.getFreeSizeOfVolume(uuid).then((number: number) => {
    console.info("getFreeSizeOfVolume successfully:" + number);
  }).catch((err: BusinessError) => {
    console.error("getFreeSizeOfVolume failed with error:" + JSON.stringify(err));
  });
}).catch((err: BusinessError) => {
  console.error("getAllVolumes failed with error:" + JSON.stringify(err));
});
```
