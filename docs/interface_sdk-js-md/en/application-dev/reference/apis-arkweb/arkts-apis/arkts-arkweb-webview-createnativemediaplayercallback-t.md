# CreateNativeMediaPlayerCallback

```TypeScript
type CreateNativeMediaPlayerCallback =
        (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge
```

Defines a **CreateNativeMediaPlayerCallback** object used as a parameter of the  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_callback. This object is used to create a player to take over media playback of the web page.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-webview-type CreateNativeMediaPlayerCallback =        (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge--><!--Device-webview-type CreateNativeMediaPlayerCallback =        (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Object used to report the player status to the ArkWeb engine.  |
| mediaInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Information about the media on the web page.  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Instance of the interface class between the player that takes over web media and the ArkWeb kernel. \_\_\_HTML\_TAG\_USD\_0\_\_\_The application needs to implement this interface class. \_\_\_HTML\_TAG\_USD\_1\_\_\_ The ArkWeb engine uses an object of this interface class to control the player created by the application to take over web page media. \_\_\_HTML\_TAG\_USD\_2\_\_\_If the application returns **null**, the application does not take over the media playback, and the media will be played by the ArkWeb engine.  |

