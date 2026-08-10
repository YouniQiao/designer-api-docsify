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
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 201 | Permission denied. |

