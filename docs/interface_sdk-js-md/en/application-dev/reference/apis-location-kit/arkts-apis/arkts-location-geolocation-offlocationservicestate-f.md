# off_locationServiceState

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## off_locationServiceState('locationServiceState')

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'locationServiceState' | Yes | Indicates the location service event to be subscribed to. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | Indicates the callback for reporting the location result. |

**Examples**

```TypeScript
import geolocation from '@ohos.geolocation';
let locationServiceState = (state:boolean):void => {
    console.info('locationServiceState: state: ' + JSON.stringify(state));
}
geolocation.on('locationServiceState', locationServiceState);
geolocation.off('locationServiceState', locationServiceState);
```

