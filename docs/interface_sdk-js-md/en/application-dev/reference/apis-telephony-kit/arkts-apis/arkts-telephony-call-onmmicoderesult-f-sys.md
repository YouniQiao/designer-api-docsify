# onMmiCodeResult (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## onMmiCodeResult

```TypeScript
function onMmiCodeResult(callback: Callback<MmiCodeResults>): void
```

Subscribe to the mmiCodeResult event.

**Since:** 26.1.0

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function onMmiCodeResult(callback: Callback<MmiCodeResults>): void--><!--Device-call-function onMmiCodeResult(callback: Callback<MmiCodeResults>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[MmiCodeResults](arkts-telephony-call-mmicoderesults-i-sys.md)&gt; | Yes | Indicates the callback for getting the result of MMI code. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error code. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Operation failed. Cannot connect to service. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

