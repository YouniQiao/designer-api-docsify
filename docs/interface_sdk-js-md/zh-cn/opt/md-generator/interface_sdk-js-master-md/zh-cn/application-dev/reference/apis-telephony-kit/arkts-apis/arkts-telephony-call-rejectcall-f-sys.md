# rejectCall（系统接口）

## 导入模块

```TypeScript
```

## rejectCall

```TypeScript
function rejectCall(callId: number, options: RejectMessageOptions, callback: AsyncCallback<void>): void
```

拒绝来电。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ANSWER_CALL

<!--Device-call-function rejectCall(callId: int, options: RejectMessageOptions, callback: AsyncCallback<void>): void--><!--Device-call-function rejectCall(callId: int, options: RejectMessageOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callId | number | 是 |
| options | [RejectMessageOptions](arkts-telephony-call-rejectmessageoptions-i-sys.md) | 是 |
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

let rejectMessageOptions : call.RejectMessageOptions = {
    messageContent: "拦截陌生号码"
}
call.rejectCall(1, rejectMessageOptions, (err: BusinessError) => {
    if (err) {
        console.error(`rejectCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`rejectCall success.`);
    }
});
```


## rejectCall

```TypeScript
function rejectCall(callId?: number, options?: RejectMessageOptions): Promise<void>
```

拒绝来电。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ANSWER_CALL

<!--Device-call-function rejectCall(callId?: int, options?: RejectMessageOptions): Promise<void>--><!--Device-call-function rejectCall(callId?: int, options?: RejectMessageOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callId | number | 否 |
| options | [RejectMessageOptions](arkts-telephony-call-rejectmessageoptions-i-sys.md) | 否 |

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

let rejectMessageOptions: call.RejectMessageOptions = {
    messageContent: "拦截陌生号码"
}
call.rejectCall(1, rejectMessageOptions).then(() => {
    console.info(`rejectCall success.`);
}).catch((err: BusinessError) => {
    console.error(`rejectCall fail, promise: err->${JSON.stringify(err)}`);
});
```


## rejectCall

```TypeScript
function rejectCall(callId: number, callback: AsyncCallback<void>): void
```

拒绝来电。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ANSWER_CALL

<!--Device-call-function rejectCall(callId: int, callback: AsyncCallback<void>): void--><!--Device-call-function rejectCall(callId: int, callback: AsyncCallback<void>): void-End-->

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

call.rejectCall(1, (err: BusinessError) => {
    if (err) {
        console.error(`rejectCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`rejectCall success.`);
    }
});
```


## rejectCall

```TypeScript
function rejectCall(callback: AsyncCallback<void>): void
```

拒绝来电。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ANSWER_CALL or ohos.permission.MANAGE_CALL_FOR_DEVICES

<!--Device-call-function rejectCall(callback: AsyncCallback<void>): void--><!--Device-call-function rejectCall(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
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

call.rejectCall((err: BusinessError) => {
    if (err) {
        console.error(`rejectCall fail, err->Code${err.code}, message:${err.message}`);
    } else {
        console.info(`rejectCall success.`);
    }
});
```


## rejectCall

```TypeScript
function rejectCall(options: RejectMessageOptions, callback: AsyncCallback<void>): void
```

拒绝来电。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ANSWER_CALL

<!--Device-call-function rejectCall(options: RejectMessageOptions, callback: AsyncCallback<void>): void--><!--Device-call-function rejectCall(options: RejectMessageOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RejectMessageOptions](arkts-telephony-call-rejectmessageoptions-i-sys.md) | 是 |
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

let rejectMessageOptions: call.RejectMessageOptions = {
    messageContent: "拦截陌生号码"
}
call.rejectCall(rejectMessageOptions, (err: BusinessError) => {
    if (err) {
        console.error(`rejectCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`rejectCall success.`);
    }
});
```
