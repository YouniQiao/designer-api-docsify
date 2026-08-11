# enableLocationMock (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## enableLocationMock

```TypeScript
function enableLocationMock(): void
```

Enable the geographical location simulation function.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 20+: ohos.permission.MOCK_LOCATION

<!--Device-geoLocationManager-function enableLocationMock(): void--><!--Device-geoLocationManager-function enableLocationMock(): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call \\${geoLocationManager.enableLocationMock} due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 20 and later |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) | The location switch is off. |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  geoLocationManager.enableLocationMock();
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

