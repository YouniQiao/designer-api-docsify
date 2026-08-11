# disableLocationMock (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## disableLocationMock

```TypeScript
function disableLocationMock(): void
```

Disable the geographical location simulation function.

**Since:** 9

**Required permissions:** 
- API version 20+: ohos.permission.MOCK_LOCATION

<!--Device-geoLocationManager-function disableLocationMock(): void--><!--Device-geoLocationManager-function disableLocationMock(): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  geoLocationManager.disableLocationMock();
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
