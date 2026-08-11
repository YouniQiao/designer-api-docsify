# getCachedGnssLocationsSize

## Modules to Import

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## getCachedGnssLocationsSize

```TypeScript
function getCachedGnssLocationsSize(callback: AsyncCallback<number>): void
```

Obtain the number of cached GNSS locations reported at a time

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.geoLocationManager/geoLocationManager.getCachedGnssLocationsSize

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function getCachedGnssLocationsSize(callback: AsyncCallback<number>): void--><!--Device-geolocation-function getCachedGnssLocationsSize(callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.getCachedGnssLocationsSize((err, size) => {
    if (err) {
        console.info('getCachedGnssLocationsSize: err=' + JSON.stringify(err));
    }
    if (size) {
        console.info('getCachedGnssLocationsSize: size=' + JSON.stringify(size));
    }
});
```


## getCachedGnssLocationsSize

```TypeScript
function getCachedGnssLocationsSize(): Promise<number>
```

Obtain the number of cached GNSS locations reported at a time

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.geoLocationManager/geoLocationManager.getCachedGnssLocationsSize

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function getCachedGnssLocationsSize(): Promise<number>--><!--Device-geolocation-function getCachedGnssLocationsSize(): Promise<number>-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.getCachedGnssLocationsSize().then((result) => {
    console.info('promise, getCachedGnssLocationsSize: ' + JSON.stringify(result));
});
```
