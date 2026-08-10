# isGeoServiceAvailable

## Modules to Import

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## isGeoServiceAvailable

```TypeScript
function isGeoServiceAvailable(callback: AsyncCallback<boolean>): void
```

Obtain geocode service status

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.geoLocationManager/geoLocationManager.isGeocoderAvailable

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function isGeoServiceAvailable(callback: AsyncCallback<boolean>): void--><!--Device-geolocation-function isGeoServiceAvailable(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Indicates the callback for reporting the geocode service status. |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.isGeoServiceAvailable((err, data) => {
    if (err) {
        console.info('isGeoServiceAvailable: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('isGeoServiceAvailable: data=' + JSON.stringify(data));
    }
});
```


## isGeoServiceAvailable

```TypeScript
function isGeoServiceAvailable(): Promise<boolean>
```

Obtain geocode service status

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.geoLocationManager/geoLocationManager.isGeocoderAvailable

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function isGeoServiceAvailable(): Promise<boolean>--><!--Device-geolocation-function isGeoServiceAvailable(): Promise<boolean>-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | The promise returned by the function. |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.isGeoServiceAvailable().then((result) => {
    console.info('promise, isGeoServiceAvailable: ' + JSON.stringify(result));
});
```

