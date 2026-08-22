# on_p2pPeerDeviceChange

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
import { wifiext } from '@kit.ConnectivityKit';
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## on('p2pPeerDeviceChange')

```TypeScript
function on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice[]>): void
```

Subscribe P2P peer device change events.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** p2pPeerDeviceChange

**Required permissions:** ohos.permission.GET_WIFI_INFO and ohos.permission.LOCATION

<!--Device-wifi-function on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice[]>): void--><!--Device-wifi-function on(type: 'p2pPeerDeviceChange', callback: Callback<WifiP2pDevice[]>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'p2pPeerDeviceChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WifiP2pDevice[]&gt; | Yes | the callback of on |

