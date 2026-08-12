# createEffect

## Modules to Import

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## createEffect

```TypeScript
function createEffect(): VisualEffect
```

Creates a VisualEffect instance for adding multiple VisualEffect effects to a component.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-uiEffect-function createEffect(): VisualEffect--><!--Device-uiEffect-function createEffect(): VisualEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| VisualEffect | Returns a VisualEffect instance, which supports adding multiple VisualEffect effects. |

## Examples

```TypeScript
let visualEffect : uiEffect.VisualEffect = uiEffect.createEffect()
```

