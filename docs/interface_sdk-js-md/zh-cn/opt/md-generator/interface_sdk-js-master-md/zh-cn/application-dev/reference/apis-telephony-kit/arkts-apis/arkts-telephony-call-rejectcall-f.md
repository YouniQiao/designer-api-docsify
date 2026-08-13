# rejectCall

## rejectCall

```TypeScript
function rejectCall(callback: AsyncCallback<void>): void
```

拒绝来电。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ANSWER_CALL or ohos.permission.MANAGE_CALL_FOR_DEVICES

<!--Device-call-function rejectCall(callback: AsyncCallback<void>): void--><!--Device-call-function rejectCall(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

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
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.rejectCall((err: BusinessError) => {
    if (err) {
        console.error(`rejectCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`rejectCall success.`);
    }
});
```
