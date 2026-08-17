# sendUssdResponse (System API)

## Modules to Import

```TypeScript
import { call } from 'call';
```

## sendUssdResponse

```TypeScript
function sendUssdResponse(slotId: int, content: string): void
```

Sends a response to the Unstructured Supplementary Service Data (USSD) service to the carrier.

**Since:** 26.0.0

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function sendUssdResponse(slotId: int, content: string): void--><!--Device-call-function sendUssdResponse(slotId: int, content: string): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | ID of the card slot that sends the response. |
| content | string | Yes | Response content. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 8400001 | Invalid parameter value. |
| 8400002 | Operation failed. Cannot connect to service. |
| 8400003 | System internal error, system database write fail. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

