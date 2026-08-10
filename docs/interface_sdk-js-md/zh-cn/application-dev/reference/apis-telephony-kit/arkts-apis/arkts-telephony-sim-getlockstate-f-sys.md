# getLockState（系统接口）

## 导入模块

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getLockState

```TypeScript
function getLockState(slotId: int, lockType: LockType, callback: AsyncCallback<LockState>): void
```

Get the lock status of the SIM card in the specified slot.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getLockState(slotId: int, lockType: LockType, callback: AsyncCallback<LockState>): void--><!--Device-sim-function getLockState(slotId: int, lockType: LockType, callback: AsyncCallback<LockState>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| lockType | [LockType](arkts-telephony-sim-locktype-e-sys.md) | 是 | Indicates the lock type. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;LockState&gt; | 是 | Indicates the callback for getting the sim card lock status. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8301002 | The SIM card failed to read or update data. |
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

sim.getLockState(0, 1, (err: BusinessError, data: sim.LockState) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getLockState

```TypeScript
function getLockState(slotId: int, lockType: LockType): Promise<LockState>
```

Get the lock status of the SIM card in the specified slot.

**起始版本：** 8

**ArkTS模式：** ArkTS-Dyn起始版本为8；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getLockState(slotId: int, lockType: LockType): Promise<LockState>--><!--Device-sim-function getLockState(slotId: int, lockType: LockType): Promise<LockState>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| lockType | [LockType](arkts-telephony-sim-locktype-e-sys.md) | 是 | Indicates the lock type. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;LockState&gt; | Returns the sim card lock status. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8301002 | The SIM card failed to read or update data. |
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

sim.getLockState(0, 1).then((data: sim.LockState) => {
    console.info(`getLockState success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getLockState failed, promise: err->${JSON.stringify(err)}`);
});
```

