# getVoNRState（系统接口）

## getVoNRState

```TypeScript
function getVoNRState(slotId: number, callback: AsyncCallback<VoNRState>): void
```

查询NR语音的开关状态。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-call-function getVoNRState(slotId: int, callback: AsyncCallback<VoNRState>): void--><!--Device-call-function getVoNRState(slotId: int, callback: AsyncCallback<VoNRState>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[VoNRState](arkts-telephony-call-vonrstate-e-sys.md)&gt; | 是 |

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

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
call.getVoNRState(slotId, (err: BusinessError, data: call.VoNRState) => {
    if (err) {
        console.error(`getVoNRState fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`getVoNRState success, data->${JSON.stringify(data)}`);
    }
});
```


## getVoNRState

```TypeScript
function getVoNRState(slotId: number): Promise<VoNRState>
```

查询NR语音的开关状态。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-call-function getVoNRState(slotId: int): Promise<VoNRState>--><!--Device-call-function getVoNRState(slotId: int): Promise<VoNRState>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[VoNRState](arkts-telephony-call-vonrstate-e-sys.md)&gt; |

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

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
call.getVoNRState(slotId).then((data: call.VoNRState) => {
    console.info(`getVoNRState success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getVoNRState fail, promise: err->${JSON.stringify(err)}`);
});
```
