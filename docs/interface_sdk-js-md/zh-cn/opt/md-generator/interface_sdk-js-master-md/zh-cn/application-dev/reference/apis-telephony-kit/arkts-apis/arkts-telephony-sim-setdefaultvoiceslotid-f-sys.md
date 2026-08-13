# setDefaultVoiceSlotId（系统接口）

## setDefaultVoiceSlotId

```TypeScript
function setDefaultVoiceSlotId(slotId: number, callback: AsyncCallback<void>): void
```

Set the card slot ID of the default voice service.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function setDefaultVoiceSlotId(slotId: int, callback: AsyncCallback<void>): void--><!--Device-sim-function setDefaultVoiceSlotId(slotId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8301001](../errorcode-telephony.md#8301001-sim卡未激活) |
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

sim.setDefaultVoiceSlotId(0, (err: BusinessError) => {
    console.info(`callback: err->${JSON.stringify(err)}`);
});
```


## setDefaultVoiceSlotId

```TypeScript
function setDefaultVoiceSlotId(slotId: number): Promise<void>
```

Set the card slot ID of the default voice service.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function setDefaultVoiceSlotId(slotId: int): Promise<void>--><!--Device-sim-function setDefaultVoiceSlotId(slotId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8301001](../errorcode-telephony.md#8301001-sim卡未激活) |
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

sim.setDefaultVoiceSlotId(0).then(() => {
    console.info(`setDefaultVoiceSlotId success.`);
}).catch((err: BusinessError) => {
    console.error(`setDefaultVoiceSlotId failed, promise: err->${JSON.stringify(err)}`);
});
```
