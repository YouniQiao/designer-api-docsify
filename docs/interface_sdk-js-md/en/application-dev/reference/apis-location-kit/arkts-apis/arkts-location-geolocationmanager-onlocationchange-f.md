# onLocationChange

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## onLocationChange

```TypeScript
function onLocationChange(request: LocationRequest | ContinuousLocationRequest,
  callback: Callback<Location>): void
```

Subscribe location changed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 23+: ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function onLocationChange(request: LocationRequest | ContinuousLocationRequest,  callback: Callback<Location>): void--><!--Device-geoLocationManager-function onLocationChange(request: LocationRequest | ContinuousLocationRequest,  callback: Callback<Location>): void-End-->

**System capability:** 
- API version 23 and later: SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [LocationRequest](arkts-location-geolocationmanager-locationrequest-i.md) \| ContinuousLocationRequest | Yes | Indicates the location request parameters.<br>**Since:** 23 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | Yes | Indicates the callback for reporting the location result.<br>**Since:** 23 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.<br>**Applicable version:** 23 and later |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.onLocationChange} due to limited device capabilities.<br>**Applicable version:** 23 and later |
| 201 | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 23 and later |
| 3301000 | The location service is unavailable.<br>**Applicable version:** 23 and later |
| 3301100 | The location switch is off.<br>**Applicable version:** 23 and later |

