# VideoController

A **VideoController** object can control one or more **Video** components.

**Since:** 7

**Deprecated since:** -1

<!--Device-unnamed-declare class VideoController--><!--Device-unnamed-declare class VideoController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

A constructor used to create a **VideoController** object.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VideoController-constructor()--><!--Device-VideoController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## exitFullscreen

```TypeScript
exitFullscreen()
```

Exits full-screen mode.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VideoController-exitFullscreen()--><!--Device-VideoController-exitFullscreen()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pause

```TypeScript
pause()
```

Pauses playback. The current frame is then displayed, and playback will be resumed from this paused position.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VideoController-pause()--><!--Device-VideoController-pause()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## requestFullscreen

```TypeScript
requestFullscreen(value: boolean)
```

Requests full-screen playback.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VideoController-requestFullscreen(value: boolean)--><!--Device-VideoController-requestFullscreen(value: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## reset

```TypeScript
reset(): void
```

Resets the **AVPlayer** instance of this component, which displays the current frame and sets the playback to start from the beginning for subsequent playbacks.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-VideoController-reset(): void--><!--Device-VideoController-reset(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setCurrentTime

```TypeScript
setCurrentTime(value: number)
```

Sets the video playback position. > **NOTE：**> > To start playback from a specific position, disable autoplay, wait for video preparation to complete, and then > seek to the target position.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VideoController-setCurrentTime(value: number)--><!--Device-VideoController-setCurrentTime(value: number)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## setCurrentTime

```TypeScript
setCurrentTime(value: number, seekMode: SeekMode)
```

Sets the video playback position with the specified seek mode.

**Since:** 8

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VideoController-setCurrentTime(value: number, seekMode: SeekMode)--><!--Device-VideoController-setCurrentTime(value: number, seekMode: SeekMode)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| seekMode | [SeekMode](arkts-arkui-seekmode-e.md) | Yes |

## start

```TypeScript
start()
```

Starts playback.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VideoController-start()--><!--Device-VideoController-start()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stop

```TypeScript
stop()
```

Stops playback. The current frame is then displayed, and playback will restart from the very beginning.

**Since:** 7

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VideoController-stop()--><!--Device-VideoController-stop()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
