# CreateNativeMediaPlayerCallback

```TypeScript
type CreateNativeMediaPlayerCallback =
      (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge
```

Defines a **CreateNativeMediaPlayerCallback** object used as a parameter of the [onCreateNativeMediaPlayer](arkts-arkweb-webview-webviewcontroller-c.md#onCreateNativeMediaPlayer) callback. This object is used to create a player to take over media playback of the web page.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-webview-type CreateNativeMediaPlayerCallback =      (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge--><!--Device-webview-type CreateNativeMediaPlayerCallback =      (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [NativeMediaPlayerHandler](arkts-arkweb-webview-nativemediaplayerhandler-i.md) | Yes |
| mediaInfo | [MediaInfo](arkts-arkweb-webview-mediainfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NativeMediaPlayerBridge](arkts-arkweb-webview-nativemediaplayerbridge-i.md) |
