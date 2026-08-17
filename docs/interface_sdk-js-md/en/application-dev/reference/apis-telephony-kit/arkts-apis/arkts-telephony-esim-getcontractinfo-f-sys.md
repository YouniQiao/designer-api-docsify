# getContractInfo (System API)

## Modules to Import

```TypeScript
import { eSIM } from 'eSIM';
```

## getContractInfo

```TypeScript
function getContractInfo(slotId: int, requestData: ContractRequestData) : Promise<string>
```

Get contract info

**Since:** 23

**Required permissions:** ohos.permission.GET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function getContractInfo(slotId: int, requestData: ContractRequestData) : Promise<string>--><!--Device-eSIM-function getContractInfo(slotId: int, requestData: ContractRequestData) : Promise<string>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | int | Yes | Indicates the card slot index number. |
| requestData | [ContractRequestData](arkts-telephony-esim-contractrequestdata-i-sys.md) | Yes | request infomation required to get contract infomation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Returns the contract info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) | System internal error. |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) | Service connection failed. |

**Examples**

```TypeScript
import { eSIM } from '@kit.TelephonyKit';
try {
    let request: eSIM.ContractRequestData = {
        publicKey: "",
        nonce: "",
        pkid: ""
    }
    let contractInfo: string = await eSIM.getContractInfo(1, request);
    console.info(`contract info is:` + contractInfo);
} catch (err) {
    console.error(`getContractInfo, promise: err->${JSON.stringify(err)}`)
}
```

