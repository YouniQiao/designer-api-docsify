# createFilter

## Modules to Import

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## createFilter

```TypeScript
function createFilter(): Filter
```

Creates a Filter instance for adding multiple filter effects to a component.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-uiEffect-function createFilter(): Filter--><!--Device-uiEffect-function createFilter(): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Filter | Returns a Filter instance, which supports adding multiple filter effects. |

## Examples

```TypeScript
let filter : uiEffect.Filter = uiEffect.createFilter()
```

