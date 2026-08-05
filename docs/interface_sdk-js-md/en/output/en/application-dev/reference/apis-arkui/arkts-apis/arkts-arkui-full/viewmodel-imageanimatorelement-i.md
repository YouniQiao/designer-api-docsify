# ImageAnimatorElement

The &lt;image-animator&gt; component is used to provide an image frame animator.

**Inheritance/Implementation:** ImageAnimatorElement extends [Element](viewmodel-element-i.md)

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

<!--Device-unnamed-export interface ImageAnimatorElement extends Element--><!--Device-unnamed-export interface ImageAnimatorElement extends Element-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## getState

```TypeScript
getState(): "Playing" | "Paused" | "Stopped"
```

Obtains the playback state. Available values are as follows: Playing Paused Stopped

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ImageAnimatorElement-getState(): "Playing" | "Paused" | "Stopped"--><!--Device-ImageAnimatorElement-getState(): "Playing" | "Paused" | "Stopped"-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| "Playing" |  |

## pause

```TypeScript
pause(): void
```

Pauses the frame animation playback of an image.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ImageAnimatorElement-pause(): void--><!--Device-ImageAnimatorElement-pause(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resume

```TypeScript
resume(): void
```

Resumes the frame animation playback of an image.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ImageAnimatorElement-resume(): void--><!--Device-ImageAnimatorElement-resume(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start(): void
```

Starts to play the frame animation of an image. If this method is called again, the playback starts from the first frame.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ImageAnimatorElement-start(): void--><!--Device-ImageAnimatorElement-start(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stop

```TypeScript
stop(): void
```

Stops the frame animation playback of an image.

**Since:** 4

**ArkTS mode:** ArkTS-Dyn only, since version 4.

**Model restriction:** This API can be used only in the FA model.

<!--Device-ImageAnimatorElement-stop(): void--><!--Device-ImageAnimatorElement-stop(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

