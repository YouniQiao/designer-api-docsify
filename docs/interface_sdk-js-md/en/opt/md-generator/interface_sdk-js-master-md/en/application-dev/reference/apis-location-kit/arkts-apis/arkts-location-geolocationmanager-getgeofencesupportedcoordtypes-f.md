# getGeofenceSupportedCoordTypes

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getGeofenceSupportedCoordTypes

```TypeScript
function getGeofenceSupportedCoordTypes(): Array<CoordinateSystemType>
```

Obtains the coordinate system types supported by geofence.

**Since:** 12

<!--Device-geoLocationManager-function getGeofenceSupportedCoordTypes(): Array<CoordinateSystemType>--><!--Device-geoLocationManager-function getGeofenceSupportedCoordTypes(): Array<CoordinateSystemType>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;CoordinateSystemType&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let supportedCoordTypes: Array<geoLocationManager.CoordinateSystemType> = geoLocationManager.getGeofenceSupportedCoordTypes();
  console.info("getGeofenceSupportedCoordTypes return:" + JSON.stringify(supportedCoordTypes));
} catch (error) {
  console.error("getGeofenceSupportedCoordTypes: error=" + JSON.stringify(error));
}
```
