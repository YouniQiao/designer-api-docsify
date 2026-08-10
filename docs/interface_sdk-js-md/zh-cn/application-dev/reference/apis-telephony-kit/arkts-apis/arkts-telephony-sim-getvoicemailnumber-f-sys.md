# getVoiceMailNumber（系统接口）

## 导入模块

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getVoiceMailNumber

```TypeScript
function getVoiceMailNumber(slotId: int, callback: AsyncCallback<string>): void
```

Obtains the voice mailbox number of the SIM card in a specified slot.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getVoiceMailNumber(slotId: int, callback: AsyncCallback<string>): void--><!--Device-sim-function getVoiceMailNumber(slotId: int, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from {@code 0} to the maximum card slot index number supported by the device. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 | Indicates the callback for getting the voice mailbox number; returns an empty string if no voice mailbox number is written into the SIM card. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300004 | No SIM card found. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getVoiceMailNumber(0, (err: BusinessError, data: string) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getVoiceMailNumber

```TypeScript
function getVoiceMailNumber(slotId: int): Promise<string>
```

Obtains the voice mailbox number of the SIM card in a specified slot.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getVoiceMailNumber(slotId: int): Promise<string>--><!--Device-sim-function getVoiceMailNumber(slotId: int): Promise<string>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from {@code 0} to the maximum card slot index number supported by the device. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Returns the voice mailbox number. returns an empty string if no voice mailbox number is written into the SIM card. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300004 | No SIM card found. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getVoiceMailNumber(0).then((data: string) => {
    console.info(`getVoiceMailNumber success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getVoiceMailNumber failed, promise: err->${JSON.stringify(err)}`);
});
```

