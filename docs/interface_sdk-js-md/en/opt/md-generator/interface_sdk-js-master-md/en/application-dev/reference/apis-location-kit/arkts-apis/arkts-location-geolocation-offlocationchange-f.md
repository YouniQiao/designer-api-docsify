# off_locationChange

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## off_locationChange

```TypeScript
function off(type: 'locationChange', callback?: Callback<Location>): void
```

Unsubscribe location changed

**Since:** 7

**Deprecated since:** 9

**Substitutes:** locationChange

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function off(type: 'locationChange', callback?: Callback<Location>): void--><!--Device-geolocation-function off(type: 'locationChange', callback?: Callback<Location>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'locationChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | No |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationRequest = {'priority': 0x203, 'scenario': 0x300, 'timeInterval': 0, 'distanceInterval': 0, 'maxAccuracy': 0};
let locationChange = (location:geolocation.Location):void => {
    console.info('locationChanger: data: ' + JSON.stringify(location));
};
geolocation.on('locationChange', requestInfo, locationChange);
geolocation.off('locationChange', locationChange);
```
