# off (System API)

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## off('cellInfoChange')

```TypeScript
function off(type: 'cellInfoChange', callback?: Callback<Array<CellInformation>>): void
```

Unregisters the observer for cell information change events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
> you do not pass the callback, you will cancel listening for all events.

**Since:** 8

<!--Device-observer-function off(type: 'cellInfoChange', callback?: Callback<Array<CellInformation>>): void--><!--Device-observer-function off(type: 'cellInfoChange', callback?: Callback<Array<CellInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cellInfoChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;CellInformation&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { radio } from '@kit.TelephonyKit';

let callback: (data: Array<radio.CellInformation>) => void = (data: Array<radio.CellInformation>) => {
    console.info("on cellInfoChange, data:" + JSON.stringify(data));
}
observer.on('cellInfoChange', callback);
// You can pass the callback of the on method to cancel listening for a certain type of callback. If you do not pass the callback, you will cancel listening for all callbacks.
observer.off('cellInfoChange', callback);
observer.off('cellInfoChange');
```
