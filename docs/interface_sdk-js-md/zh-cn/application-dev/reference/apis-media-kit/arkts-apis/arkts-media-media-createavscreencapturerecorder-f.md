# createAVScreenCaptureRecorder

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createAVScreenCaptureRecorder

```TypeScript
function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder>
```

创建屏幕录制实例，使用Promise异步回调。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AVScreenCaptureRecorder](arkts-media-media-avscreencapturerecorder-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../errorcode-media.md#5400101-内存分配失败) |
