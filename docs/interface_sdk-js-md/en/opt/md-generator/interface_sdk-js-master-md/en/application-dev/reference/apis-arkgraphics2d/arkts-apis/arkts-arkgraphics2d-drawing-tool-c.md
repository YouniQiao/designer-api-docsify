# Tool

A utility class that provides only static methods to convert data structs defined in other modules and  
[common2D](arkts-graphics-common2d.md).

> **NOTE：**
> 
> - The initial APIs of this class are supported since API version 15.
> 
> - This module uses the physical pixel unit, px.
> 
> - The module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 15

<!--Device-drawing-class Tool--><!--Device-drawing-class Tool-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## makeColorFromResourceColor

```TypeScript
static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color
```

Converts a color value of the **ResourceColor** type to a **common2D.Color** object.

**Since:** 15

<!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color--><!--Device-Tool-static makeColorFromResourceColor(resourceColor: ResourceColor): common2D.Color-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceColor | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Color |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
