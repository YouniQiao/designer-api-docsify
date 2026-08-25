# disableReverseGeocodingMock (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## disableReverseGeocodingMock

```TypeScript
function disableReverseGeocodingMock(): void
```

Disable the reverse geocoding simulation function.

**Since:** 9

**Required permissions:** 
- API version 20+: ohos.permission.MOCK_LOCATION

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [201](../../errorcode-universal.md#201-permission-denied) |
