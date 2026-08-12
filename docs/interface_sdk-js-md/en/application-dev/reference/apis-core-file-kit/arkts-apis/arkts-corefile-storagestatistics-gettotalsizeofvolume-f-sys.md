# getTotalSizeOfVolume (System API)

## Modules to Import

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
```

## getTotalSizeOfVolume

```TypeScript
function getTotalSizeOfVolume(volumeUuid: string, callback: AsyncCallback<long>): void
```

Get the total size of volume.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getTotalSizeOfVolume(volumeUuid: string, callback: AsyncCallback<long>): void--><!--Device-storageStatistics-function getTotalSizeOfVolume(volumeUuid: string, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeUuid | string | Yes | The uuid of the volume |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;long&gt; | Yes | callback &lt;br&gt;Unit: Byte. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 13600008 | No such object. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

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
function getTotalSizeOfVolume(volumeUuid: string): Promise<long>
```

Get the total size of volume.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getTotalSizeOfVolume(volumeUuid: string): Promise<long>--><!--Device-storageStatistics-function getTotalSizeOfVolume(volumeUuid: string): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeUuid | string | Yes | The uuid of the volume |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | return Promise (Unit: Byte) |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 13600008 | No such object. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

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

