# off_cachedGnssLocationsReporting

## Modules to Import

```TypeScript
import { geolocation } from 'geolocation';
```

## off_cachedGnssLocationsReporting

```TypeScript
function off(type: 'cachedGnssLocationsReporting', callback?: Callback<Array<Location>>): void
```

Unsubscribe to cache GNSS locations update messages

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** cachedGnssLocationsChange

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function off(type: 'cachedGnssLocationsReporting', callback?: Callback<Array<Location>>): void--><!--Device-geolocation-function off(type: 'cachedGnssLocationsReporting', callback?: Callback<Array<Location>>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cachedGnssLocationsReporting' | Yes | Indicates the location service event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;Location&gt;&gt; | No | Indicates the callback for reporting the cached gnss locations. |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let cachedLocationsCb = (locations:Array<geolocation.Location>):void => {
    console.info('cachedGnssLocationsReporting: locations: ' + JSON.stringify(locations));
}
let requestInfo:geolocation.CachedGnssLocationsRequest = {'reportingPeriodSec': 10, 'wakeUpCacheQueueFull': true};
geolocation.on('cachedGnssLocationsReporting', requestInfo, cachedLocationsCb);
geolocation.off('cachedGnssLocationsReporting');
```

