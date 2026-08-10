# offHotspotStateChange

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## offHotspotStateChange

```TypeScript
function offHotspotStateChange(callback?: Callback<int>): void
```

Unsubscribe Wi-Fi hotspot state change events.All callback functions will be deregistered If there is no specific callback parameter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function offHotspotStateChange(callback?: Callback<int>): void--><!--Device-wifiManager-function offHotspotStateChange(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | No | the callback of off |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 2601000 | Operation failed. |

