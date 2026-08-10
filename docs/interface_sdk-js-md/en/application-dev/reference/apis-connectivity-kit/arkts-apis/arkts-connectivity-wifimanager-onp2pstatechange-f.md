# onP2pStateChange

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## onP2pStateChange

```TypeScript
function onP2pStateChange(callback: Callback<int>): void
```

Subscribe P2P status change events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function onP2pStateChange(callback: Callback<int>): void--><!--Device-wifiManager-function onP2pStateChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | the callback of on, 1: idle, 2: starting, 3:started, 4: closing, 5: closed |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 201 | Permission denied. |

