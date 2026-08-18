# unHoldCall（系统接口）

## 导入模块

```TypeScript
```

## unHoldCall

```TypeScript
function unHoldCall(callId: number, callback: AsyncCallback<void>): void
```

取消保持通话。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ANSWER_CALL

<!--Device-call-function unHoldCall(callId: int, callback: AsyncCallback<void>): void--><!--Device-call-function unHoldCall(callId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.unHoldCall(1, (err: BusinessError) => {
    if (err) {
        console.error(`unHoldCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`unHoldCall success.`);
    }
});
```


## unHoldCall

```TypeScript
function unHoldCall(callId: number): Promise<void>
```

取消保持通话。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ANSWER_CALL

<!--Device-call-function unHoldCall(callId: int): Promise<void>--><!--Device-call-function unHoldCall(callId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.unHoldCall(1).then(() => {
    console.info(`unHoldCall success.`);
}).catch((err: BusinessError) => {
    console.error(`unHoldCall fail, promise: err->${JSON.stringify(err)}`);
});
```
