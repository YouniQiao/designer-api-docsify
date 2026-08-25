# reportAVScreenCaptureUserChoice（系统接口）

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## reportAVScreenCaptureUserChoice

```TypeScript
function reportAVScreenCaptureUserChoice(sessionId: number, choice: string): Promise<void>
```

Reports the user selection result in the screen capture privacy dialog box to the AVScreenCapture server to determine whether to start screen capture. Screen capture starts only when the user touches a button to continue the operation. This API is called by the system application that creates the dialog box.

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | number | 是 |
| choice | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
