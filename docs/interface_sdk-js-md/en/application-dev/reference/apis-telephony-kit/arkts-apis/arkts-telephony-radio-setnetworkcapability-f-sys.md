# setNetworkCapability (System API)

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## setNetworkCapability

```TypeScript
function setNetworkCapability(slotId: int, type: NetworkCapabilityType, state: NetworkCapabilityState,
    callback: AsyncCallback<void>): void
```

Set the type and state for the specified network capability.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-radio-function setNetworkCapability(slotId: int, type: NetworkCapabilityType, state: NetworkCapabilityState,    callback: AsyncCallback<void>): void--><!--Device-radio-function setNetworkCapability(slotId: int, type: NetworkCapabilityType, state: NetworkCapabilityState,    callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| type | [NetworkCapabilityType](arkts-telephony-radio-networkcapabilitytype-e-sys.md) | Yes | Indicates the service type of the [NetworkCapabilityType](arkts-telephony-radio-networkcapabilitytype-e-sys.md#NetworkCapabilityType). |
| state | [NetworkCapabilityState](arkts-telephony-radio-networkcapabilitystate-e-sys.md) | Yes | Indicates the service ability state of the [NetworkCapabilityState](arkts-telephony-radio-networkcapabilitystate-e-sys.md#NetworkCapabilityState). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | The callback of setNetworkCapability. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
let type: radio.NetworkCapabilityType = radio.NetworkCapabilityType.SERVICE_TYPE_NR;
let state: radio.NetworkCapabilityState = radio.NetworkCapabilityState.SERVICE_CAPABILITY_ON;
radio.setNetworkCapability(slotId, type, state, (err: BusinessError) => {
    if (err) {
        console.error(`setNetworkCapability failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.info(`setNetworkCapability success.`);
});
```


## setNetworkCapability

```TypeScript
function setNetworkCapability(slotId: int, type: NetworkCapabilityType, state: NetworkCapabilityState): Promise<void>
```

Set the type and state for the specified network capability.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-radio-function setNetworkCapability(slotId: int, type: NetworkCapabilityType, state: NetworkCapabilityState): Promise<void>--><!--Device-radio-function setNetworkCapability(slotId: int, type: NetworkCapabilityType, state: NetworkCapabilityState): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| type | [NetworkCapabilityType](arkts-telephony-radio-networkcapabilitytype-e-sys.md) | Yes | Indicates the service type of the [NetworkCapabilityType](arkts-telephony-radio-networkcapabilitytype-e-sys.md#NetworkCapabilityType). |
| state | [NetworkCapabilityState](arkts-telephony-radio-networkcapabilitystate-e-sys.md) | Yes | Indicates the service ability state of the [NetworkCapabilityState](arkts-telephony-radio-networkcapabilitystate-e-sys.md#NetworkCapabilityState). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the setNetworkCapability. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
let type: radio.NetworkCapabilityType = radio.NetworkCapabilityType.SERVICE_TYPE_NR;
let state: radio.NetworkCapabilityState = radio.NetworkCapabilityState.SERVICE_CAPABILITY_ON;
radio.setNetworkCapability(slotId, type, state).then(() => {
    console.info(`setNetworkCapability success`);
}).catch((err: BusinessError) => {
    console.error(`setNetworkCapability failed, promise: err->${JSON.stringify(err)}`);
});
```

