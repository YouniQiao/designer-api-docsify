# sendTerminalResponseCmd（系统接口）

## sendTerminalResponseCmd

```TypeScript
function sendTerminalResponseCmd(slotId: number, cmd: string, callback: AsyncCallback<void>): void
```

Send terminal response command to SIM card.

**起始版本：** 8

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function sendTerminalResponseCmd(slotId: int, cmd: string, callback: AsyncCallback<void>): void--><!--Device-sim-function sendTerminalResponseCmd(slotId: int, cmd: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| cmd | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
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

sim.sendTerminalResponseCmd(0, "ls", (err: BusinessError) => {
    console.info(`callback: err->${JSON.stringify(err)}`);
});
```


## sendTerminalResponseCmd

```TypeScript
function sendTerminalResponseCmd(slotId: number, cmd: string): Promise<void>
```

Send terminal response command to SIM card.

**起始版本：** 8

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function sendTerminalResponseCmd(slotId: int, cmd: string): Promise<void>--><!--Device-sim-function sendTerminalResponseCmd(slotId: int, cmd: string): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| cmd | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
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

sim.sendTerminalResponseCmd(0, "ls").then(() => {
    console.info(`sendTerminalResponseCmd success.`);
}).catch((err: BusinessError) => {
    console.error(`sendTerminalResponseCmd failed, promise: err->${JSON.stringify(err)}`);
});
```
