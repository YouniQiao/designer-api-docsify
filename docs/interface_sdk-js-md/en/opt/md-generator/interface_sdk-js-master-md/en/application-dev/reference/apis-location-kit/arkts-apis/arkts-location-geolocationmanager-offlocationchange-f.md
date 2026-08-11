# offLocationChange

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## offLocationChange

```TypeScript
function offLocationChange(callback?: Callback<Location>): void
```

Unsubscribe location changed.

**Since:** 26.0.0

**Required permissions:** 
- API version 23 - 24: ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function offLocationChange(callback?: Callback<Location>): void--><!--Device-geoLocationManager-function offLocationChange(callback?: Callback<Location>): void-End-->

**System capability:** 
- API version 23 and later: SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
