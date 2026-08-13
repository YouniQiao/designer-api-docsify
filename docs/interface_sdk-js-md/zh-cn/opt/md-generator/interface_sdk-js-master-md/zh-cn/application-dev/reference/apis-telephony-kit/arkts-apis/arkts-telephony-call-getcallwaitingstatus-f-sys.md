# getCallWaitingStatus（系统接口）

## getCallWaitingStatus

```TypeScript
function getCallWaitingStatus(slotId: number, callback: AsyncCallback<CallWaitingStatus>): void
```

获取呼叫等待状态。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-call-function getCallWaitingStatus(slotId: int, callback: AsyncCallback<CallWaitingStatus>): void--><!--Device-call-function getCallWaitingStatus(slotId: int, callback: AsyncCallback<CallWaitingStatus>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CallWaitingStatus](arkts-telephony-call-callwaitingstatus-e-sys.md)&gt; | 是 |

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

call.getCallWaitingStatus(0, (err: BusinessError, data: call.CallWaitingStatus) => {
    if (err) {
        console.error(`getCallWaitingStatus fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`getCallWaitingStatus success, data->${JSON.stringify(data)}`);
    }
});
```


## getCallWaitingStatus

```TypeScript
function getCallWaitingStatus(slotId: number): Promise<CallWaitingStatus>
```

获取呼叫等待状态。使用Promise异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-call-function getCallWaitingStatus(slotId: int): Promise<CallWaitingStatus>--><!--Device-call-function getCallWaitingStatus(slotId: int): Promise<CallWaitingStatus>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CallWaitingStatus](arkts-telephony-call-callwaitingstatus-e-sys.md)&gt; |

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

call.getCallWaitingStatus(0).then((data: call.CallWaitingStatus) => {
    console.info(`getCallWaitingStatus success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getCallWaitingStatus fail, promise: err->${JSON.stringify(err)}`);
});
```
