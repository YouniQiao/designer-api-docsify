# offP2pPeerDeviceChange

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## offP2pPeerDeviceChange

```TypeScript
function offP2pPeerDeviceChange(callback?: Callback<WifiP2pDevice[]>): void
```

Unsubscribe P2P peer device change events.

**Since:** 23

<!--Device-wifiManager-function offP2pPeerDeviceChange(callback?: Callback<WifiP2pDevice[]>): void--><!--Device-wifiManager-function offP2pPeerDeviceChange(callback?: Callback<WifiP2pDevice[]>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WifiP2pDevice[]&gt; | No | the callback of off |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [2801000](../errorcode-wifi.md#2801000-p2p-module-error) | Operation failed. |

