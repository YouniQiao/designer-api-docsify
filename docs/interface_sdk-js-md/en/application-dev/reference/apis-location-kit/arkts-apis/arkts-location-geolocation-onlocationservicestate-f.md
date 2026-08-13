# on_locationServiceState

## Modules to Import

```TypeScript
import { geolocation } from '@kit.LocationKit';
```

## on_locationServiceState

```TypeScript
function on(type: 'locationServiceState', callback: Callback<boolean>): void
```

Subscribe location switch changed

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** locationEnabledChange

**Required permissions:** ohos.permission.LOCATION

<!--Device-geolocation-function on(type: 'locationServiceState', callback: Callback<boolean>): void--><!--Device-geolocation-function on(type: 'locationServiceState', callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'locationServiceState' | Yes | Indicates the location service event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes | Indicates the callback for reporting the location result. |

## Examples

```TypeScript
import geolocation from '@ohos.geolocation';
let locationServiceState = (state:boolean):void => {
    console.info('locationServiceState: ' + JSON.stringify(state));
}
geolocation.on('locationServiceState', locationServiceState);
```

