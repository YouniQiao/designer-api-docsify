# getLastLocation

## Modules to Import

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## getLastLocation

```TypeScript
function getLastLocation(callback: AsyncCallback<Location>): void
```

Obtain last known location

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getLastLocation](arkts-location-geolocationmanager-getlastlocation-f.md)

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Location&gt; | Yes |


## getLastLocation

```TypeScript
function getLastLocation(): Promise<Location>
```

Obtain last known location

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getLastLocation](arkts-location-geolocationmanager-getlastlocation-f.md)

**Required permissions:** ohos.permission.LOCATION

**System capability:** SystemCapability.Location.Location.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Location & gt; |
