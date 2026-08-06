# NativeMediaPlayerConfig

Represents the configuration for \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ .

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface NativeMediaPlayerConfig--><!--Device-unnamed-export declare interface NativeMediaPlayerConfig-End-->

**System capability:** SystemCapability.Web.Webview.Core

## enable

```TypeScript
enable: boolean
```

Whether to enable the application to take over web page media playback. The value **true** means to enable the application to take over web page media playback, and **false** means the opposite. Default value: **false**.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerConfig-enable: boolean--><!--Device-NativeMediaPlayerConfig-enable: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## shouldOverlay

```TypeScript
shouldOverlay: boolean
```

Whether the video player's display overlays the web page content when the application takes over the web page's video player. The value **true** indicates that the video player's display overlays the web page content. This means that the height of the video layer is adjusted to cover the web page content. The value **false** indicates that the video player's display does not overlay the web page content. This means that the video player maintains its original height and is embedded within the web page. Default value: **false**.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerConfig-shouldOverlay: boolean--><!--Device-NativeMediaPlayerConfig-shouldOverlay: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

