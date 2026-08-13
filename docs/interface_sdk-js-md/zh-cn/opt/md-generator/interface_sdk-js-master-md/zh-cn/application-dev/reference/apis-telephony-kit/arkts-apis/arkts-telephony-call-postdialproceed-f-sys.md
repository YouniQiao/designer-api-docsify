# postDialProceed（系统接口）

## postDialProceed

```TypeScript
function postDialProceed(callId: number, proceed: boolean, callback: AsyncCallback<void>): void
```

继续进行通话。使用callback异步回调。

当用户呼叫号码为：“普通电话号码”+“;”+"DTMF字符"(例如：“400xxxxxxx;123”)，并且已经订阅了通话后延迟事件，电话接通后，系统将上报通话后延迟事件，应用可以调用此接口选择是否发送DTMF音。

**起始版本：** 11

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function postDialProceed(callId: int, proceed: boolean, callback: AsyncCallback<void>): void--><!--Device-call-function postDialProceed(callId: int, proceed: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callId | number | 是 |
| proceed | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.postDialProceed(1, true, (err: BusinessError) => {
    console.info(`callback: err->${JSON.stringify(err)}`);
});
```


## postDialProceed

```TypeScript
function postDialProceed(callId: number, proceed: boolean): Promise<void>
```

继续进行通话。使用Promise异步回调。

当用户呼叫号码为：“普通电话号码”+“;”+"DTMF字符"(例如：“400xxxxxxx;123”)，并且已经订阅了通话后延迟事件，电话接通后，系统将上报通话后延迟事件，应用可以调用此接口选择是否发送DTMF音。

**起始版本：** 11

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function postDialProceed(callId: int, proceed: boolean): Promise<void>--><!--Device-call-function postDialProceed(callId: int, proceed: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callId | number | 是 |
| proceed | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.postDialProceed(1, true).then(() => {
    console.info(`postDialProceed success.`);
}).catch((err: BusinessError) => {
    console.error(`postDialProceed fail, promise: err->${JSON.stringify(err)}`);
});
```
