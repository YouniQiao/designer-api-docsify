# ImmersiveEffect

Describes the immersive effect.

**Since:** 23

<!--Device-inputMethodEngine-interface ImmersiveEffect--><!--Device-inputMethodEngine-interface ImmersiveEffect-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
import { inputMethodEngine } from '@kit.IMEKit';
```

## gradientHeight

```TypeScript
gradientHeight: int
```

Gradient height, which cannot exceed 15% of the screen height.

**Type:** int

**Since:** 23

<!--Device-ImmersiveEffect-gradientHeight: int--><!--Device-ImmersiveEffect-gradientHeight: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## gradientMode

```TypeScript
gradientMode: GradientMode
```

Gradient mode. If this attribute is not specified or is set to an invalid value, the gradient mode is not used by default.

**Type:** [GradientMode](arkts-ime-inputmethodengine-gradientmode-e.md)

**Since:** 23

<!--Device-ImmersiveEffect-gradientMode: GradientMode--><!--Device-ImmersiveEffect-gradientMode: GradientMode-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

