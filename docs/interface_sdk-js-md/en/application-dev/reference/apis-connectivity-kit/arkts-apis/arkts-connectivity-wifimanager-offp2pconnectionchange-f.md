# offP2pConnectionChange

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## offP2pConnectionChange

```TypeScript
function offP2pConnectionChange(callback?: Callback<WifiP2pLinkedInfo>): void
```

Unsubscribe P2P connection change events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function offP2pConnectionChange(callback?: Callback<WifiP2pLinkedInfo>): void--><!--Device-wifiManager-function offP2pConnectionChange(callback?: Callback<WifiP2pLinkedInfo>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WifiP2pLinkedInfo&gt; | No | the callback of off |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [2801000](../errorcode-wifi.md#2801000-p2p-module-error) | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

