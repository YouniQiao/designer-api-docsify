# NativeMediaPlayerBridge

Implements a **CreateNativeMediaPlayerCallback** object to control the player created by the application for taking over the web page media playback. This object is a return value type of the  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_callback.
    **NOTE**  
    
    - The sample effect is subject to the actual device.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-webview-interface NativeMediaPlayerBridge--><!--Device-webview-interface NativeMediaPlayerBridge-End-->

**System capability:** SystemCapability.Web.Webview.Core

## enterFullscreen

```TypeScript
enterFullscreen: ZeroParamFn<>
```

Enables the player to enter full screen mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-enterFullscreen: ZeroParamFn<>--><!--Device-NativeMediaPlayerBridge-enterFullscreen: ZeroParamFn<>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## exitFullscreen

```TypeScript
exitFullscreen: ZeroParamFn<>
```

Enables the player to exit full screen mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-exitFullscreen: ZeroParamFn<>--><!--Device-NativeMediaPlayerBridge-exitFullscreen: ZeroParamFn<>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## pause

```TypeScript
pause: ZeroParamFn<>
```

Pauses playback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-pause: ZeroParamFn<>--><!--Device-NativeMediaPlayerBridge-pause: ZeroParamFn<>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## play

```TypeScript
play: ZeroParamFn<>
```

Plays this video.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-play: ZeroParamFn<>--><!--Device-NativeMediaPlayerBridge-play: ZeroParamFn<>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## release

```TypeScript
release: ZeroParamFn<>
```

Releases this player.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-release: ZeroParamFn<>--><!--Device-NativeMediaPlayerBridge-release: ZeroParamFn<>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## resumePlayer

```TypeScript
resumePlayer?: ResumePlayerFn
```

Resumes the player and its status information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-resumePlayer?: ResumePlayerFn--><!--Device-NativeMediaPlayerBridge-resumePlayer?: ResumePlayerFn-End-->

**System capability:** SystemCapability.Web.Webview.Core

## seek

```TypeScript
seek: OneParamFn<double>
```

Seeks to a specific time point in the media.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-seek: OneParamFn<double>--><!--Device-NativeMediaPlayerBridge-seek: OneParamFn<double>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## setMuted

```TypeScript
setMuted: OneParamFn<boolean>
```

Sets the muted status.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-setMuted: OneParamFn<boolean>--><!--Device-NativeMediaPlayerBridge-setMuted: OneParamFn<boolean>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## setPlaybackRate

```TypeScript
setPlaybackRate: OneParamFn<double>
```

Sets the playback rate.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-setPlaybackRate: OneParamFn<double>--><!--Device-NativeMediaPlayerBridge-setPlaybackRate: OneParamFn<double>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## setVolume

```TypeScript
setVolume: OneParamFn<double>
```

Sets the playback volume.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-setVolume: OneParamFn<double>--><!--Device-NativeMediaPlayerBridge-setVolume: OneParamFn<double>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## suspendPlayer

```TypeScript
suspendPlayer?: SuspendPlayerFn
```

Suspends the player and save its status information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-suspendPlayer?: SuspendPlayerFn--><!--Device-NativeMediaPlayerBridge-suspendPlayer?: SuspendPlayerFn-End-->

**System capability:** SystemCapability.Web.Webview.Core

## updateRect

```TypeScript
updateRect: UpdateRectFn
```

Updates the surface position information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerBridge-updateRect: UpdateRectFn--><!--Device-NativeMediaPlayerBridge-updateRect: UpdateRectFn-End-->

**System capability:** SystemCapability.Web.Webview.Core

