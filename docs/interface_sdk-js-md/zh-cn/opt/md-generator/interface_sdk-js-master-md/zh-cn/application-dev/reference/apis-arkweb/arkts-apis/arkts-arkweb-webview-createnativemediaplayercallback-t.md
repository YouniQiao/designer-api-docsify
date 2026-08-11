# CreateNativeMediaPlayerCallback

```TypeScript
type CreateNativeMediaPlayerCallback =
      (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge
```

[onCreateNativeMediaPlayer](@ohos.web.webview:webview.WebviewController#onCreateNativeMediaPlayer(callback: CreateNativeMediaPlayerCallback))方法的参数。一个回调函数，创建一个播放器，用于接管网页中的媒体播放。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-webview-type CreateNativeMediaPlayerCallback =      (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge--><!--Device-webview-type CreateNativeMediaPlayerCallback =      (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [NativeMediaPlayerHandler](arkts-arkweb-webview-nativemediaplayerhandler-i.md) | 是 |
| mediaInfo | [MediaInfo](arkts-arkweb-webview-mediainfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [NativeMediaPlayerBridge](arkts-arkweb-webview-nativemediaplayerbridge-i.md) |
