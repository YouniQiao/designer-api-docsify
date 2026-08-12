# offCallStateChangeEx

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## offCallStateChangeEx

```TypeScript
function offCallStateChangeEx(callback?: Callback<TelCallState>): void
```

Cancel callback when the telCall state is updated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-observer-function offCallStateChangeEx(callback?: Callback<TelCallState>): void--><!--Device-observer-function offCallStateChangeEx(callback?: Callback<TelCallState>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;TelCallState&gt; | No | Indicates the callback to unsubscribe from the callStateChangeEx event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8800999](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800999-internal-error) | Unknown error. |
| [8800002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800002-service-connection-error) | Service connection failed. |
| [8800003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800003-system-internal-error) | System internal error. |
| [8800001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800001-input-parameter-value-out-of-range) | Invalid parameter value. |

