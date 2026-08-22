# onP2pConnectionChange

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## onP2pConnectionChange

```TypeScript
function onP2pConnectionChange(callback: Callback<WifiP2pLinkedInfo>): void
```

Subscribe P2P connection change events.

**Since:** 23

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function onP2pConnectionChange(callback: Callback<WifiP2pLinkedInfo>): void--><!--Device-wifiManager-function onP2pConnectionChange(callback: Callback<WifiP2pLinkedInfo>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WifiP2pLinkedInfo&gt; | Yes | the callback of on |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [2801000](../errorcode-wifi.md#2801000-p2p-module-error) | Operation failed. |

