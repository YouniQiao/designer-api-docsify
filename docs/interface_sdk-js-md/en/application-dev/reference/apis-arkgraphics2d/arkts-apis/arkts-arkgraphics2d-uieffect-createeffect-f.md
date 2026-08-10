# createEffect

## Modules to Import

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## createEffect

```TypeScript
function createEffect(): VisualEffect
```

创建VisualEffect实例用于给组件添加多种VisualEffect效果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-uiEffect-function createEffect(): VisualEffect--><!--Device-uiEffect-function createEffect(): VisualEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) | 返回VisualEffect实例，支持添加多种VisualEffect效果。 |

## Examples

```TypeScript
// Create a VisualEffect instance
let visualEffect : uiEffect.VisualEffect = uiEffect.createEffect();
```

