# AnimatorResult

Defines the Animator result interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface AnimatorResult--><!--Device-unnamed-export interface AnimatorResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AnimatorOptions, SimpleAnimatorOptions, AnimatorResult } from 'kits/@kit.ArkUI';
```

## cancel

```TypeScript
cancel(): void
```

Cancels the animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorResult-cancel(): void--><!--Device-AnimatorResult-cancel(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## finish

```TypeScript
finish(): void
```

Ends the animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorResult-finish(): void--><!--Device-AnimatorResult-finish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCancel

```TypeScript
onCancel: () => void
```

The animation is canceled.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorResult-onCancel: () => void--><!--Device-AnimatorResult-onCancel: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onFinish

```TypeScript
onFinish: () => void
```

The animation is finished.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorResult-onFinish: () => void--><!--Device-AnimatorResult-onFinish: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onFrame

```TypeScript
onFrame: (progress: double) => void
```

Trigger when vSync callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorResult-onFrame: (progress: double) => void--><!--Device-AnimatorResult-onFrame: (progress: double) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| progress | double | Yes |  |

## onRepeat

```TypeScript
onRepeat: () => void
```

The animation is repeated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorResult-onRepeat: () => void--><!--Device-AnimatorResult-onRepeat: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pause

```TypeScript
pause(): void
```

Pauses the animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorResult-pause(): void--><!--Device-AnimatorResult-pause(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## play

```TypeScript
play(): void
```

Starts the animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorResult-play(): void--><!--Device-AnimatorResult-play(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reset

```TypeScript
reset(options: AnimatorOptions | SimpleAnimatorOptions): void
```

Reset the options for current animator.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorResult-reset(options: AnimatorOptions | SimpleAnimatorOptions): void--><!--Device-AnimatorResult-reset(options: AnimatorOptions | SimpleAnimatorOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AnimatorOptions](arkts-arkui-animator-animatoroptions-i.md) \| SimpleAnimatorOptions | Yes | Options. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../errorcode-internal.md#100001-internal-error) | The specified page is not found or the object property list is not obtained. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## reverse

```TypeScript
reverse(): void
```

Plays the animation in reverse direction.Invalid when using interpolating-spring curve.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorResult-reverse(): void--><!--Device-AnimatorResult-reverse(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setExpectedFrameRateRange

```TypeScript
setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void
```

The expected frame rate of dynamical of rate range.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimatorResult-setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void--><!--Device-AnimatorResult-setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rateRange | [ExpectedFrameRateRange](../arkts-components/arkts-arkui-expectedframeraterange-i.md) | Yes | Indicates ExpectedFrameRateRange. |

