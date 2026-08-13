# onLocationChange

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## onLocationChange

```TypeScript
function onLocationChange(request: LocationRequest | ContinuousLocationRequest,
  callback: Callback<Location>): void
```

Subscribe location changed.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** 
- API version 23+: ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function onLocationChange(request: LocationRequest | ContinuousLocationRequest,  callback: Callback<Location>): void--><!--Device-geoLocationManager-function onLocationChange(request: LocationRequest | ContinuousLocationRequest,  callback: Callback<Location>): void-End-->

**System capability:** 
- API version 23 and later: SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | LocationRequest \| [ContinuousLocationRequest](arkts-location-geolocationmanager-continuouslocationrequest-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) |
