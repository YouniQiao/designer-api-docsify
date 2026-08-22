# on_p2pConnectionChange

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
import { wifiext } from '@kit.ConnectivityKit';
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## on('p2pConnectionChange')

```TypeScript
function on(type: 'p2pConnectionChange', callback: Callback<WifiP2pLinkedInfo>): void
```

Subscribe P2P connection change events.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** p2pConnectionChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function on(type: 'p2pConnectionChange', callback: Callback<WifiP2pLinkedInfo>): void--><!--Device-wifi-function on(type: 'p2pConnectionChange', callback: Callback<WifiP2pLinkedInfo>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'p2pConnectionChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WifiP2pLinkedInfo&gt; | Yes | the callback of on |

