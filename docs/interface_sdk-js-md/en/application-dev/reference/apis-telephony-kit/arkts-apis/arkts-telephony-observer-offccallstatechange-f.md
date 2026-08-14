# offCCallStateChange

## Modules to Import

```TypeScript
import { observer } from 'observer';
```

## offCCallStateChange

```TypeScript
function offCCallStateChange(callback?: Callback<CCallStateInfo>): void
```

Cancels the listening on the carrier call status and obtaining of the call number by a third-party application. This method uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_CALL_FOR_DEVICES

<!--Device-observer-function offCCallStateChange(callback?: Callback<CCallStateInfo>): void--><!--Device-observer-function offCCallStateChange(callback?: Callback<CCallStateInfo>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CCallStateInfo](arkts-telephony-observer-ccallstateinfo-i.md)&gt; | No | Callback function used to return the call status information object. <br>The application can obtain CCallState. <br> |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8800999](../errorcode-telephony.md#8800999-internal-error) | Unknown error. |
| [8800002](../errorcode-telephony.md#8800002-service-connection-error) | Service connection failed. |
| [8800003](../errorcode-telephony.md#8800003-system-internal-error) | System internal error. |
| [8800001](../errorcode-telephony.md#8800001-input-parameter-value-out-of-range) | Invalid parameter value. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { call, observer } from '@kit.TelephonyKit';

let callback: (data: observer.CCallStateInfo) => void = (data: observer.CCallStateInfo) => {
    console.info("onCCallStateChange, data:" + JSON.stringify(data));
}

observer.offCCallStateChange(callback);
observer.offCCallStateChange();
```

