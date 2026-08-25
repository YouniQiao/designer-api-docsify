# NativeMediaPlayerBridge

NativeMediaPlayerBridge 是[CreateNativeMediaPlayerCallback](arkts-arkweb-webview-createnativemediaplayercallback-t.md)回调函数的返回值类 型，是接管网页媒体的播放器和 ArkWeb 内核之间的一个接口类。ArkWeb 内核通过该接口类的实例对象控制应用创建的用于接管网页媒体的播放器。该接口允许应用使用自定义的媒体播放器接管网页中的媒体内容播放，同时，该接口还支持播放 器的挂起和恢复机制。

**起始版本：** 12

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## enterFullscreen

```TypeScript
enterFullscreen(): void
```

使播放器进入全屏。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## exitFullscreen

```TypeScript
exitFullscreen(): void
```

使播放器退出全屏。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## pause

```TypeScript
pause(): void
```

暂停播放。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## play

```TypeScript
play(): void
```

播放媒体。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## release

```TypeScript
release(): void
```

销毁播放器。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## resumePlayer

```TypeScript
resumePlayer?(): void
```

通知应用重建播放器，并恢复播放器的状态信息。仅与 suspendPlayer 成对出现。

**起始版本：** 12

**系统能力：** SystemCapability.Web.Webview.Core

## seek

```TypeScript
seek(targetTime: number): void
```

跳转播放进度到指定时间点。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetTime | number | 是 |

## setMuted

```TypeScript
setMuted(muted: boolean): void
```

设置静音状态。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| muted | boolean | 是 |

## setPlaybackRate

```TypeScript
setPlaybackRate(playbackRate: number): void
```

设置播放速率。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| playbackRate | number | 是 |

## setVolume

```TypeScript
setVolume(volume: number): void
```

设置播放器音量值。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volume | number | 是 |

## suspendPlayer

```TypeScript
suspendPlayer?(type: SuspendType): void
```

通知应用销毁播放器，并保存播放器的状态信息。仅与 resumePlayer 成对出现。

**起始版本：** 12

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SuspendType](arkts-arkweb-webview-suspendtype-e.md) | 是 |

## updateRect

```TypeScript
updateRect(x: number, y: number, width: number, height: number): void
```

向应用通知 surface 位置信息。当网页布局变化、页面滚动或播放区域发生改变时由 ArkWeb 内核回调此方法，应用需据此更新原生播放器渲染表面的位置和大小。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| width | number | 是 |
| height | number | 是 |
