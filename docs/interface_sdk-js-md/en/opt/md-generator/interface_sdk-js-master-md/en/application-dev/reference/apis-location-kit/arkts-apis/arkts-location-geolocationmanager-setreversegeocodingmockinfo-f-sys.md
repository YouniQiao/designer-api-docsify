# setReverseGeocodingMockInfo (System API)

## Modules to Import

```TypeScript
```

## setReverseGeocodingMockInfo

```TypeScript
function setReverseGeocodingMockInfo(mockInfos: Array<ReverseGeocodingMockInfo>): void
```

Set the configuration parameters for simulating reverse geocoding.

**Since:** 23

**Required permissions:** 
- API version 20+: ohos.permission.MOCK_LOCATION

<!--Device-geoLocationManager-function setReverseGeocodingMockInfo(mockInfos: Array<ReverseGeocodingMockInfo>): void--><!--Device-geoLocationManager-function setReverseGeocodingMockInfo(mockInfos: Array<ReverseGeocodingMockInfo>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mockInfos | Array&lt;[ReverseGeocodingMockInfo](arkts-location-geolocationmanager-reversegeocodingmockinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

**Examples**

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

let mockInfos: Array<geoLocationManager.ReverseGeocodingMockInfo> = [
  {
    "location": {
      "locale": "zh",
      "latitude": 30.12,
      "longitude": 120.11,
      "maxItems": 1
    },
    "geoAddress": {
      "locale": "zh",
      "latitude": 30.12,
      "longitude": 120.11,
      "isFromMock": true
    }
  },
  {
    "location": {
      "locale": "zh",
      "latitude": 31.12,
      "longitude": 121.11,
      "maxItems": 1
    },
    "geoAddress": {
      "locale": "zh",
      "latitude": 31.12,
      "longitude": 121.11,
      "isFromMock": true
    }
  },
  {
    "location": {
      "locale": "zh",
      "latitude": 32.12,
      "longitude": 122.11,
      "maxItems": 1
    },
    "geoAddress": {
      "locale": "zh",
      "latitude": 32.12,
      "longitude": 122.11,
      "isFromMock": true
    }
  },
  {
    "location": {
      "locale": "zh",
      "latitude": 33.12,
      "longitude": 123.11,
      "maxItems": 1
    },
    "geoAddress": {
      "locale": "zh",
      "latitude": 33.12,
      "longitude": 123.11,
      "isFromMock": true
    }
  },
  {
    "location": {
      "locale": "zh",
      "latitude": 34.12,
      "longitude": 124.11,
      "maxItems": 1
    },
    "geoAddress": {
      "locale": "zh",
      "latitude": 34.12,
      "longitude": 124.11,
      "isFromMock": true
    }
  },
];
try {
  geoLocationManager.enableReverseGeocodingMock();
  geoLocationManager.setReverseGeocodingMockInfo(mockInfos);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
