# enableReverseGeocodingMock (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## enableReverseGeocodingMock

```TypeScript
function enableReverseGeocodingMock(): void
```

Enable the reverse geocoding simulation function.

**Since:** 9

**Required permissions:** 
- API version 20+: ohos.permission.MOCK_LOCATION

<!--Device-geoLocationManager-function enableReverseGeocodingMock(): void--><!--Device-geoLocationManager-function enableReverseGeocodingMock(): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  geoLocationManager.enableReverseGeocodingMock();
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
