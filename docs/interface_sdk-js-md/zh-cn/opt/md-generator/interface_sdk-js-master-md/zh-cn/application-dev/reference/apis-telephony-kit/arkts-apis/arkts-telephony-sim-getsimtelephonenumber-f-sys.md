# getSimTelephoneNumber（系统接口）

## getSimTelephoneNumber

```TypeScript
function getSimTelephoneNumber(slotId: number, callback: AsyncCallback<string>): void
```

Obtains the MSISDN of the SIM card in a specified slot. The MSISDN is recorded in the EFMSISDN file of the SIM card.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_PHONE_NUMBERS

<!--Device-sim-function getSimTelephoneNumber(slotId: int, callback: AsyncCallback<string>): void--><!--Device-sim-function getSimTelephoneNumber(slotId: int, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
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

sim.getSimTelephoneNumber(0, (err: BusinessError, data: string) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getSimTelephoneNumber

```TypeScript
function getSimTelephoneNumber(slotId: number): Promise<string>
```

Obtains the MSISDN of the SIM card in a specified slot. The MSISDN is recorded in the EFMSISDN file of the SIM card.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_PHONE_NUMBERS

<!--Device-sim-function getSimTelephoneNumber(slotId: int): Promise<string>--><!--Device-sim-function getSimTelephoneNumber(slotId: int): Promise<string>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
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

sim.getSimTelephoneNumber(0).then((data: string) => {
    console.info(`getSimTelephoneNumber success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimTelephoneNumber failed, promise: err->${JSON.stringify(err)}`);
});
```
