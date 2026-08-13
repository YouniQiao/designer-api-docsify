# setVoNRState（系统接口）

## setVoNRState

```TypeScript
function setVoNRState(slotId: number, state: VoNRState, callback: AsyncCallback<void>): void
```

设置NR语音的开关状态。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setVoNRState(slotId: int, state: VoNRState, callback: AsyncCallback<void>): void--><!--Device-call-function setVoNRState(slotId: int, state: VoNRState, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| state | [VoNRState](arkts-telephony-call-vonrstate-e-sys.md) | 是 |
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

let slotId: number = 0;
let state: call.VoNRState = call.VoNRState.VONR_STATE_ON;
call.setVoNRState(slotId, state, (err: BusinessError) => {
    if (err) {
        console.error(`setVoNRState fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`setVoNRState success`);
    }
});
```


## setVoNRState

```TypeScript
function setVoNRState(slotId: number, state: VoNRState): Promise<void>
```

设置NR语音的开关状态。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setVoNRState(slotId: int, state: VoNRState): Promise<void>--><!--Device-call-function setVoNRState(slotId: int, state: VoNRState): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| state | [VoNRState](arkts-telephony-call-vonrstate-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

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

let slotId: number = 0;
let state: call.VoNRState = call.VoNRState.VONR_STATE_ON;
call.setVoNRState(slotId, state).then(() => {
    console.info(`setVoNRState success`);
}).catch((err: BusinessError) => {
    console.error(`setVoNRState fail, promise: err->${JSON.stringify(err)}`);
});
```
