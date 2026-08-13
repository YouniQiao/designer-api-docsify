# removeMissedIncomingCallNotification（系统接口）

## removeMissedIncomingCallNotification

```TypeScript
function removeMissedIncomingCallNotification(callback: AsyncCallback<void>): void
```

删除未接来电通知。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.SET_TELEPHONY_STATE and ohos.permission.READ_CALL_LOG and ohos.permission.WRITE_CALL_LOG

<!--Device-call-function removeMissedIncomingCallNotification(callback: AsyncCallback<void>): void--><!--Device-call-function removeMissedIncomingCallNotification(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.removeMissedIncomingCallNotification((err: BusinessError) => {
    if (err) {
        console.error(`removeMissedIncomingCallNotification failed, err->${JSON.stringify(err)}`);
    } else {
        console.info(`removeMissedIncomingCallNotification success`);
    }
});
```


## removeMissedIncomingCallNotification

```TypeScript
function removeMissedIncomingCallNotification(): Promise<void>
```

删除未接来电通知。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.SET_TELEPHONY_STATE and ohos.permission.READ_CALL_LOG and ohos.permission.WRITE_CALL_LOG

<!--Device-call-function removeMissedIncomingCallNotification(): Promise<void>--><!--Device-call-function removeMissedIncomingCallNotification(): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.removeMissedIncomingCallNotification().then(() => {
    console.info(`removeMissedIncomingCallNotification success`);
}).catch((err: BusinessError) => {
    console.error(`removeMissedIncomingCallNotification failed, promise: err->${JSON.stringify(err)}`);
});
```
