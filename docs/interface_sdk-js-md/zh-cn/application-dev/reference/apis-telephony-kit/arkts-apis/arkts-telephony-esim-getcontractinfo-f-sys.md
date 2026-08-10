# getContractInfo（系统接口）

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## getContractInfo

```TypeScript
function getContractInfo(slotId: int, requestData: ContractRequestData) : Promise<string>
```

Get contract info

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function getContractInfo(slotId: int, requestData: ContractRequestData) : Promise<string>--><!--Device-eSIM-function getContractInfo(slotId: int, requestData: ContractRequestData) : Promise<string>-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number. |
| requestData | [ContractRequestData](arkts-telephony-esim-contractrequestdata-i-sys.md) | 是 | request infomation required to get contract infomation. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Returns the contract info. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 3120002 | System internal error. |
| 3120001 | Service connection failed. |

## 示例

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

