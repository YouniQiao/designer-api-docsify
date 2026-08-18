# NativeMediaPlayerHandler

NativeMediaPlayerHandler is the parameter of the [CreateNativeMediaPlayerCallback](arkts-arkweb-webview-createnativemediaplayercallback-t.md#createnativemediaplayercallback) callback function. When an app uses [NativeMediaPlayerBridge](arkts-arkweb-webview-nativemediaplayerbridge-i.md#nativemediaplayerbridge) to take over web media playback, it must synchronize various player state changes to the ArkWeb kernel in real time. This ensures that the web JavaScript can obtain the correct player state. The ArkWeb kernel converts these states into standard HTML5 Media Events and triggers the event listeners registered in the web page, thereby ensuring the normal functioning of the web page.

**Since:** 12

<!--Device-webview-interface NativeMediaPlayerHandler--><!--Device-webview-interface NativeMediaPlayerHandler-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## handleBufferedEndTimeChanged

```TypeScript
handleBufferedEndTimeChanged(bufferedEndTime: number): void
```

Called to notify the ArkWeb engine of the buffer time when the buffer time changes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleBufferedEndTimeChanged(bufferedEndTime: number): void--><!--Device-NativeMediaPlayerHandler-handleBufferedEndTimeChanged(bufferedEndTime: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bufferedEndTime | number | Yes |

## handleDurationChanged

```TypeScript
handleDurationChanged(duration: number): void
```

Called to notify the ArkWeb engine of the total duration of the media.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleDurationChanged(duration: number): void--><!--Device-NativeMediaPlayerHandler-handleDurationChanged(duration: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| duration | number | Yes |

## handleEnded

```TypeScript
handleEnded(): void
```

When media playback ends, this method is called to notify the ArkWeb kernel of the playback end event.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleEnded(): void--><!--Device-NativeMediaPlayerHandler-handleEnded(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handleError

```TypeScript
handleError(error: MediaError, errorMessage: string): void
```

When an error occurs in the player, this method is called to notify the ArkWeb kernel of the error.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleError(error: MediaError, errorMessage: string): void--><!--Device-NativeMediaPlayerHandler-handleError(error: MediaError, errorMessage: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| error | [MediaError](arkts-arkweb-webview-mediaerror-e.md) | Yes |
| [errorMessage](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-update-errormessage-i-sys.md) | string | Yes |

## handleFullscreenChanged

```TypeScript
handleFullscreenChanged(fullscreen: boolean): void
```

Called to notify the ArkWeb engine of the full screen status of the player when the full screen status changes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleFullscreenChanged(fullscreen: boolean): void--><!--Device-NativeMediaPlayerHandler-handleFullscreenChanged(fullscreen: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fullscreen | boolean | Yes |

## handleMutedChanged

```TypeScript
handleMutedChanged(muted: boolean): void
```

Called to notify the ArkWeb engine of the muted status of the player when the muted status changes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleMutedChanged(muted: boolean): void--><!--Device-NativeMediaPlayerHandler-handleMutedChanged(muted: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| muted | boolean | Yes |

## handleNetworkStateChanged

```TypeScript
handleNetworkStateChanged(state: NetworkState): void
```

Called to notify the ArkWeb engine of the network status of the player when the network status changes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleNetworkStateChanged(state: NetworkState): void--><!--Device-NativeMediaPlayerHandler-handleNetworkStateChanged(state: NetworkState): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | [NetworkState](../../apis-telephony-kit/arkts-apis/arkts-telephony-radio-networkstate-i.md) | Yes |

## handlePlaybackRateChanged

```TypeScript
handlePlaybackRateChanged(playbackRate: number): void
```

When the playback rate of the player changes, this method is called to notify the ArkWeb kernel of the playback rate.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handlePlaybackRateChanged(playbackRate: number): void--><!--Device-NativeMediaPlayerHandler-handlePlaybackRateChanged(playbackRate: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| playbackRate | number | Yes |

## handleReadyStateChanged

```TypeScript
handleReadyStateChanged(state: ReadyState): void
```

Called to notify the ArkWeb engine of the cache status of the player when the cache status changes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleReadyStateChanged(state: ReadyState): void--><!--Device-NativeMediaPlayerHandler-handleReadyStateChanged(state: ReadyState): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| state | [ReadyState](arkts-arkweb-webview-readystate-e.md) | Yes |

## handleSeekFinished

```TypeScript
handleSeekFinished(): void
```

When the player completes seeking, this method is called to notify the ArkWeb kernel of the seek completion event.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleSeekFinished(): void--><!--Device-NativeMediaPlayerHandler-handleSeekFinished(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handleSeeking

```TypeScript
handleSeeking(): void
```

When the player enters the seek state, this method is called to notify the ArkWeb kernel of the seek entry event. After the seek is complete, handleSeekFinished should be called to notify the ArkWeb kernel of the seek completion event.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleSeeking(): void--><!--Device-NativeMediaPlayerHandler-handleSeeking(): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

## handleStatusChanged

```TypeScript
handleStatusChanged(status: PlaybackStatus): void
```

Called to notify the ArkWeb engine of the playback status of the player when the playback status changes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleStatusChanged(status: PlaybackStatus): void--><!--Device-NativeMediaPlayerHandler-handleStatusChanged(status: PlaybackStatus): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| status | [PlaybackStatus](arkts-arkweb-webview-playbackstatus-e.md) | Yes |

## handleTimeUpdate

```TypeScript
handleTimeUpdate(currentPlayTime: number): void
```

Called to notify the ArkWeb engine of the playback progress when the playback progress changes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleTimeUpdate(currentPlayTime: number): void--><!--Device-NativeMediaPlayerHandler-handleTimeUpdate(currentPlayTime: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| currentPlayTime | number | Yes |

## handleVideoSizeChanged

```TypeScript
handleVideoSizeChanged(width: number, height: number): void
```

When the player parses the video dimensions, this method is called to notify the ArkWeb kernel of the video size.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleVideoSizeChanged(width: number, height: number): void--><!--Device-NativeMediaPlayerHandler-handleVideoSizeChanged(width: number, height: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| height | number | Yes |

## handleVolumeChanged

```TypeScript
handleVolumeChanged(volume: number): void
```

Called to notify the ArkWeb engine of the volume of the player when the volume changes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NativeMediaPlayerHandler-handleVolumeChanged(volume: number): void--><!--Device-NativeMediaPlayerHandler-handleVolumeChanged(volume: number): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volume | number | Yes |
