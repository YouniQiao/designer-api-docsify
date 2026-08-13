# getAddressesFromLocationName

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## getAddressesFromLocationName

```TypeScript
function getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void
```

Obtain latitude and longitude info from location address.

**Since:** 23

**Deprecated since:** -1

<!--Device-geoLocationManager-function getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void--><!--Device-geoLocationManager-function getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [GeoCodeRequest](arkts-location-geolocation-geocoderequest-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;GeoAddress&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [3301400](../errorcode-geoLocationManager.md#3301400-query-failed-during-geocoding) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

let geocodeRequest: geoLocationManager.GeoCodeRequest = { "description": "No. xx, xx Road, Pudong District, Shanghai", "maxItems": 1};
try {
  geoLocationManager.getAddressesFromLocationName(geocodeRequest, (err, data) => {
    if (err) {
      console.error('getAddressesFromLocationName: err=' + JSON.stringify(err));
    }
    if (data) {
      console.info('getAddressesFromLocationName: data=' + JSON.stringify(data));
    }
  });
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```


## getAddressesFromLocationName

```TypeScript
function getAddressesFromLocationName(request: GeoCodeRequest): Promise<Array<GeoAddress>>
```

Obtain latitude and longitude info from location address.

**Since:** 23

**Deprecated since:** -1

<!--Device-geoLocationManager-function getAddressesFromLocationName(request: GeoCodeRequest): Promise<Array<GeoAddress>>--><!--Device-geoLocationManager-function getAddressesFromLocationName(request: GeoCodeRequest): Promise<Array<GeoAddress>>-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [GeoCodeRequest](arkts-location-geolocation-geocoderequest-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;GeoAddress & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [3301400](../errorcode-geoLocationManager.md#3301400-query-failed-during-geocoding) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let geocodeRequest: geoLocationManager.GeoCodeRequest = { "description": "No. xx, xx Road, Pudong District, Shanghai", "maxItems": 1};
try {
  geoLocationManager.getAddressesFromLocationName(geocodeRequest).then((result) => {
    console.info('getAddressesFromLocationName: ' + JSON.stringify(result));
  })
    .catch((error: BusinessError) => {
      console.error('promise, getAddressesFromLocationName: error=' + JSON.stringify(error));
    });
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
