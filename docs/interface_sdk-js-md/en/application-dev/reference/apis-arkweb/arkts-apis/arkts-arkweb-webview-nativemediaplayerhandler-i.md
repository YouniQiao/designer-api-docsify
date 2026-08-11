# NativeMediaPlayerHandler

Implements a **NativeMediaPlayerHandler** object used as a parameter of the  
[CreateNativeMediaPlayerCallback](../../../reference/apis-arkweb/arkts-apis-webview-t.md#createnativemediaplayercallback12)callback. The application uses this object to report the player status to the ArkWeb engine.

> **NOTE：**
> 
> - The sample effect is subject to the actual device.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-webview-interface NativeMediaPlayerHandler--><!--Device-webview-interface NativeMediaPlayerHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## handleBufferedEndTimeChanged

```TypeScript
handleBufferedEndTimeChanged(bufferedEndTime: double): void
```

Called to notify the ArkWeb engine of the buffer time when the buffer time changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleBufferedEndTimeChanged(bufferedEndTime: double): void--><!--Device-NativeMediaPlayerHandler-handleBufferedEndTimeChanged(bufferedEndTime: double): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bufferedEndTime | double | Yes | Duration of media data in the buffer.&lt;br&gt;Unit: second. Value range: [0, duration] |

## handleDurationChanged

```TypeScript
handleDurationChanged(duration: double): void
```

Called to notify the ArkWeb engine of the total duration of the media.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleDurationChanged(duration: double): void--><!--Device-NativeMediaPlayerHandler-handleDurationChanged(duration: double): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| duration | double | Yes | Total duration of the media.&lt;br&gt;Unit: second. Value range: [0,+��) |

## handleEnded

```TypeScript
handleEnded(): void
```

Called to notify the ArkWeb engine that the media playback ends.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleEnded(): void--><!--Device-NativeMediaPlayerHandler-handleEnded(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handleError

```TypeScript
handleError(error: MediaError, errorMessage: string): void
```

Called to notify the ArkWeb engine that an error occurs with the player.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleError(error: MediaError, errorMessage: string): void--><!--Device-NativeMediaPlayerHandler-handleError(error: MediaError, errorMessage: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| error | [MediaError](arkts-arkweb-webview-mediaerror-e.md) | Yes | Error object type. |
| errorMessage | string | Yes | Error message. |

## handleFullscreenChanged

```TypeScript
handleFullscreenChanged(fullscreen: boolean): void
```

Called to notify the ArkWeb engine of the full screen status of the player when the full screen status changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleFullscreenChanged(fullscreen: boolean): void--><!--Device-NativeMediaPlayerHandler-handleFullscreenChanged(fullscreen: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fullscreen | boolean | Yes | Whether the player is in full screen.&lt;br&gt;The value **true** means that the player is in full screen, and **false** means the opposite. |

## handleMutedChanged

```TypeScript
handleMutedChanged(muted: boolean): void
```

Called to notify the ArkWeb engine of the muted status of the player when the muted status changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleMutedChanged(muted: boolean): void--><!--Device-NativeMediaPlayerHandler-handleMutedChanged(muted: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| muted | boolean | Yes | Whether the player is muted.&lt;br&gt;The value **true** indicates that the player is muted, and **false** indicates the opposite. |

## handleNetworkStateChanged

```TypeScript
handleNetworkStateChanged(state: NetworkState): void
```

Called to notify the ArkWeb engine of the network status of the player when the network status changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleNetworkStateChanged(state: NetworkState): void--><!--Device-NativeMediaPlayerHandler-handleNetworkStateChanged(state: NetworkState): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [NetworkState](../../apis-telephony-kit/arkts-apis/arkts-telephony-radio-networkstate-i.md) | Yes | Network status of the player. |

## handlePlaybackRateChanged

```TypeScript
handlePlaybackRateChanged(playbackRate: double): void
```

Called to notify the ArkWeb engine of the playback rate of the player when the playback rate changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handlePlaybackRateChanged(playbackRate: double): void--><!--Device-NativeMediaPlayerHandler-handlePlaybackRateChanged(playbackRate: double): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| playbackRate | double | Yes | Playback rate. The value range is [0, +��). |

## handleReadyStateChanged

```TypeScript
handleReadyStateChanged(state: ReadyState): void
```

Called to notify the ArkWeb engine of the cache status of the player when the cache status changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleReadyStateChanged(state: ReadyState): void--><!--Device-NativeMediaPlayerHandler-handleReadyStateChanged(state: ReadyState): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [ReadyState](arkts-arkweb-webview-readystate-e.md) | Yes | Cache status of the player. |

## handleSeekFinished

```TypeScript
handleSeekFinished(): void
```

Called to notify the ArkWeb engine that the seek operation is complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleSeekFinished(): void--><!--Device-NativeMediaPlayerHandler-handleSeekFinished(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handleSeeking

```TypeScript
handleSeeking(): void
```

Called to notify the ArkWeb engine that the player enters the seek state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleSeeking(): void--><!--Device-NativeMediaPlayerHandler-handleSeeking(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handleStatusChanged

```TypeScript
handleStatusChanged(status: PlaybackStatus): void
```

Called to notify the ArkWeb engine of the playback status of the player when the playback status changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleStatusChanged(status: PlaybackStatus): void--><!--Device-NativeMediaPlayerHandler-handleStatusChanged(status: PlaybackStatus): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| status | [PlaybackStatus](arkts-arkweb-webview-playbackstatus-e.md) | Yes | Player status. |

## handleTimeUpdate

```TypeScript
handleTimeUpdate(currentPlayTime: double): void
```

Called to notify the ArkWeb engine of the playback progress when the playback progress changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleTimeUpdate(currentPlayTime: double): void--><!--Device-NativeMediaPlayerHandler-handleTimeUpdate(currentPlayTime: double): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| currentPlayTime | double | Yes | Current progress.&lt;br&gt;Unit: second. Value range: [0, duration] |

## handleVideoSizeChanged

```TypeScript
handleVideoSizeChanged(width: double, height: double): void
```

Called to notify the ArkWeb engine of the video size of the player.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleVideoSizeChanged(width: double, height: double): void--><!--Device-NativeMediaPlayerHandler-handleVideoSizeChanged(width: double, height: double): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | double | Yes | Video width, in pixels. Value range: [0,+��) |
| height | double | Yes | Video height, in pixels. Value range: [0,+��) |

## handleVolumeChanged

```TypeScript
handleVolumeChanged(volume: double): void
```

Called to notify the ArkWeb engine of the volume of the player when the volume changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-NativeMediaPlayerHandler-handleVolumeChanged(volume: double): void--><!--Device-NativeMediaPlayerHandler-handleVolumeChanged(volume: double): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volume | double | Yes | Volume of the player. The value range is [0, 1.0]. |

