# onP2pDiscoveryChange

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## onP2pDiscoveryChange

```TypeScript
function onP2pDiscoveryChange(callback: Callback<int>): void
```

Subscribe P2P discovery events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function onP2pDiscoveryChange(callback: Callback<int>): void--><!--Device-wifiManager-function onP2pDiscoveryChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | the callback of on |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [2801000](../errorcode-wifi.md#2801000-p2p-module-error) | Operation failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

