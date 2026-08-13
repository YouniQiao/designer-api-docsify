# getCurrentLocation

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## getCurrentLocation

```TypeScript
function getCurrentLocation(request: CurrentLocationRequest, callback: AsyncCallback<Location>): void
```

Obtain current location

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md#getCurrentLocation)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function getCurrentLocation(request: CurrentLocationRequest, callback: AsyncCallback<Location>): void--><!--Device-geolocation-function getCurrentLocation(request: CurrentLocationRequest, callback: AsyncCallback<Location>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [CurrentLocationRequest](arkts-location-geolocationmanager-currentlocationrequest-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Location&gt; | Yes |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
import BusinessError from "@ohos.base"
let requestInfo:geolocation.CurrentLocationRequest = {'priority': 0x203, 'scenario': 0x300,'maxAccuracy': 0};
let locationChange = (err:BusinessError.BusinessError, location:geolocation.Location) => {
    if (err) {
        console.info('locationChanger: err=' + JSON.stringify(err));
    }
    if (location) {
        console.info('locationChanger: location=' + JSON.stringify(location));
    }
};
geolocation.getCurrentLocation(requestInfo, locationChange);
```


## getCurrentLocation

```TypeScript
function getCurrentLocation(callback: AsyncCallback<Location>): void
```

Obtain current location

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md#getCurrentLocation)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function getCurrentLocation(callback: AsyncCallback<Location>): void--><!--Device-geolocation-function getCurrentLocation(callback: AsyncCallback<Location>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Location&gt; | Yes |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
import BusinessError from "@ohos.base"
let locationChange = (err:BusinessError.BusinessError, location:geolocation.Location):void => {
    if (err) {
        console.info('locationChanger: err=' + JSON.stringify(err));
    }
    if (location) {
        console.info('locationChanger: location=' + JSON.stringify(location));
    }
};
geolocation.getCurrentLocation(locationChange);
```


## getCurrentLocation

```TypeScript
function getCurrentLocation(request?: CurrentLocationRequest): Promise<Location>
```

Obtain current location

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getCurrentLocation](arkts-location-geolocationmanager-getcurrentlocation-f.md#getCurrentLocation)

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function getCurrentLocation(request?: CurrentLocationRequest): Promise<Location>--><!--Device-geolocation-function getCurrentLocation(request?: CurrentLocationRequest): Promise<Location>-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [CurrentLocationRequest](arkts-location-geolocationmanager-currentlocationrequest-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Location & gt; |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.CurrentLocationRequest = {'priority': 0x203, 'scenario': 0x300,'maxAccuracy': 0};
geolocation.getCurrentLocation(requestInfo).then((result) => {
    console.info('current location: ' + JSON.stringify(result));
});
```
