# startManualNetworkScan (System API)

## Modules to Import

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## startManualNetworkScan

```TypeScript
function startManualNetworkScan(slotId: int, callback: Callback<NetworkSearchRealTimeResult>): void
```

start ManualNetworkScan , Real-time report.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function startManualNetworkScan(slotId: int, callback: Callback<NetworkSearchRealTimeResult>): void--><!--Device-radio-function startManualNetworkScan(slotId: int, callback: Callback<NetworkSearchRealTimeResult>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkSearchRealTimeResult&gt; | Yes | Indicates the callback for manual network scan |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Nonsystem applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

