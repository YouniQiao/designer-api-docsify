# onCCallStateChange

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## onCCallStateChange

```TypeScript
function onCCallStateChange(callback: Callback<CCallStateInfo>, options?: ObserverOptions): void
```

Subscribes to the carrier call state changes and obtains the call number. This method uses an asynchronous callback to return the execution result.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_CALL_FOR_DEVICES

<!--Device-observer-function onCCallStateChange(callback: Callback<CCallStateInfo>, options?: ObserverOptions): void--><!--Device-observer-function onCCallStateChange(callback: Callback<CCallStateInfo>, options?: ObserverOptions): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CCallStateInfo](arkts-telephony-observer-ccallstateinfo-i.md)&gt; | Yes |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | No |

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
let options: observer.ObserverOptions = {
    slotId: 0
}

observer.onCCallStateChange(callback, options);
observer.onCCallStateChange(callback);
```
