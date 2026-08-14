# offCallStateChangeEx

## Modules to Import

```TypeScript
import { observer } from 'observer';
```

## offCallStateChangeEx

```TypeScript
function offCallStateChangeEx(callback?: Callback<TelCallState>): void
```

Cancel callback when the telCall state is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-observer-function offCallStateChangeEx(callback?: Callback<TelCallState>): void--><!--Device-observer-function offCallStateChangeEx(callback?: Callback<TelCallState>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | No | Indicates the callback to unsubscribe from the callStateChangeEx event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8800999](../errorcode-telephony.md#8800999-internal-error) | Unknown error. |
| [8800002](../errorcode-telephony.md#8800002-service-connection-error) | Service connection failed. |
| [8800003](../errorcode-telephony.md#8800003-system-internal-error) | System internal error. |
| [8800001](../errorcode-telephony.md#8800001-input-parameter-value-out-of-range) | Invalid parameter value. |

