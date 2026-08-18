# getLastLocation

## Modules to Import

```TypeScript
```

## getLastLocation

```TypeScript
function getLastLocation(callback: AsyncCallback<Location>): void
```

Obtain last known location

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getLastLocation](arkts-location-geolocationmanager-getlastlocation-f.md#getlastlocation)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function getLastLocation(callback: AsyncCallback<Location>): void--><!--Device-geolocation-function getLastLocation(callback: AsyncCallback<Location>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Location&gt; | Yes |

**Examples**

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.getLastLocation((err, data) => {
    if (err) {
        console.info('getLastLocation: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('getLastLocation: data=' + JSON.stringify(data));
    }
});
```


## getLastLocation

```TypeScript
function getLastLocation(): Promise<Location>
```

Obtain last known location

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getLastLocation](arkts-location-geolocationmanager-getlastlocation-f.md#getlastlocation)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function getLastLocation(): Promise<Location>--><!--Device-geolocation-function getLastLocation(): Promise<Location>-End-->

**System capability:** SystemCapability.Location.Location.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Location & gt; |

**Examples**

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.getLastLocation().then((result) => {
    console.info('getLastLocation: result: ' + JSON.stringify(result));
});
```
