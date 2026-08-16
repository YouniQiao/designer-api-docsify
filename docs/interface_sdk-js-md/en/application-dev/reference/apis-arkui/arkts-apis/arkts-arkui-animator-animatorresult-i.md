# AnimatorResult

Defines the animator result.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** -1

<!--Device-unnamed-export interface AnimatorResult--><!--Device-unnamed-export interface AnimatorResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AnimatorOptions } from 'AnimatorOptions';
import { AnimatorResult } from 'AnimatorResult';
import { SimpleAnimatorOptions } from 'SimpleAnimatorOptions';
```

## cancel

```TypeScript
cancel(): void
```

Cancels the animation, triggering the [onCancel](../arkts-components/arkts-arkui-imageframeinfo-i.md#ImageFrameInfo) callback. This API is functionally identical to [finish](../../apis-na/arkts-apis/arkts-na-animator-animatorresult-i.md#finish) except for the callback it triggers. It is recommended that you use the **finish** API to end animations.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatorResult-cancel(): void--><!--Device-AnimatorResult-cancel(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

See ArkTS-based Declarative Development Paradigm.

```TypeScript
animator.cancel();
```

## finish

```TypeScript
finish(): void
```

Ends the animation, triggering the [onFinish](../arkts-components/arkts-arkui-imageframeinfo-i.md#ImageFrameInfo) callback.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatorResult-finish(): void--><!--Device-AnimatorResult-finish(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

See ArkTS-based Declarative Development Paradigm.

```TypeScript
animator.finish();
```

## pause

```TypeScript
pause(): void
```

Pauses this animation.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatorResult-pause(): void--><!--Device-AnimatorResult-pause(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

See ArkTS-based Declarative Development Paradigm.

```TypeScript
animator.pause();
```

## play

```TypeScript
play(): void
```

Plays this animation. The animation retains the previous playback state. For example, if the animation is set to **reverse** and paused, it will remain in **reverse** when resumed.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatorResult-play(): void--><!--Device-AnimatorResult-play(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

See ArkTS-based Declarative Development Paradigm.

```TypeScript
animator.play();
```

## reset

```TypeScript
reset(options: AnimatorOptions): void
```

Resets the animation parameters of this animator.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatorResult-reset(options: AnimatorOptions): void--><!--Device-AnimatorResult-reset(options: AnimatorOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AnimatorOptions](../../apis-na/arkts-apis/arkts-na-animator-animatoroptions-i.md) | Yes | Animator options. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../errorcode-internal.md#100001-internal-error) | The specified page is not found or the object property list is not obtained. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |

## Examples

```TypeScript
import { AnimatorResult } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;

  create() {
    this.animatorResult = this.getUIContext().createAnimator({
      duration: 1500,
      easing: "friction",
      delay: 0,
      fill: "forwards",
      direction: "normal",
      iterations: 3,
      begin: 200.0,
      end: 400.0
    })
    this.animatorResult.reset({
      duration: 1500,
      easing: "friction",
      delay: 0,
      fill: "forwards",
      direction: "normal",
      iterations: 5,
      begin: 200.0,
      end: 400.0
    });
  }

  build() {
    // ......
  }
}
```

## reset

```TypeScript
reset(options: AnimatorOptions | SimpleAnimatorOptions): void
```

Resets the animation parameters of this animator. Compared with [reset](../../apis-na/arkts-apis/arkts-na-animator-animatorresult-i.md#reset), this API accepts parameters of the [SimpleAnimatorOptions](../../apis-na/arkts-apis/arkts-na-animator-simpleanimatoroptions-c.md#SimpleAnimatorOptions) type.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AnimatorResult-reset(options: AnimatorOptions | SimpleAnimatorOptions): void--><!--Device-AnimatorResult-reset(options: AnimatorOptions | SimpleAnimatorOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AnimatorOptions](../../apis-na/arkts-apis/arkts-na-animator-animatoroptions-i.md) \| [SimpleAnimatorOptions](../../apis-na/arkts-apis/arkts-na-animator-simpleanimatoroptions-c.md) | Yes | Animator options. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../errorcode-internal.md#100001-internal-error) | The specified page is not found or the object property list is not obtained. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |

## Examples

See ArkTS-based Declarative Development Paradigm.

```TypeScript
import { Animator as animator, AnimatorResult, AnimatorOptions, SimpleAnimatorOptions } from '@kit.ArkUI';

let options: AnimatorOptions = {
  duration: 1500,
  easing: "ease",
  delay: 0,
  fill: "forwards",
  direction: "normal",
  iterations: 1,
  begin: 100,
  end: 200
};
let optionsNew: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200)
  .duration(2000)
  .iterations(3)
  .delay(1000)
let animatorResult: AnimatorResult = animator.create(options);
animatorResult.reset(optionsNew);
```

## reverse

```TypeScript
reverse(): void
```

Plays this animation in reverse order. This API does not take effect when the interpolating spring curve is used.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatorResult-reverse(): void--><!--Device-AnimatorResult-reverse(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

See ArkTS-based Declarative Development Paradigm.

```TypeScript
animator.reverse();
```

## setExpectedFrameRateRange

```TypeScript
setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void
```

Sets the expected frame rate range.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AnimatorResult-setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void--><!--Device-AnimatorResult-setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rateRange | ExpectedFrameRateRange | Yes | Expected frame rate range. |

## Examples

```TypeScript
import { AnimatorResult } from '@kit.ArkUI';

let expectedFrameRate: ExpectedFrameRateRange = {
  min: 0,
  max: 120,
  expected: 30
}

@Entry
@Component
struct AnimatorTest {
  private backAnimator: AnimatorResult | undefined = undefined

  create() {
    this.backAnimator = this.getUIContext().createAnimator({
      duration: 2000,
      easing: "ease",
      delay: 0,
      fill: "forwards",
      direction: "normal",
      iterations: 1,
      begin: 100, // Start point of the animation interpolation.
      end: 200 // End point of the animation interpolation.
    })
    this.backAnimator.setExpectedFrameRateRange(expectedFrameRate);
  }

  build() {
    // ......
  }
}
```

## update

```TypeScript
update(options: AnimatorOptions): void
```

Updates this animator.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** reset

<!--Device-AnimatorResult-update(options: AnimatorOptions): void--><!--Device-AnimatorResult-update(options: AnimatorOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AnimatorOptions](../../apis-na/arkts-apis/arkts-na-animator-animatoroptions-i.md) | Yes | Animator options. |

## Examples

See ArkTS-based Declarative Development Paradigm.

```TypeScript
animator.update(options);
```

## onCancel

```TypeScript
onCancel: () => void
```

Called when this animation is canceled.

**Type:** () =&gt; void

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AnimatorResult-onCancel: () => void--><!--Device-AnimatorResult-onCancel: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onFinish

```TypeScript
onFinish: () => void
```

Called when this animation is finished.

**Type:** () =&gt; void

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AnimatorResult-onFinish: () => void--><!--Device-AnimatorResult-onFinish: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onFrame

```TypeScript
onFrame: (progress: number) => void
```

Called when a frame is received. **progress**: current value of the animation. Value range: [begin, end] defined in [AnimatorOptions](../../apis-na/arkts-apis/arkts-na-animator-animatoroptions-i.md#AnimatorOptions). Default value range: [0, 1]

**Type:** (progress: number) =&gt; void

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AnimatorResult-onFrame: (progress: number) => void--><!--Device-AnimatorResult-onFrame: (progress: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onRepeat

```TypeScript
onRepeat: () => void
```

Called when this animation repeats.

**Type:** () =&gt; void

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AnimatorResult-onRepeat: () => void--><!--Device-AnimatorResult-onRepeat: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## oncancel

```TypeScript
oncancel: () => void
```

Called when this animation is canceled. Note: This API is supported since API version 6 and deprecated since API version 12. You are advised to use **onCancel** instead.

**Type:** () =&gt; void

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 12

**Substitutes:** onCancel

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatorResult-oncancel: () => void--><!--Device-AnimatorResult-oncancel: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onfinish

```TypeScript
onfinish: () => void
```

Called when this animation is finished. Note: This API is supported since API version 6 and deprecated since API version 12. You are advised to use **onFinish** instead.

**Type:** () =&gt; void

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 12

**Substitutes:** onFinish

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatorResult-onfinish: () => void--><!--Device-AnimatorResult-onfinish: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onframe

```TypeScript
onframe: (progress: number) => void
```

Called when a frame is received. Note: This API is supported since API version 6 and deprecated since API version 12. You are advised to use **onFrame** instead.

**Type:** (progress: number) =&gt; void

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 12

**Substitutes:** onFrame

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatorResult-onframe: (progress: number) => void--><!--Device-AnimatorResult-onframe: (progress: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onrepeat

```TypeScript
onrepeat: () => void
```

Called when this animation repeats. Note: This API is supported since API version 6 and deprecated since API version 12. You are advised to use **onRepeat** instead.

**Type:** () =&gt; void

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 12

**Substitutes:** onRepeat

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AnimatorResult-onrepeat: () => void--><!--Device-AnimatorResult-onrepeat: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

