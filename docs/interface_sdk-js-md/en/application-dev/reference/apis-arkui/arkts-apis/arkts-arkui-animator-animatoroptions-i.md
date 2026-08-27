# AnimatorOptions

Animator options.

**Since:** 6

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Animator, AnimatorOptions, AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';
```

## begin

```TypeScript
begin: number
```

Start point of the animation interpolation.

Note: This setting affects the input parameter value of the [onFrame](../../../reference/apis-arkui/js-apis-animator.md#properties) callback.

Default value: **0**

**Type:** number

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay: number
```

Animation delay duration, in milliseconds. Value **0** means that there is no delay. If the value specified is a negative number, the animation starts playing ahead of its scheduled time. If the amount of time by which the playback is advanced exceeds the total duration of the animation, the animation immediately skips to its end state.

Default value: **0**

**Type:** number

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

See ArkTS-based Declarative Development Paradigm.

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).delay(500);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

## direction

```TypeScript
direction: "normal" | "reverse" | "alternate" | "alternate-reverse"
```

Animation playback mode.

**'normal'**: plays the animation in forward loop mode.

**'reverse'**: plays the animation in reverse loop mode.

**'alternate'**: plays the animation in alternating loop mode. When the animation is played for an odd number of times, the playback is in forward direction. When the animation is played for an even number of times, the playback is in reverse direction.

**'alternate-reverse'**: plays the animation in reverse alternating loop mode. When the animation is played for an odd number of times, the playback is in reverse direction. When the animation is played for an even number of times, the playback is in forward direction.

Default value: **'normal'**

**Type:** "normal" \| "reverse" \| "alternate" \| "alternate-reverse"

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

See ArkTS-based Declarative Development Paradigm.

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).direction(PlayMode.Alternate);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

## duration

```TypeScript
duration: number
```

Duration for playing the animation, in milliseconds.

Value range: 0, +∞).

Default value: **0**

**Type:** number

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

See [ArkTS-based Declarative Development Paradigm.

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(500);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

## easing

```TypeScript
easing: string
```

Animation interpolation curve.

If the provided string is invalid, **"ease"** is used.

**Type:** string

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

See ArkTS-based Declarative Development Paradigm.

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).easing("ease-in");

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

## end

```TypeScript
end: number
```

End point of animation interpolation.

Note: This setting affects the input parameter value of the [onFrame](../../../reference/apis-arkui/js-apis-animator.md#properties) callback.

Default value: **1**

**Type:** number

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fill

```TypeScript
fill: "none" | "forwards" | "backwards" | "both"
```

State of the animated target after the animation is executed.

**'none'**: No style is applied to the target before or after the animation is executed.

**'forwards'**: The target keeps the state at the end of the animation (defined in the last key frame) after the animation is executed.

**'backwards'**: During the delay period specified in [AnimatorOptions](#animatoroptions), the animation uses the value defined in the first keyframe. When **direction** in [AnimatorOptions](#animatoroptions) is **'normal'** or **'alternate'**, the animation uses the **from** keyframe value. When **direction** in [AnimatorOptions](#animatoroptions) is **'reverse'** or **'alternate-reverse'**, the animation uses the **to** keyframe value.

**'both'**: The animation follows the **'forwards'** and **'backwards'** rules.

**Type:** "none" \| "forwards" \| "backwards" \| "both"

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

See ArkTS-based Declarative Development Paradigm.

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).fill(FillMode.Forwards);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```

## iterations

```TypeScript
iterations: number
```

Number of times that the animation is played. The value **0** means the animation is not played, **-1** means the animation is played for an unlimited number of times, and a positive integer means the animation is played that specific number of times.

Note: Any negative value other than **-1** is treated as invalid. For invalid values, the animation is played once.

**Type:** number

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

See ArkTS-based Declarative Development Paradigm.

```TypeScript
import { AnimatorResult, SimpleAnimatorOptions } from '@kit.ArkUI';

@Entry
@Component
struct AnimatorTest {
  private animatorResult: AnimatorResult | undefined = undefined;
  options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).iterations(3);

  create() {
    this.animatorResult = this.getUIContext().createAnimator(this.options);
  }

  build() {
    // ......
  }
}
```
