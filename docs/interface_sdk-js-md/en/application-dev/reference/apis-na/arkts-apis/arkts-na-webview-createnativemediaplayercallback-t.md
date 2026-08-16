# CreateNativeMediaPlayerCallback

```TypeScript
type CreateNativeMediaPlayerCallback =
        (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge
```

Defines a **CreateNativeMediaPlayerCallback** object used as a parameter of the [onCreateNativeMediaPlayer](../../../reference/apis-arkweb/arkts-apis-webview-WebviewController.md#onCreateNativeMediaPlayer) callback. This object is used to create a player to take over media playback of the web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-webview-type CreateNativeMediaPlayerCallback =        (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge--><!--Device-webview-type CreateNativeMediaPlayerCallback =        (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [NativeMediaPlayerHandler](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-nativemediaplayerhandler-i.md) | Yes | Object used to report the player status to the ArkWeb engine. |
| mediaInfo | [MediaInfo](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-mediainfo-i.md) | Yes | Information about the media on the web page. |

**Return value:**

| Type | Description |
| --- | --- |
| [NativeMediaPlayerBridge](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-nativemediaplayerbridge-i.md) | Instance of the interface class between the player that takes over web media and the ArkWeb kernel. <br>The application needs to implement this interface class. <br> The ArkWeb engine uses an object of this interface class to control the player created by the application to take over web page media. <br>If the application returns **null**, the application does not take over the media playback, and the media will be played by the ArkWeb engine. |

