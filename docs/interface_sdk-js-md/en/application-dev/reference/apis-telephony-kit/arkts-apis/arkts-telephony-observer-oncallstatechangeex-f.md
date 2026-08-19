# onCallStateChangeEx

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## onCallStateChangeEx

```TypeScript
function onCallStateChangeEx(callback: Callback<TelCallState>, options?: ObserverOptions): void
```

Callback when the telCall state corresponding to the monitored {@code slotId} is updated.

**Since:** 23

<!--Device-observer-function onCallStateChangeEx(callback: Callback<TelCallState>, options?: ObserverOptions): void--><!--Device-observer-function onCallStateChangeEx(callback: Callback<TelCallState>, options?: ObserverOptions): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | Yes | Indicates the callback for getting the telCall state. |
| options | ObserverOptions | No | Indicates the options for observer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8800999](../errorcode-telephony.md#8800999-internal-error) | Unknown error. |
| [8800002](../errorcode-telephony.md#8800002-service-connection-error) | Service connection failed. |
| [8800003](../errorcode-telephony.md#8800003-system-internal-error) | System internal error. |
| [8800001](../errorcode-telephony.md#8800001-input-parameter-value-out-of-range) | Invalid parameter value. |

