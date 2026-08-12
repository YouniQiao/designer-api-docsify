# getScreenCaptureMonitor（系统接口）

## getScreenCaptureMonitor

```TypeScript
function getScreenCaptureMonitor(): Promise<ScreenCaptureMonitor>
```

Obtains a **ScreenCaptureMonitor** instance. This API uses a promise to return the result.

**起始版本：** 18

<!--Device-media-function getScreenCaptureMonitor(): Promise<ScreenCaptureMonitor>--><!--Device-media-function getScreenCaptureMonitor(): Promise<ScreenCaptureMonitor>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ScreenCaptureMonitor](arkts-media-multimedia-media-screencapturemonitor-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-内存分配失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
let screenCaptureMonitor: media.ScreenCaptureMonitor;
try {
  screenCaptureMonitor = await media.getScreenCaptureMonitor();
} catch (err) {
  console.error(`getScreenCaptureMonitor failed, error message:${err.message}`);
}
```
