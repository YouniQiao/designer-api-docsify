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

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) |

**Examples**

```TypeScript
let visualEffect : uiEffect.VisualEffect = uiEffect.createEffect()
```
