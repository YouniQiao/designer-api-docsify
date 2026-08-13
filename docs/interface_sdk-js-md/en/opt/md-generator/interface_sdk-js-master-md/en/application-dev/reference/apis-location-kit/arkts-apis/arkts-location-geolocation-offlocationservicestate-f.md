# off_locationServiceState

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## off_locationServiceState

```TypeScript
function off(type: 'locationServiceState', callback?: Callback<boolean>): void
```

Unsubscribe location switch changed

**Since:** 7

**Deprecated since:** 9

**Substitutes:** locationEnabledChange

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function off(type: 'locationServiceState', callback?: Callback<boolean>): void--><!--Device-geolocation-function off(type: 'locationServiceState', callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'locationServiceState' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let locationServiceState = (state:boolean):void => {
    console.info('locationServiceState: state: ' + JSON.stringify(state));
}
geolocation.on('locationServiceState', locationServiceState);
geolocation.off('locationServiceState', locationServiceState);
```
