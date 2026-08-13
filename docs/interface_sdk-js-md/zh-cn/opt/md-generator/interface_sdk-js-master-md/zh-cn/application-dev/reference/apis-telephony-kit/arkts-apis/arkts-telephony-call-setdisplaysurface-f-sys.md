# setDisplaySurface（系统接口）

## setDisplaySurface

```TypeScript
function setDisplaySurface(callId: number, surfaceId: string): Promise<void>
```

设置远端画面窗口。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setDisplaySurface(callId: int, surfaceId: string): Promise<void>--><!--Device-call-function setDisplaySurface(callId: int, surfaceId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callId | number | 是 |
| surfaceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

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

call.setDisplaySurface(1, "surfaceId1").then(() => {
    console.info(`setDisplaySurface success.`);
}).catch((err: BusinessError) => {
    console.error(`setDisplaySurface fail, promise: err->${JSON.stringify(err)}`);
});
```
