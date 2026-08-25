# getScreenCaptureMonitor（系统接口）

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## getScreenCaptureMonitor

```TypeScript
function getScreenCaptureMonitor(): Promise<ScreenCaptureMonitor>
```

Obtains a **ScreenCaptureMonitor** instance. This API uses a promise to return the result.

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ScreenCaptureMonitor](arkts-media-media-screencapturemonitor-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
