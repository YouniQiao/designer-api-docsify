# flushCachedGnssLocations

## Modules to Import

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## flushCachedGnssLocations

```TypeScript
function flushCachedGnssLocations(callback: AsyncCallback<boolean>): void
```

All prepared GNSS locations are returned to the application through the callback function, and the bottom-layer buffer is cleared.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [flushCachedGnssLocations](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md)

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |


## flushCachedGnssLocations

```TypeScript
function flushCachedGnssLocations(): Promise<boolean>
```

All prepared GNSS locations are returned to the application through the callback function, and the bottom-layer buffer is cleared.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [flushCachedGnssLocations](arkts-location-geolocationmanager-flushcachedgnsslocations-f.md)

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Gnss

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |
