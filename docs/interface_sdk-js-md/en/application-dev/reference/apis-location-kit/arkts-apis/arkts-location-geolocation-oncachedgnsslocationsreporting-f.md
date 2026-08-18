# on_cachedGnssLocationsReporting

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## on_cachedGnssLocationsReporting('cachedGnssLocationsReporting')

```TypeScript
function on(type: 'cachedGnssLocationsReporting', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void
```

Subscribe to cache GNSS locations update messages

**Since:** 8

**Deprecated since:** 9

**Substitutes:** cachedGnssLocationsChange

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function on(type: 'cachedGnssLocationsReporting', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void--><!--Device-geolocation-function on(type: 'cachedGnssLocationsReporting', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cachedGnssLocationsReporting' | Yes | Indicates the location service event to be subscribed to. |
| request | CachedGnssLocationsRequest | Yes | Indicates the cached GNSS locations request parameters. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;Location&gt;&gt; | Yes | Indicates the callback for reporting the cached GNSS locations. |

**Examples**

```TypeScript
import geolocation from '@ohos.geolocation';
let cachedLocationsCb = (locations:Array<geolocation.Location>):void => {
    console.info('cachedGnssLocationsReporting: locations: ' + JSON.stringify(locations));
}
let requestInfo:geolocation.CachedGnssLocationsRequest = {'reportingPeriodSec': 10, 'wakeUpCacheQueueFull': true};
geolocation.on('cachedGnssLocationsReporting', requestInfo, cachedLocationsCb);
```

