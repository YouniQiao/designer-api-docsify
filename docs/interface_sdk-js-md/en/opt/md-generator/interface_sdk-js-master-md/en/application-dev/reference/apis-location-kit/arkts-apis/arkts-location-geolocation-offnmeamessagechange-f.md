# off_nmeaMessageChange

## Modules to Import

```TypeScript
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'nmeaMessageChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No |

**Examples**

```TypeScript
import geolocation from '@ohos.geolocation';
let nmeaCb = (str:string):void => {
    console.info('nmeaMessageChange: ' + JSON.stringify(str));
}
geolocation.on('nmeaMessageChange', nmeaCb);
geolocation.off('nmeaMessageChange', nmeaCb);
```
