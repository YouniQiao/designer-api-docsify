# ColorSpaceManager

Implements management of color space objects. ColorSpaceManager is a core class used to manage and operate color space objects. It provides functions such as obtaining the color space type, white point value, and gamma value, and supports transfer between concurrent ArkTS instances.

Before calling any of the following APIs, you must use [create()](arkts-arkgraphics2d-sendablecolorspacemanager-create-f.md#create) to create a color space manager.

**Inheritance/Implementation:** ColorSpaceManager extends [ISendable](arkts-arkgraphics2d-sendablecolorspacemanager-isendable-t.md)

**Since:** 12

<!--Device-sendableColorSpaceManager-interface ColorSpaceManager extends ISendable--><!--Device-sendableColorSpaceManager-interface ColorSpaceManager extends ISendable-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

## Modules to Import

```TypeScript
import { sendableColorSpaceManager } from 'kits/@kit.ArkGraphics2D';
```

## getColorSpaceName

```TypeScript
getColorSpaceName(): colorSpaceManager.ColorSpace
```

Obtains the color space type.

**Since:** 12

<!--Device-ColorSpaceManager-getColorSpaceName(): colorSpaceManager.ColorSpace--><!--Device-ColorSpaceManager-getColorSpaceName(): colorSpaceManager.ColorSpace-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| colorSpaceManager.ColorSpace |

**Error codes:**

| Error Code ID |
| --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) |

## Examples

```TypeScript
// Obtain the color space type.
let spaceName: colorSpaceManager.ColorSpace = colorSpace.getColorSpaceName();
```

## getGamma

```TypeScript
getGamma(): number
```

Obtains the gamma of the color space.

**Since:** 12

<!--Device-ColorSpaceManager-getGamma(): number--><!--Device-ColorSpaceManager-getGamma(): number-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) |

## Examples

```TypeScript
// Obtain the gamma value of the color space.
let gamma: number = colorSpace.getGamma();
```

## getWhitePoint

```TypeScript
getWhitePoint(): collections.Array<number>
```

Obtains the white point value of the color space. The chromaticity coordinates [x, y] are returned, indicating the coordinates of the white point in the color space.

**Since:** 12

<!--Device-ColorSpaceManager-getWhitePoint(): collections.Array<number>--><!--Device-ColorSpaceManager-getWhitePoint(): collections.Array<number>-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| collections.Array&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) |

## Examples

```TypeScript
import { collections } from '@kit.ArkTS';
// Obtain the white point value [x, y] of the color space.
let point: collections.Array<number> = colorSpace.getWhitePoint();
```
