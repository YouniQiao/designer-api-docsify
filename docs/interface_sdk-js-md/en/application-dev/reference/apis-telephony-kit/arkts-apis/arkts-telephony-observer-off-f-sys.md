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

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-observer-function off(type: 'cellInfoChange', callback?: Callback<Array<CellInformation>>): void--><!--Device-observer-function off(type: 'cellInfoChange', callback?: Callback<Array<CellInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cellInfoChange' | Yes | Cell information change event. This field has a fixed value of **cellInfoChange**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;CellInformation&gt;&gt; | No | Callback used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

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

