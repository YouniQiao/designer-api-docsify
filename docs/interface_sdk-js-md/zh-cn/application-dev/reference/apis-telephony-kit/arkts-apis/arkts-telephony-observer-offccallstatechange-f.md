# offCCallStateChange

## offCCallStateChange

```TypeScript
function offCCallStateChange(callback?: Callback<CCallStateInfo>): void
```

取消三方应用监听运营商通话状态并获取通话号码，使用callback方式作为异步方法。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.MANAGE_CALL_FOR_DEVICES

<!--Device-observer-function offCCallStateChange(callback?: Callback<CCallStateInfo>): void--><!--Device-observer-function offCCallStateChange(callback?: Callback<CCallStateInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CCallStateInfo](arkts-telephony-observer-ccallstateinfo-i.md)&gt; | 否 | 回调函数，返回通话状态信息对象。&lt;br/&gt;应用可获取到CCallState。&lt;br/&gt; |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [8800999](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800999-内部错误) | Unknown error. |
| [8800002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800002-服务连接失败) | Service connection failed. |
| [8800003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800003-系统内部错误) | System internal error. |
| [8800001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800001-输入参数不在处理范围内) | Invalid parameter value. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. |

## 示例

```TypeScript
import { call, observer } from '@kit.TelephonyKit';

let callback: (data: observer.CCallStateInfo) => void = (data: observer.CCallStateInfo) => {
    console.info("onCCallStateChange, data:" + JSON.stringify(data));
}

observer.offCCallStateChange(callback);
observer.offCCallStateChange();
```

