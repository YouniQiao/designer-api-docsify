# addFusionFence (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## addFusionFence

```TypeScript
function addFusionFence(fenceRequestParams: FusionFenceRequestParams): Promise<void>
```

Add a fusion fence.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 26.1.0.

**Required permissions:** ohos.permission.LOCATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-geoLocationManager-function addFusionFence(fenceRequestParams: FusionFenceRequestParams): Promise<void>--><!--Device-geoLocationManager-function addFusionFence(fenceRequestParams: FusionFenceRequestParams): Promise<void>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fenceRequestParams | [FusionFenceRequestParams](arkts-location-geolocationmanager-fusionfencerequestparams-i-sys.md) | Yes | Indicates the fusion fence request parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.addFusionFence} due to limited device. |
| 3301601 | The number of geofences exceeds the maximum. |
| 3501603 | Duplicate fusion fence identifier. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

