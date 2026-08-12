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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-volumeManager-function getVolumeByUuid(uuid: string, callback: AsyncCallback<Volume>): void--><!--Device-volumeManager-function getVolumeByUuid(uuid: string, callback: AsyncCallback<Volume>): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | string | Yes | UUID of the volume. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[Volume](arkts-corefile-volumemanager-volume-i-sys.md)&gt; | Yes | Callback used to return the volume information obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The input parameter is invalid.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 13600008 | No such object. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |


## getVolumeByUuid

```TypeScript
function getVolumeByUuid(uuid: string): Promise<Volume>
```

Obtains information about a volume based on the universally unique identifier (UUID). This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-volumeManager-function getVolumeByUuid(uuid: string): Promise<Volume>--><!--Device-volumeManager-function getVolumeByUuid(uuid: string): Promise<Volume>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uuid | string | Yes | UUID of the volume. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Volume](arkts-corefile-volumemanager-volume-i-sys.md)&gt; | Promise used to return the volume information of the current UUID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The input parameter is invalid.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 13600008 | No such object. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

