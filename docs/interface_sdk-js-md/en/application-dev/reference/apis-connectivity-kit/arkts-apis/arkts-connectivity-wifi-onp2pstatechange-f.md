# on_p2pStateChange

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## on_p2pStateChange

```TypeScript
function on(type: 'p2pStateChange', callback: Callback<number>): void
```

Subscribe P2P status change events.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** p2pStateChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function on(type: 'p2pStateChange', callback: Callback<number>): void--><!--Device-wifi-function on(type: 'p2pStateChange', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'p2pStateChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes | the callback of on, 1: idle, 2: starting, 3:started, 4: closing, 5: closed |

