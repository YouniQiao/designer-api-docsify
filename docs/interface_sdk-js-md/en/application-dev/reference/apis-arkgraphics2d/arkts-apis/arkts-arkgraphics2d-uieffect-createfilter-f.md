# createFilter

## Modules to Import

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## createFilter

```TypeScript
function createFilter(): Filter
```

创建Filter实例用于给组件添加多种Filter效果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-uiEffect-function createFilter(): Filter--><!--Device-uiEffect-function createFilter(): Filter-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [Filter](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 返回Filter实例，支持添加多种Filter效果。 |

## Examples

```TypeScript
// Create a Filter instance
let filter : uiEffect.Filter = uiEffect.createFilter();
```

