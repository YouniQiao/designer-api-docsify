# TypefaceArguments

This module defines a struct for setting typeface arguments.

> **NOTE：**
> 
> - The initial APIs of this class are supported since API version 20.
> 
> - This module uses the physical pixel unit, px.
> 
> - The module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 20

<!--Device-drawing-class TypefaceArguments--><!--Device-drawing-class TypefaceArguments-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## addVariation

```TypeScript
addVariation(axis: string, value: number)
```

Defines the typeface weight.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypefaceArguments-addVariation(axis: string, value: number)--><!--Device-TypefaceArguments-addVariation(axis: string, value: number)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| axis | string | Yes |
| value | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkgraphics2d/errorcode-drawing.md#25900001-abnormal-parameter-value) |

## constructor

```TypeScript
constructor()
```

Constructor for typeface arguments.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypefaceArguments-constructor()--><!--Device-TypefaceArguments-constructor()-End-->

**System capability:** SystemCapability.Graphics.Drawing
