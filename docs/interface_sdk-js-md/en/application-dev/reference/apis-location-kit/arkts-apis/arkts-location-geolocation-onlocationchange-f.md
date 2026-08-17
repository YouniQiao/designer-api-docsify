# on_locationChange

## Modules to Import

```TypeScript
import { geolocation } from 'geolocation';
```

## on_locationChange

```TypeScript
function on(type: 'locationChange', request: LocationRequest, callback: Callback<Location>): void
```

Subscribe location changed

**Since:** 7

**Deprecated since:** 9

**Substitutes:** locationChange

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function on(type: 'locationChange', request: LocationRequest, callback: Callback<Location>): void--><!--Device-geolocation-function on(type: 'locationChange', request: LocationRequest, callback: Callback<Location>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'locationChange' | Yes | Indicates the location service event to be subscribed to. |
| request | LocationRequest | Yes | Indicates the location request parameters. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | Yes | Indicates the callback for reporting the location result. |

**Examples**

```TypeScript
import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationRequest = {'priority': 0x203, 'scenario': 0x300, 'timeInterval': 0, 'distanceInterval': 0, 'maxAccuracy': 0};
let locationChange = (location:geolocation.Location):void => {
    console.info('locationChanger: data: ' + JSON.stringify(location));
};
geolocation.on('locationChange', requestInfo, locationChange);
```

