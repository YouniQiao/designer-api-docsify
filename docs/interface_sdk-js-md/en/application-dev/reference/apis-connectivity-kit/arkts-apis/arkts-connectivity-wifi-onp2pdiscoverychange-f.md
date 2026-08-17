# on_p2pDiscoveryChange

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## on_p2pDiscoveryChange

```TypeScript
function on(type: 'p2pDiscoveryChange', callback: Callback<number>): void
```

Subscribe P2P discovery events.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** p2pDiscoveryChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function on(type: 'p2pDiscoveryChange', callback: Callback<number>): void--><!--Device-wifi-function on(type: 'p2pDiscoveryChange', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'p2pDiscoveryChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes | the callback of on |

