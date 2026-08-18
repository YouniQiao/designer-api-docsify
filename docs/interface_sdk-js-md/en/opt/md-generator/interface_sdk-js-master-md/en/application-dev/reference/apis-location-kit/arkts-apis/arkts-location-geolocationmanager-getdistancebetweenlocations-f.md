# getDistanceBetweenLocations

## Modules to Import

```TypeScript
```

## getDistanceBetweenLocations

```TypeScript
function getDistanceBetweenLocations(location1: Location, location2: Location): number
```

Obtains the distance between two locations.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-geoLocationManager-function getDistanceBetweenLocations(location1: Location, location2: Location): double--><!--Device-geoLocationManager-function getDistanceBetweenLocations(location1: Location, location2: Location): double-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| location1 | [Location](arkts-location-geolocationmanager-location-i.md) | Yes |
| location2 | [Location](arkts-location-geolocationmanager-location-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let location1: geoLocationManager.Location = {
    "latitude": 30.12,
    "longitude": 120.11,
    "altitude": 0,
    "accuracy": 0,
    "speed": 0,
    "timeStamp": 0,
    "direction": 0,
    "timeSinceBoot": 0,
    "additionSize": 0
  }
  let location2: geoLocationManager.Location = {
    "latitude": 30.12,
    "longitude": 120.11,
    "altitude": 0,
    "accuracy": 0,
    "speed": 0,
    "timeStamp": 0,
    "direction": 0,
    "timeSinceBoot": 0,
    "additionSize": 0
  }
  let distance = geoLocationManager.getDistanceBetweenLocations(location1, location2);
  console.info("distance:" + distance);
} catch (error) {
  console.error("getDistanceBetweenLocations: errCode" + error.code + ", errMessage" + error.message);
}
```
