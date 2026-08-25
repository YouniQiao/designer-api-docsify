# ColorSpaceManager

Implements management of color space objects.Before calling any of the following APIs, you must use [create()](arkts-arkgraphics2d-colorspacemanager-create-f.md) to create a color space manager.

**Since:** 9

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

## Modules to Import

```TypeScript
import { colorSpaceManager } from 'kits/@kit.ArkGraphics2D';
```

## getColorSpaceName

```TypeScript
getColorSpaceName(): ColorSpace
```

Obtains the color space type.

**Since:** 9

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorSpace](../../apis-arkui/arkts-apis/arkts-arkui-window-colorspace-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) |

## getGamma

```TypeScript
getGamma(): number
```

Obtains the gamma of the color space.

**Since:** 9

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) |

## getWhitePoint

```TypeScript
getWhitePoint(): Array<number>
```

Obtains the coordinates of the white point in the color space.

**Since:** 9

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) |
