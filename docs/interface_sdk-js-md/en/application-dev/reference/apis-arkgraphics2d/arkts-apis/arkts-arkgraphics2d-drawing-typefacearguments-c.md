# TypefaceArguments

This module defines a struct for setting typeface arguments. > **NOTE：**> > - The initial APIs of this class are supported since API version 20. > > - This module uses the physical pixel unit, px. > > - The module operates under a single-threaded model. The caller needs to manage thread safety and context state > transitions.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

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

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypefaceArguments-addVariation(axis: string, value: number)--><!--Device-TypefaceArguments-addVariation(axis: string, value: number)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| axis | string | Yes | Indicates the axis tag, which must contain four ASCII characters. |
| value | number | Yes | Indicates the value of the axis field. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) | Parameter error. Possible causes: Incorrect parameter range. |

## addVariation

```TypeScript
addVariation(axis: string, value: double) : void
```

Adds variation axis for the TypefaceArguments.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-TypefaceArguments-addVariation(axis: string, value: double) : void--><!--Device-TypefaceArguments-addVariation(axis: string, value: double) : void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| axis | string | Yes | Indicates the axis tag, which must contain four ASCII characters. |
| value | double | Yes | Indicates the value of the axis field. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) | Parameter error. Possible causes: Incorrect parameter range. |

## constructor

```TypeScript
constructor()
```

Constructor for typeface arguments.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TypefaceArguments-constructor()--><!--Device-TypefaceArguments-constructor()-End-->

**System capability:** SystemCapability.Graphics.Drawing

