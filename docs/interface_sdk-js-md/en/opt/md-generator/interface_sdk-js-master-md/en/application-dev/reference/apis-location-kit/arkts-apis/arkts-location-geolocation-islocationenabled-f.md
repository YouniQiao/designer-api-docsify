# isLocationEnabled

## Modules to Import

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## isLocationEnabled

```TypeScript
function isLocationEnabled(callback: AsyncCallback<boolean>): void
```

Obtain current location switch status

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.geoLocationManager/geoLocationManager.isLocationEnabled

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function isLocationEnabled(callback: AsyncCallback<boolean>): void--><!--Device-geolocation-function isLocationEnabled(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.isLocationEnabled((err, data) => {
    if (err) {
        console.info('isLocationEnabled: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('isLocationEnabled: data=' + JSON.stringify(data));
    }
});
```


## isLocationEnabled

```TypeScript
function isLocationEnabled(): Promise<boolean>
```

Obtain current location switch status

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.geoLocationManager/geoLocationManager.isLocationEnabled

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function isLocationEnabled(): Promise<boolean>--><!--Device-geolocation-function isLocationEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.Location.Location.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.isLocationEnabled().then((result) => {
    console.info('promise, isLocationEnabled: ' + JSON.stringify(result));
});
```
