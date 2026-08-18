# muteRinger（系统接口）

## 导入模块

```TypeScript
```

## muteRinger

```TypeScript
function muteRinger(callback: AsyncCallback<void>): void
```

如果来电铃声响起，设备将停止铃声。否则，此方法不起作用。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function muteRinger(callback: AsyncCallback<void>): void--><!--Device-call-function muteRinger(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.muteRinger((err: BusinessError) => {
    if (err) {
        console.error(`muteRinger fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`muteRinger success.`);
    }
});
```


## muteRinger

```TypeScript
function muteRinger(): Promise<void>
```

如果来电铃声响起，设备将停止铃声。否则，此方法不起作用。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function muteRinger(): Promise<void>--><!--Device-call-function muteRinger(): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.muteRinger().then(() => {
    console.info(`muteRinger success.`);
}).catch((err: BusinessError) => {
    console.error(`muteRinger fail, promise: err->${JSON.stringify(err)}`);
});
```
