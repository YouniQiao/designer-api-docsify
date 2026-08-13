# off_gnssStatusChange

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## off_gnssStatusChange

```TypeScript
function off(type: 'gnssStatusChange', callback?: Callback<SatelliteStatusInfo>): void
```

Unsubscribe gnss status changed

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** satelliteStatusChange

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function off(type: 'gnssStatusChange', callback?: Callback<SatelliteStatusInfo>): void--><!--Device-geolocation-function off(type: 'gnssStatusChange', callback?: Callback<SatelliteStatusInfo>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'gnssStatusChange' | Yes | Indicates the location service event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SatelliteStatusInfo&gt; | No | Indicates the callback for reporting the gnss status change. |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let gnssStatusCb = (satelliteStatusInfo:geolocation.SatelliteStatusInfo) => {
    console.info('gnssStatusChange: ' + JSON.stringify(satelliteStatusInfo));
}
geolocation.on('gnssStatusChange', gnssStatusCb);
geolocation.off('gnssStatusChange', gnssStatusCb);
```

