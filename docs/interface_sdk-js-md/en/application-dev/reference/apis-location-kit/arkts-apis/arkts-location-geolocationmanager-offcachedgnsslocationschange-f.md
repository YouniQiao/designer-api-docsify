# offCachedGnssLocationsChange

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## offCachedGnssLocationsChange

```TypeScript
function offCachedGnssLocationsChange(callback?: Callback<Array<Location>>): void
```

Unsubscribe to cache GNSS locations update messages.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function offCachedGnssLocationsChange(callback?: Callback<Array<Location>>): void--><!--Device-geoLocationManager-function offCachedGnssLocationsChange(callback?: Callback<Array<Location>>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;Location&gt;&gt; | No | Indicates the callback for reporting the cached gnss locations. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${geoLocationManager.offCachedGnssLocationsChange} due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) | The location switch is off. |

