# ScreenCaptureMonitor（系统接口）

A class that provides APIs to query and monitor the system screen recorder status. Before calling any API, you must use getScreenCaptureMonitor() to obtain a ScreenCaptureMonitor instance.

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## off('systemScreenRecorder')

```TypeScript
off(type: 'systemScreenRecorder', callback?: Callback<ScreenCaptureEvent>): void
```

Unsubscribes from state change events of the system screen recorder.

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'systemScreenRecorder' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ScreenCaptureEvent](arkts-media-media-screencaptureevent-e-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## on('systemScreenRecorder')

```TypeScript
on(type: 'systemScreenRecorder', callback: Callback<ScreenCaptureEvent>): void
```

Subscribes to state change events of the system screen recorder. From the ScreenCaptureEvent event reported, you can determine whether the system screen recorder is working.

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'systemScreenRecorder' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ScreenCaptureEvent](arkts-media-media-screencaptureevent-e-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## isSystemScreenRecorderWorking

```TypeScript
readonly isSystemScreenRecorderWorking: boolean
```

Whether the system screen recorder is working.

**类型：** boolean

**起始版本：** 18

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**系统接口：** 此接口为系统接口。
