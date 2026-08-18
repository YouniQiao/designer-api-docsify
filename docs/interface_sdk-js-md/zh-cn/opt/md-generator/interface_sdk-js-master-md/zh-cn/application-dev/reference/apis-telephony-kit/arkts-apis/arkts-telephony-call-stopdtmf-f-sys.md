# stopDTMF（系统接口）

## 导入模块

```TypeScript
```

## stopDTMF

```TypeScript
function stopDTMF(callId: number, callback: AsyncCallback<void>): void
```

停止双音多频。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function stopDTMF(callId: int, callback: AsyncCallback<void>): void--><!--Device-call-function stopDTMF(callId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.stopDTMF(1, (err: BusinessError) => {
    if (err) {
        console.error(`stopDTMF fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`stopDTMF success.`);
    }
});
```


## stopDTMF

```TypeScript
function stopDTMF(callId: number): Promise<void>
```

停止双音多频。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function stopDTMF(callId: int): Promise<void>--><!--Device-call-function stopDTMF(callId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.stopDTMF(1).then(() => {
    console.info(`stopDTMF success.`);
}).catch((err: BusinessError) => {
    console.error(`stopDTMF fail, promise: err->${JSON.stringify(err)}`);
});
```
