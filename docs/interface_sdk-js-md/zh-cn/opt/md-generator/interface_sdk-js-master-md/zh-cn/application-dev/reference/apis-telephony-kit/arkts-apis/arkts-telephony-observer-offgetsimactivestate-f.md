# offGetSimActiveState

## offGetSimActiveState

```TypeScript
function offGetSimActiveState(callback?: Callback<boolean>): void
```

取消SIM卡激活状态变化的监听，使用callback方式作为异步方法。

**起始版本：** 23

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-observer-function offGetSimActiveState(callback?: Callback<boolean>): void--><!--Device-observer-function offGetSimActiveState(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let simActiveState: Callback<boolean> = (isSimActive: boolean) => {
    console.info(`simActiveState slotId ${JSON.stringify(isSimActive)}`);
}
observer.offGetSimActiveState(simActiveState);
```
