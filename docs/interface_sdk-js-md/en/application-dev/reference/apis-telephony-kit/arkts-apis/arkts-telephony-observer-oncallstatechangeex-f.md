# onCallStateChangeEx

## Modules to Import

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## onCallStateChangeEx

```TypeScript
function onCallStateChangeEx(callback: Callback<TelCallState>, options?: ObserverOptions): void
```

Callback when the telCall state corresponding to the monitored {@code slotId} is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-observer-function onCallStateChangeEx(callback: Callback<TelCallState>, options?: ObserverOptions): void--><!--Device-observer-function onCallStateChangeEx(callback: Callback<TelCallState>, options?: ObserverOptions): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | Yes | Indicates the callback for getting the telCall state. |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | No | Indicates the options for observer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 8800999 | Unknown error. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800001 | Invalid parameter value. |

