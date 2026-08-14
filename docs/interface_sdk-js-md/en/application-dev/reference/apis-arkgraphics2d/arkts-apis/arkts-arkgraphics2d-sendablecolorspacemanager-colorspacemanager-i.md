# ColorSpaceManager

Implements management of color space objects. ColorSpaceManager is a core class used to manage and operate color space objects. It provides functions such as obtaining the color space type, white point value, and gamma value, and supports transfer between concurrent ArkTS instances. Before calling any of the following APIs, you must use [create()](arkts-arkgraphics2d-sendablecolorspacemanager-create-f.md#create) to create a color space manager.

**Inheritance/Implementation:** ColorSpaceManager extends [ISendable](arkts-arkgraphics2d-sendablecolorspacemanager-isendable-t.md#ISendable)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-sendableColorSpaceManager-interface ColorSpaceManager--><!--Device-sendableColorSpaceManager-interface ColorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

## Modules to Import

```TypeScript
import { sendableColorSpaceManager } from 'sendableColorSpaceManager';
```

## getColorSpaceName

```TypeScript
getColorSpaceName(): colorSpaceManager.ColorSpace
```

Obtains the color space type.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-ColorSpaceManager-getColorSpaceName(): colorSpaceManager.ColorSpace--><!--Device-ColorSpaceManager-getColorSpaceName(): colorSpaceManager.ColorSpace-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| colorSpaceManager.ColorSpace | Color space type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) | The parameter value is abnormal.<br>**Applicable version:** 12 - 22 |

## Examples

```TypeScript
let spaceName: colorSpaceManager.ColorSpace = colorSpace.getColorSpaceName();
```

## getGamma

```TypeScript
getGamma(): number
```

Obtains the gamma of the color space.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-ColorSpaceManager-getGamma(): number--><!--Device-ColorSpaceManager-getGamma(): number-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | Gamma of the color space. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) | The parameter value is abnormal.<br>**Applicable version:** 12 - 22 |

## Examples

```TypeScript
let gamma: number = colorSpace.getGamma();
```

## getWhitePoint

```TypeScript
getWhitePoint(): collections.Array<number>
```

Obtains the white point value of the color space. The chromaticity coordinates [x, y] are returned, indicating the coordinates of the white point in the color space.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-ColorSpaceManager-getWhitePoint(): collections.Array<number>--><!--Device-ColorSpaceManager-getWhitePoint(): collections.Array<number>-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| collections.Array&lt;number&gt; | Coordinates [x, y] of the white point. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) | The parameter value is abnormal.<br>**Applicable version:** 12 - 22 |

## Examples

```TypeScript
import { collections } from '@kit.ArkTS';
let point: collections.Array<number> = colorSpace.getWhitePoint();
```

