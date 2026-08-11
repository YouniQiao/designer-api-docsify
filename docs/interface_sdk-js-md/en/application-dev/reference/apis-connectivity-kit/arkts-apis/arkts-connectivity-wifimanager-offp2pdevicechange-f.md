# offP2pDeviceChange

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## offP2pDeviceChange

```TypeScript
function offP2pDeviceChange(callback?: Callback<WifiP2pDevice>): void
```

Unsubscribe P2P local device change events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-wifiManager-function offP2pDeviceChange(callback?: Callback<WifiP2pDevice>): void--><!--Device-wifiManager-function offP2pDeviceChange(callback?: Callback<WifiP2pDevice>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WifiP2pDevice&gt; | No | the callback of off |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [2801000](../errorcode-wifi.md#2801000-p2p-module-error) | Operation failed. |

