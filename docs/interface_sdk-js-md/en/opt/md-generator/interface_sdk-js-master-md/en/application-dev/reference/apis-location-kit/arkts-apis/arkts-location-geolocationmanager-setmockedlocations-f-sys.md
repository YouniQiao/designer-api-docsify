# setMockedLocations (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## setMockedLocations

```TypeScript
function setMockedLocations(config: LocationMockConfig): void
```

Set the configuration parameters for location simulation.

**Since:** 9

**Required permissions:** 
- API version 20+: ohos.permission.MOCK_LOCATION

<!--Device-geoLocationManager-function setMockedLocations(config: LocationMockConfig): void--><!--Device-geoLocationManager-function setMockedLocations(config: LocationMockConfig): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [LocationMockConfig](arkts-location-geolocationmanager-locationmockconfig-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

let locations: Array<geoLocationManager.Location> = [
  {
    "latitude": 30.12,
    "longitude": 120.11,
    "altitude": 123,
    "accuracy": 1,
    "speed": 5.2,
    "timeStamp": 16594326109,
    "direction": 123.11,
    "timeSinceBoot": 1000000000,
    "additionSize": 0,
    "isFromMock": true
  },
  {
    "latitude": 31.13,
    "longitude": 121.11,
    "altitude": 123,
    "accuracy": 2,
    "speed": 5.2,
    "timeStamp": 16594326109,
    "direction": 123.11,
    "timeSinceBoot": 2000000000,
    "additionSize": 0,
    "isFromMock": true
  },
  {
    "latitude": 32.14,
    "longitude": 122.11,
    "altitude": 123,
    "accuracy": 3,
    "speed": 5.2,
    "timeStamp": 16594326109,
    "direction": 123.11,
    "timeSinceBoot": 3000000000,
    "additionSize": 0,
    "isFromMock": true
  },
  {
    "latitude": 33.15,
    "longitude": 123.11,
    "altitude": 123,
    "accuracy": 4,
    "speed": 5.2,
    "timeStamp": 16594326109,
    "direction": 123.11,
    "timeSinceBoot": 4000000000,
    "additionSize": 0,
    "isFromMock": true
  },
  {
    "latitude": 34.16,
    "longitude": 124.11,
    "altitude": 123,
    "accuracy": 5,
    "speed": 5.2,
    "timeStamp": 16594326109,
    "direction": 123.11,
    "timeSinceBoot": 5000000000,
    "additionSize": 0,
    "isFromMock": true
  }
];
let config: geoLocationManager.LocationMockConfig = { "timeInterval": 5, "locations": locations };
try {
  geoLocationManager.enableLocationMock();
  geoLocationManager.setMockedLocations(config);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
