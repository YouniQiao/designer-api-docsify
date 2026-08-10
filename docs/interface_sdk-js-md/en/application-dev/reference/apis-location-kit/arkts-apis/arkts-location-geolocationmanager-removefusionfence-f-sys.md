# removeFusionFence (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## removeFusionFence

```TypeScript
function removeFusionFence(identifier: string): Promise<void>
```

Remove a fusion fence.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-geoLocationManager-function removeFusionFence(identifier: string): Promise<void>--><!--Device-geoLocationManager-function removeFusionFence(identifier: string): Promise<void>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| identifier | string | Yes | Indicates identifier of the fusion fence. The string format should be a valid unique identifier (e.g., GUID or specific alphanumeric pattern). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 3301602 | Failed to delete a fusion fence due to an incorrect identifier. |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.removeFusionFence} due to limited device. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 3301000 | The location service is unavailable. |

