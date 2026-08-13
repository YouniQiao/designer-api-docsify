# offCCallStateChange

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## offCCallStateChange

```TypeScript
function offCCallStateChange(callback?: Callback<CCallStateInfo>): void
```

Cancels the listening on the carrier call status and obtaining of the call number by a third-party application.This method uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_CALL_FOR_DEVICES

<!--Device-observer-function offCCallStateChange(callback?: Callback<CCallStateInfo>): void--><!--Device-observer-function offCCallStateChange(callback?: Callback<CCallStateInfo>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CCallStateInfo](arkts-telephony-observer-ccallstateinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [8800999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800999-internal-error) |
| [8800002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800002-service-connection-error) |
| [8800003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800003-system-internal-error) |
| [8800001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800001-input-parameter-value-out-of-range) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { call, observer } from '@kit.TelephonyKit';

let callback: (data: observer.CCallStateInfo) => void = (data: observer.CCallStateInfo) => {
    console.info("onCCallStateChange, data:" + JSON.stringify(data));
}

observer.offCCallStateChange(callback);
observer.offCCallStateChange();
```
