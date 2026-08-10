# getRadioTechSync

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## getRadioTechSync

```TypeScript
function getRadioTechSync(slotId: int): NetworkRadioTech
```

Obtains radio access technology (RAT) of the registered network.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-radio-function getRadioTechSync(slotId: int): NetworkRadioTech--><!--Device-radio-function getRadioTechSync(slotId: int): NetworkRadioTech-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NetworkRadioTech](arkts-telephony-radio-networkradiotech-i.md) | Returns the RAT of PS domain and CS domain of registered network. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error code. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

