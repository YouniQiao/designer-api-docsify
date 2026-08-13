# on_gnssStatusChange

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## on_gnssStatusChange

```TypeScript
function on(type: 'gnssStatusChange', callback: Callback<SatelliteStatusInfo>): void
```

Subscribe gnss status changed

**Since:** 8

**Deprecated since:** 9

**Substitutes:** satelliteStatusChange

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function on(type: 'gnssStatusChange', callback: Callback<SatelliteStatusInfo>): void--><!--Device-geolocation-function on(type: 'gnssStatusChange', callback: Callback<SatelliteStatusInfo>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'gnssStatusChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SatelliteStatusInfo&gt; | Yes |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let gnssStatusCb = (satelliteStatusInfo:geolocation.SatelliteStatusInfo):void => {
    console.info('gnssStatusChange: ' + JSON.stringify(satelliteStatusInfo));
}
geolocation.on('gnssStatusChange', gnssStatusCb);
```
