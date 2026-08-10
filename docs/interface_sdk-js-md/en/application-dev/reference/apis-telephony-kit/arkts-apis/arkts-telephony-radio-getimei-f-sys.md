# getIMEI (System API)

## Modules to Import

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## getIMEI

```TypeScript
function getIMEI(slotId: int, callback: AsyncCallback<string>): void
```

Obtains the IMEI of a specified card slot of the device.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function getIMEI(slotId: int, callback: AsyncCallback<string>): void--><!--Device-radio-function getIMEI(slotId: int, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Indicates the callback for getting the IMEI. Returns an empty string if the IMEI does not exist. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getIMEI(slotId, (err: BusinessError, data: string) => {
    if (err) {
        console.error(`getIMEI failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.info(`getIMEI success, callback: data->${JSON.stringify(data)}`);
});
```


## getIMEI

```TypeScript
function getIMEI(slotId?: int): Promise<string>
```

Obtains the IMEI of a specified card slot of the device.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function getIMEI(slotId?: int): Promise<string>--><!--Device-radio-function getIMEI(slotId?: int): Promise<string>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Returns the IMEI. Returns an empty string if the IMEI does not exist. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getIMEI(slotId).then((data: string) => {
    console.info(`getIMEI success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getIMEI failed, promise: err->${JSON.stringify(err)}`);
});
```


## getIMEI

```TypeScript
function getIMEI(callback: AsyncCallback<string>): void
```

Obtains the IMEI of a specified card slot of the device.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function getIMEI(callback: AsyncCallback<string>): void--><!--Device-radio-function getIMEI(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Indicates the callback for getting the IMEI. Returns an empty string if the IMEI does not exist. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

radio.getIMEI((err: BusinessError, data: string) => {
    if (err) {
        console.error(`getIMEI failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.info(`getIMEI success, callback: data->${JSON.stringify(data)}`);
});
```

