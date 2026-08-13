# on_p2pStateChange

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'p2pStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |
