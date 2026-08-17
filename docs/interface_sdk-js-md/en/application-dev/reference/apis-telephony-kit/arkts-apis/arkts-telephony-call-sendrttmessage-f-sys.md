# sendRttMessage (System API)

## Modules to Import

```TypeScript
import { call } from 'call';
```

## sendRttMessage

```TypeScript
function sendRttMessage(callId: int, rttMessage: string): Promise<void>
```

Send rtt message.

**Since:** 23

**Required permissions:** ohos.permission.PLACE_CALL

<!--Device-call-function sendRttMessage(callId: int, rttMessage: string): Promise<void>--><!--Device-call-function sendRttMessage(callId: int, rttMessage: string): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callId | int | Yes | Indicates the identifier of the call. |
| rttMessage | string | Yes | Indicates the message of rtt. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the sendRttMessage. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 8400001 | Invalid parameter value. |
| 8400002 | Operation failed. Cannot connect to service. |
| 8400003 | System internal error. |
| 8400999 | Unknown error code. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

