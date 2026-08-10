# getOperatorConfigs（系统接口）

## 导入模块

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getOperatorConfigs

```TypeScript
function getOperatorConfigs(slotId: int, callback: AsyncCallback<Array<OperatorConfig>>): void
```

Obtains the operatorconfigs of the SIM card in a specified slot.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getOperatorConfigs(slotId: int, callback: AsyncCallback<Array<OperatorConfig>>): void--><!--Device-sim-function getOperatorConfigs(slotId: int, callback: AsyncCallback<Array<OperatorConfig>>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;OperatorConfig&gt;&gt; | 是 | Indicates the callback for getting the operatorconfigs in a specified slot; returns empty OperatorConfig if no SIM card is inserted. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getOperatorConfigs(0, (err: BusinessError, data: Array<sim.OperatorConfig>) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getOperatorConfigs

```TypeScript
function getOperatorConfigs(slotId: int): Promise<Array<OperatorConfig>>
```

Obtains the operatorconfigs of the SIM card in a specified slot.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getOperatorConfigs(slotId: int): Promise<Array<OperatorConfig>>--><!--Device-sim-function getOperatorConfigs(slotId: int): Promise<Array<OperatorConfig>>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;OperatorConfig&gt;&gt; | Returns the operatorconfigs in a specified slot; returns empty OperatorConfig if no SIM card is inserted. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getOperatorConfigs(0).then((data: Array<sim.OperatorConfig>) => {
    console.info(`getOperatorConfigs success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getOperatorConfigs failed, promise: err->${JSON.stringify(err)}`);
});
```

