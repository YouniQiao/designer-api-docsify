# sendUssdResponse（系统接口）

## sendUssdResponse

```TypeScript
function sendUssdResponse(slotId: number, content: string): void
```

用于向运营商发送USSD业务（Unstructured Supplementary Service Data，非结构化补充数据业务）的响应消息。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function sendUssdResponse(slotId: int, content: string): void--><!--Device-call-function sendUssdResponse(slotId: int, content: string): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| content | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { call } from '@kit.TelephonyKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

function testSendUssdResponse() {
    const slotId: number = 0;
    const content: string = "OK";

    try {
        call.sendUssdResponse(slotId, content);
    } catch (error) {
        const err = error as BusinessError;
        hilog.error(0x0000, 'testTag', `Failed to send USSD response. Code: ${err.code}, Message: ${err.message}`);
    }
}
```
