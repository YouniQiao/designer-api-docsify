# on (System API)

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## on('cellInfoChange')

```TypeScript
function on(type: 'cellInfoChange', callback: Callback<Array<CellInformation>>): void
```

Registers an observer for cell information change events. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-observer-function on(type: 'cellInfoChange', callback: Callback<Array<CellInformation>>): void--><!--Device-observer-function on(type: 'cellInfoChange', callback: Callback<Array<CellInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cellInfoChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;CellInformation&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { radio } from '@kit.TelephonyKit';

observer.on('cellInfoChange', (data: Array<radio.CellInformation>) => {
    console.info("on cellInfoChange, data:" + JSON.stringify(data));
});
```


## on('cellInfoChange')

```TypeScript
function on(type: 'cellInfoChange', options: ObserverOptions, callback: Callback<Array<CellInformation>>): void
```

Registers an observer for signal status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the execution result.

**Since:** 8

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-observer-function on(type: 'cellInfoChange', options: ObserverOptions, callback: Callback<Array<CellInformation>>): void--><!--Device-observer-function on(type: 'cellInfoChange', options: ObserverOptions, callback: Callback<Array<CellInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cellInfoChange' | Yes |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;CellInformation&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { radio } from '@kit.TelephonyKit';

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('cellInfoChange', options, (data: Array<radio.CellInformation>) => {
    console.info("on cellInfoChange, data:" + JSON.stringify(data));
});
```
