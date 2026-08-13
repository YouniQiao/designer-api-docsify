# answerCall（系统接口）

## answerCall

```TypeScript
function answerCall(callId: int, callback: AsyncCallback<void>): void
```

接听来电。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ANSWER_CALL

<!--Device-call-function answerCall(callId: int, callback: AsyncCallback<void>): void--><!--Device-call-function answerCall(callId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 呼叫Id。可以通过订阅callDetailsChange事件获得。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 以回调函数的方式返回接听电话的结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.answerCall(1, (err: BusinessError) => {
    if (err) {
        console.error(`answerCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`answerCall success.`);
    }
});
```


## answerCall

```TypeScript
function answerCall(callId?: int): Promise<void>
```

接听来电。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ANSWER_CALL

<!--Device-call-function answerCall(callId?: int): Promise<void>--><!--Device-call-function answerCall(callId?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 否 | 呼叫Id。可以通过订阅callDetailsChange事件获得。从API version 9开始为可选参数。&lt;br/&gt;不填该参数则接通最近一通正在响铃的来电。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 以Promise形式异步返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.answerCall(1).then(() => {
    console.info(`answerCall success.`);
}).catch((err: BusinessError) => {
    console.error(`answerCall fail, promise: err->${JSON.stringify(err)}`);
});
```


## answerCall

```TypeScript
function answerCall(videoState: VideoStateType, callId: int): Promise<void>
```

接听来电。使用Promise异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ANSWER_CALL

<!--Device-call-function answerCall(videoState: VideoStateType, callId: int): Promise<void>--><!--Device-call-function answerCall(videoState: VideoStateType, callId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| videoState | [VideoStateType](arkts-telephony-call-videostatetype-e-sys.md) | 是 | 接听通话类型。 |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 呼叫Id。可以通过订阅callDetailsChange事件获得。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 以Promise形式异步返回接听电话结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [8300999](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) | Unknown error code. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Non-system applications use system APIs. |
| [8300002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) | Operation failed. Cannot connect to service. |
| [8300003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) | System internal error. |
| [8300001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) | Invalid parameter value. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.answerCall(0, 1).then(() => {
    console.info(`answerCall success.`);
}).catch((err: BusinessError) => {
    console.error(`answerCall fail, promise: err->${JSON.stringify(err)}`);
});
```


## answerCall

```TypeScript
function answerCall(videoState: VideoStateType, callId: int, isRtt: boolean): Promise<void>
```

接听rtt来电

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.ANSWER_CALL

<!--Device-call-function answerCall(videoState: VideoStateType, callId: int, isRtt: boolean): Promise<void>--><!--Device-call-function answerCall(videoState: VideoStateType, callId: int, isRtt: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| videoState | [VideoStateType](arkts-telephony-call-videostatetype-e-sys.md) | 是 | Indicates the answer the call with video or voice. |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the identifier of the call to answer. |
| isRtt | boolean | 是 | Indicates the call is rtt or not. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the answerCall. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 8400001 | Invalid parameter value. |
| 8400002 | Operation failed. Cannot connect to service. |
| 8400003 | System internal error. |
| 8400999 | Unknown error code. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Non-system applications use system APIs. |

