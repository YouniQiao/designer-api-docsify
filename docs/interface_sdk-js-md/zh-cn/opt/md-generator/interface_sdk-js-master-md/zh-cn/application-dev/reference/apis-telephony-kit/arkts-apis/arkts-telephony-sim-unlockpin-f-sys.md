# unlockPin（系统接口）

## unlockPin

```TypeScript
function unlockPin(slotId: number, pin: string, callback: AsyncCallback<LockStatusResponse>): void
```

Unlock the SIM card password of the specified card slot.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function unlockPin(slotId: int, pin: string, callback: AsyncCallback<LockStatusResponse>): void--><!--Device-sim-function unlockPin(slotId: int, pin: string, callback: AsyncCallback<LockStatusResponse>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| pin | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[LockStatusResponse](arkts-telephony-sim-lockstatusresponse-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8301002](../errorcode-telephony.md#8301002-sim卡读取数据或者更新数据失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let pin: string = '1234';
sim.unlockPin(0, pin, (err: BusinessError, data: sim.LockStatusResponse) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## unlockPin

```TypeScript
function unlockPin(slotId: number, pin: string): Promise<LockStatusResponse>
```

Unlock the SIM card password of the specified card slot.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function unlockPin(slotId: int, pin: string): Promise<LockStatusResponse>--><!--Device-sim-function unlockPin(slotId: int, pin: string): Promise<LockStatusResponse>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| pin | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[LockStatusResponse](arkts-telephony-sim-lockstatusresponse-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8301002](../errorcode-telephony.md#8301002-sim卡读取数据或者更新数据失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let pin: string = '1234';
sim.unlockPin(0, pin).then((data: sim.LockStatusResponse) => {
    console.info(`unlockPin success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`unlockPin failed, promise: err->${JSON.stringify(err)}`);
});
```
