# makeDirectCall

## 导入模块

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## makeDirectCall

```TypeScript
function makeDirectCall(phoneNumber: string): Promise<void>
```

应用一键拨打电话。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.DIRECT_CALL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-call-function makeDirectCall(phoneNumber: string): Promise<void>--><!--Device-call-function makeDirectCall(phoneNumber: string): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | 电话号码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission denied. |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) | Invalid parameter value. |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) | Operation failed. Cannot connect to service. |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) | System internal error. |
| [8300005](../errorcode-telephony.md#8300005-飞行模式已开启) | Airplane mode is on. |
| [8300006](../errorcode-telephony.md#8300006-网络无服务) | Network not in service. |

**示例**

```TypeScript
import { call } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';
call.makeDirectCall("138xxxxxxxx").then(() => {
    console.info(`makeDirectCall success`);
}).catch((err: BusinessError) => {
    console.error(`makeDirectCall fail, promise: err->Code${err.code}, message:${err.message}`);
});
```
