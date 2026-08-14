# off_hotspotStateChange

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## off_hotspotStateChange

```TypeScript
function off(type: 'hotspotStateChange', callback?: Callback<number>): void
```

Unsubscribe Wi-Fi hotspot state change events. &lt;p&gt;All callback functions will be deregistered If there is no specific callback parameter.&lt;/p&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** hotspotStateChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function off(type: 'hotspotStateChange', callback?: Callback<number>): void--><!--Device-wifi-function off(type: 'hotspotStateChange', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hotspotStateChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No | the callback of on, 0: inactive, 1: active, 2: activating, 3: de-activating |

