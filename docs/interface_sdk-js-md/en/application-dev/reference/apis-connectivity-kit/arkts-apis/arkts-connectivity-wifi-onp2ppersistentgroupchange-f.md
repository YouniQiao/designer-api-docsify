# on_p2pPersistentGroupChange

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## on_p2pPersistentGroupChange

```TypeScript
function on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void
```

Subscribe P2P persistent group change events.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** p2pPersistentGroupChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void--><!--Device-wifi-function on(type: 'p2pPersistentGroupChange', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'p2pPersistentGroupChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback of on |

