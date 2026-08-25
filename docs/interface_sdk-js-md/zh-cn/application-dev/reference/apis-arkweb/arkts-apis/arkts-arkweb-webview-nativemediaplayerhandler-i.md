# NativeMediaPlayerHandler

NativeMediaPlayerHandler 是[CreateNativeMediaPlayerCallback](arkts-arkweb-webview-createnativemediaplayercallback-t.md)回调函数的参数。当 应用使用[NativeMediaPlayerBridge](arkts-arkweb-webview-nativemediaplayerbridge-i.md)接管网页媒体播放时，需要通过将播放器的各种状态变化实时同步给 ArkWeb 内核，确保网页 JavaScript 能够获取正确的播放器状态，ArkWeb 内核会将这些状态转换为标准的 HTML5 Media Events，触发网页中注册的事件监听器，从而保证网页功能的正常运行。

**起始版本：** 12

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## handleBufferedEndTimeChanged

```TypeScript
handleBufferedEndTimeChanged(bufferedEndTime: number): void
```

当媒体的缓冲时长发生变化时，调用该方法将媒体的缓冲时长通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bufferedEndTime | number | 是 |

## handleDurationChanged

```TypeScript
handleDurationChanged(duration: number): void
```

当播放器解析出媒体的总时长时，调用该方法将媒体的总时长通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| duration | number | 是 |

## handleEnded

```TypeScript
handleEnded(): void
```

当媒体播放结束时，调用该方法将播放结束事件通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## handleError

```TypeScript
handleError(error: MediaError, errorMessage: string): void
```

当播放器发生错误时，调用该方法将错误通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| error | [MediaError](arkts-arkweb-webview-mediaerror-e.md) | 是 |
| [errorMessage](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-update-errormessage-i-sys.md) | string | 是 |

## handleFullscreenChanged

```TypeScript
handleFullscreenChanged(fullscreen: boolean): void
```

当播放器的全屏状态发生变化时，调用该方法将播放器的全屏状态通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fullscreen](../../apis-arkui/arkts-components/arkts-arkui-fullscreeninfo-i.md) | boolean | 是 |

## handleMutedChanged

```TypeScript
handleMutedChanged(muted: boolean): void
```

当播放器的静音状态发生变化时，调用该方法将静音状态通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| muted | boolean | 是 |

## handleNetworkStateChanged

```TypeScript
handleNetworkStateChanged(state: NetworkState): void
```

当播放器的网络状态发生变化时，调用该方法将播放器的网络状态通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | [NetworkState](../../apis-telephony-kit/arkts-apis/arkts-telephony-radio-networkstate-i.md) | 是 |

## handlePlaybackRateChanged

```TypeScript
handlePlaybackRateChanged(playbackRate: number): void
```

当播放器的播放速率发生变化时，调用该方法将播放速率通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| playbackRate | number | 是 |

## handleReadyStateChanged

```TypeScript
handleReadyStateChanged(state: ReadyState): void
```

当播放器的缓存状态发生变化时，调用该方法将播放器的缓存状态通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | [ReadyState](arkts-arkweb-webview-readystate-e.md) | 是 |

## handleSeekFinished

```TypeScript
handleSeekFinished(): void
```

当播放器 seek 完成后，调用该方法将 seek 完成事件通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## handleSeeking

```TypeScript
handleSeeking(): void
```

当播放器进入 seek 状态时，调用该方法将 seek 进入事件通知 ArkWeb 内核。seek 完成后，应调用 handleSeekFinished 将 seek 完成事件通知 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

## handleStatusChanged

```TypeScript
handleStatusChanged(status: PlaybackStatus): void
```

当播放器的播放状态发生变化时，调用该方法将播放状态通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| status | [PlaybackStatus](arkts-arkweb-webview-playbackstatus-e.md) | 是 |

## handleTimeUpdate

```TypeScript
handleTimeUpdate(currentPlayTime: number): void
```

当媒体的播放进度发生变化时，调用该方法将媒体的播放进度通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| currentPlayTime | number | 是 |

## handleVideoSizeChanged

```TypeScript
handleVideoSizeChanged(width: number, height: number): void
```

当播放器解析出视频的尺寸时，调用该方法将视频尺寸通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| height | number | 是 |

## handleVolumeChanged

```TypeScript
handleVolumeChanged(volume: number): void
```

当播放器的音量发生变化时，调用该方法将音量通知给 ArkWeb 内核。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| volume | number | 是 |
