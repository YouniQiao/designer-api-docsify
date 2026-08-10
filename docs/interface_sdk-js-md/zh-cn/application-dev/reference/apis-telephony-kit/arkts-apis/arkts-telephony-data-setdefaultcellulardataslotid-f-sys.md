# setDefaultCellularDataSlotId（系统接口）

## 导入模块

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## setDefaultCellularDataSlotId

```TypeScript
function setDefaultCellularDataSlotId(slotId: int, callback: AsyncCallback<void>): void
```

Switch cellular data services to another card, without changing the default settings.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-data-function setDefaultCellularDataSlotId(slotId: int, callback: AsyncCallback<void>): void--><!--Device-data-function setDefaultCellularDataSlotId(slotId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CellularData

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the ID of the target card slot. The value {@code 0} indicates card 1, and the value {@code 1} indicates card 2. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | The callback of setDefaultCellularDataSlotId. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8301001 | SIM card is not activated. |
| 201 | Permission denied. |
| 8300999 | Internal error. |
| 202 | Non-system applications use system APIs. |
| 8300004 | No SIM card found. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.setDefaultCellularDataSlotId(0, (err: BusinessError) => {
    if(err) {
        console.error(`setDefaultCellularDataSlotId fail. code: ${err.code}, message: ${err.message}`);
    } else {
        console.info(`setDefaultCellularDataSlotId success`);
    }
});
```


## setDefaultCellularDataSlotId

```TypeScript
function setDefaultCellularDataSlotId(slotId: int): Promise<void>
```

Switch cellular data services to another card, without changing the default settings.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-data-function setDefaultCellularDataSlotId(slotId: int): Promise<void>--><!--Device-data-function setDefaultCellularDataSlotId(slotId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CellularData

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the ID of the target card slot. The value {@code 0} indicates card 1, and the value {@code 1} indicates card 2. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the setDefaultCellularDataSlotId. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8301001 | SIM card is not activated. |
| 201 | Permission denied. |
| 8300999 | Internal error. |
| 202 | Non-system applications use system APIs. |
| 8300004 | No SIM card found. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.setDefaultCellularDataSlotId(0).then(() => {
    console.info(`setDefaultCellularDataSlotId success.`);
}).catch((err: BusinessError) => {
    console.error(`setDefaultCellularDataSlotId fail. code: ${err.code}, message: ${err.message}`);
});
```

