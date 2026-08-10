# getCallTransferInfo (System API)

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## getCallTransferInfo

```TypeScript
function getCallTransferInfo(slotId: int, type: CallTransferType, callback: AsyncCallback<CallTransferResult>): void
```

Get call forwarding information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-call-function getCallTransferInfo(slotId: int, type: CallTransferType, callback: AsyncCallback<CallTransferResult>): void--><!--Device-call-function getCallTransferInfo(slotId: int, type: CallTransferType, callback: AsyncCallback<CallTransferResult>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| type | [CallTransferType](arkts-telephony-call-calltransfertype-e.md) | Yes | Indicates which type of call forwarding to obtain. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CallTransferResult&gt; | Yes | Indicates the callback for getting the call forwarding status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.getCallTransferInfo(0, call.CallTransferType.TRANSFER_TYPE_BUSY, (err: BusinessError, data: call.CallTransferResult) => {
    if (err) {
        console.error(`getCallTransferInfo fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`getCallTransferInfo success, data->${JSON.stringify(data)}`);
    }
});
```


## getCallTransferInfo

```TypeScript
function getCallTransferInfo(slotId: int, type: CallTransferType): Promise<CallTransferResult>
```

Get call forwarding information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_TELEPHONY_STATE

<!--Device-call-function getCallTransferInfo(slotId: int, type: CallTransferType): Promise<CallTransferResult>--><!--Device-call-function getCallTransferInfo(slotId: int, type: CallTransferType): Promise<CallTransferResult>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| type | [CallTransferType](arkts-telephony-call-calltransfertype-e.md) | Yes | Indicates which type of call forwarding to obtain. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CallTransferResult&gt; | Returns the call forwarding status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.getCallTransferInfo(0, call.CallTransferType.TRANSFER_TYPE_BUSY).then((data: call.CallTransferResult) => {
    console.info(`getCallTransferInfo success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getCallTransferInfo fail, promise: err->${JSON.stringify(err)}`);
});
```

