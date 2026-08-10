# setDefaultVoiceSlotId（系统接口）

## 导入模块

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## setDefaultVoiceSlotId

```TypeScript
function setDefaultVoiceSlotId(slotId: int, callback: AsyncCallback<void>): void
```

Set the card slot ID of the default voice service.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function setDefaultVoiceSlotId(slotId: int, callback: AsyncCallback<void>): void--><!--Device-sim-function setDefaultVoiceSlotId(slotId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The callback of setDefaultVoiceSlotId. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8301001 | SIM card is not activated. |
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

sim.setDefaultVoiceSlotId(0, (err: BusinessError) => {
    console.info(`callback: err->${JSON.stringify(err)}`);
});
```


## setDefaultVoiceSlotId

```TypeScript
function setDefaultVoiceSlotId(slotId: int): Promise<void>
```

Set the card slot ID of the default voice service.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function setDefaultVoiceSlotId(slotId: int): Promise<void>--><!--Device-sim-function setDefaultVoiceSlotId(slotId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the setVoiceMailInfo. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8301001 | SIM card is not activated. |
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

sim.setDefaultVoiceSlotId(0).then(() => {
    console.info(`setDefaultVoiceSlotId success.`);
}).catch((err: BusinessError) => {
    console.error(`setDefaultVoiceSlotId failed, promise: err->${JSON.stringify(err)}`);
});
```

