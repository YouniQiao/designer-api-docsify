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

**Deprecated since:** -1

**Required permissions:** ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function offCachedGnssLocationsChange(callback?: Callback<Array<Location>>): void--><!--Device-geoLocationManager-function offCachedGnssLocationsChange(callback?: Callback<Array<Location>>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;Location&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) |
