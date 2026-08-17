# off_nmeaMessageChange

## Modules to Import

```TypeScript
import { geolocation } from 'geolocation';
```

## off_nmeaMessageChange

```TypeScript
function off(type: 'nmeaMessageChange', callback?: Callback<string>): void
```

Unsubscribe nmea message changed

**Since:** 8

**Deprecated since:** 9

**Substitutes:** nmeaMessage

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function off(type: 'nmeaMessageChange', callback?: Callback<string>): void--><!--Device-geolocation-function off(type: 'nmeaMessageChange', callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'nmeaMessageChange' | Yes | Indicates the location service event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No | Indicates the callback for reporting the nmea message. |

**Examples**

```TypeScript
import geolocation from '@ohos.geolocation';
let nmeaCb = (str:string):void => {
    console.info('nmeaMessageChange: ' + JSON.stringify(str));
}
geolocation.on('nmeaMessageChange', nmeaCb);
geolocation.off('nmeaMessageChange', nmeaCb);
```

