# enableCellularDataRoaming (System API)

## Modules to Import

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## enableCellularDataRoaming

```TypeScript
function enableCellularDataRoaming(slotId: int, callback: AsyncCallback<void>): void
```

Enable cellular data roaming.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-data-function enableCellularDataRoaming(slotId: int, callback: AsyncCallback<void>): void--><!--Device-data-function enableCellularDataRoaming(slotId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Telephony.CellularData

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the ID of a card slot. The value {@code 0} indicates card 1, and the value {@code 1} indicates card 2. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The callback of enableCellularDataRoaming. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Internal error. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.enableCellularDataRoaming(0, (err: BusinessError) => {
    if(err) {
        console.error(`enableCellularDataRoaming fail. code: ${err.code}, message: ${err.message}`);
    } else {
        console.info(`enableCellularDataRoaming success`);
    }
});
```


## enableCellularDataRoaming

```TypeScript
function enableCellularDataRoaming(slotId: int): Promise<void>
```

Enable cellular data roaming.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-data-function enableCellularDataRoaming(slotId: int): Promise<void>--><!--Device-data-function enableCellularDataRoaming(slotId: int): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CellularData

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the ID of a card slot. The value {@code 0} indicates card 1, and the value {@code 1} indicates card 2. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the enableCellularDataRoaming. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Internal error. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.enableCellularDataRoaming(0).then(() => {
    console.info(`enableCellularDataRoaming success.`);
}).catch((err: BusinessError) => {
    console.error(`enableCellularDataRoaming fail. code: ${err.code}, message: ${err.message}`);
});
```

