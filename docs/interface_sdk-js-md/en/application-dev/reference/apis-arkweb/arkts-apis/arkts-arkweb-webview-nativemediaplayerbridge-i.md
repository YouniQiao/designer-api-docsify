# NativeMediaPlayerBridge

NativeMediaPlayerBridge is the return value type of the [CreateNativeMediaPlayerCallback](arkts-arkweb-webview-createnativemediaplayercallback-t.md) callback function. It is an interface class between the player that takes over web page media and the ArkWeb kernel. The ArkWeb kernel uses an object of this interface class to control the player created by the app to take over web page media. This interface allows the app to use a custom media player to take over media content playback in web pages. It also supports player suspension and resumption mechanisms.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from 'kits/@kit.ArkWeb';
```

## enterFullscreen

```TypeScript
enterFullscreen(): void
```

Enables the player to enter full screen mode.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

## exitFullscreen

```TypeScript
exitFullscreen(): void
```

Enables the player to exit full screen mode.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

## pause

```TypeScript
pause(): void
```

Pauses playback.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

## play

```TypeScript
play(): void
```

Plays the media.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

## release

```TypeScript
release(): void
```

Releases this player.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

## resumePlayer

```TypeScript
resumePlayer?(): void
```

Notifies the app to rebuild the player and restore its status information. This method is used only in pair with suspendPlayer.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

## seek

```TypeScript
seek(targetTime: number): void
```

Seeks to a specific time point in the media.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| targetTime | number | Yes |

## setMuted

```TypeScript
setMuted(muted: boolean): void
```

Sets the muted status.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| muted | boolean | Yes |

## setPlaybackRate

```TypeScript
setPlaybackRate(playbackRate: number): void
```

Sets the playback rate.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| playbackRate | number | Yes |

## setVolume

```TypeScript
setVolume(volume: number): void
```

Sets the playback volume.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volume | number | Yes |

## suspendPlayer

```TypeScript
suspendPlayer?(type: SuspendType): void
```

Notifies the app to destroy the player and save its status information. This method is used only in pair with resumePlayer.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [SuspendType](arkts-arkweb-webview-suspendtype-e.md) | Yes |

## updateRect

```TypeScript
updateRect(x: number, y: number, width: number, height: number): void
```

Notifies the app of the surface position information. This method is called back by the ArkWeb kernel when the web page layout changes, the page scrolls, or the playback area changes. The app must update the position and size of the native player's rendering surface accordingly.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| width | number | Yes |
| height | number | Yes |
