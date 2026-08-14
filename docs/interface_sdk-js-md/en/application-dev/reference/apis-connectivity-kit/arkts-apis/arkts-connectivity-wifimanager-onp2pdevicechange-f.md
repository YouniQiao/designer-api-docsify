# onP2pDeviceChange

## Modules to Import

```TypeScript
import { wifiManager } from 'wifiManager';
```

## onP2pDeviceChange

```TypeScript
function onP2pDeviceChange(callback: Callback<WifiP2pDevice>): void
```

Subscribe P2P local device change events.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function onP2pDeviceChange(callback: Callback<WifiP2pDevice>): void--><!--Device-wifiManager-function onP2pDeviceChange(callback: Callback<WifiP2pDevice>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WifiP2pDevice&gt; | Yes | the callback of on |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [2801000](../errorcode-wifi.md#2801000-p2p-module-error) | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

