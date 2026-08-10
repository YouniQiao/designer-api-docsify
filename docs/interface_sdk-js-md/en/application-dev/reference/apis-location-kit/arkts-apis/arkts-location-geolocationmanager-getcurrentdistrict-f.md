# getCurrentDistrict

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getCurrentDistrict

```TypeScript
function getCurrentDistrict(params?: DistrictRequestParams): Promise<DistrictInfo>
```

Obtains the information about the district where the current device is located.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 26.1.0.

**Required permissions:** ohos.permission.APPROXIMATELY_LOCATION

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-geoLocationManager-function getCurrentDistrict(params?: DistrictRequestParams): Promise<DistrictInfo>--><!--Device-geoLocationManager-function getCurrentDistrict(params?: DistrictRequestParams): Promise<DistrictInfo>-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [DistrictRequestParams](arkts-location-geolocationmanager-districtrequestparams-i.md) | No | Indicates request parameters for obtaining the district information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DistrictInfo&gt; | Promise used to return \\${DistrictInfo}. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.getCurrentDistrict} due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301500 | Failed to query the area information because the reverse geocoding server returns an error. |

