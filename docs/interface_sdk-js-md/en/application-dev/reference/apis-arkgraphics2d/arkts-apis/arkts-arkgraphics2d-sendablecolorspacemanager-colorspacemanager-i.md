# ColorSpaceManager

当前可共享的色彩管理实例。ColorSpaceManager是用于管理和操作色域对象的核心类，提供了获取色域类型、白点值、gamma值等功能，并支持在ArkTS并发实例间传递。

下列API示例中都需先使用[create()](arkts-arkgraphics2d-sendablecolorspacemanager-create-f.md#create)获取到ColorSpaceManager实例，再通过此实例调用对应方法。

**Inheritance/Implementation:** ColorSpaceManager extends [ISendable](arkts-arkgraphics2d-sendablecolorspacemanager-isendable-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

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

获取色域类型。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ColorSpaceManager-getColorSpaceName(): colorSpaceManager.ColorSpace--><!--Device-ColorSpaceManager-getColorSpaceName(): colorSpaceManager.ColorSpace-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| colorSpaceManager.ColorSpace | 返回色域类型枚举值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 18600001 | The parameter value is abnormal.<br>**Applicable version:** 12 - 22 |

## Examples

```TypeScript
// Obtain the color space type.
let spaceName: colorSpaceManager.ColorSpace = colorSpace.getColorSpaceName();
```

## getGamma

```TypeScript
getGamma(): number
```

获取色域gamma值。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ColorSpaceManager-getGamma(): number--><!--Device-ColorSpaceManager-getGamma(): number-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回色域gamma值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 18600001 | The parameter value is abnormal.<br>**Applicable version:** 12 - 22 |

## Examples

```TypeScript
// Obtain the gamma value of the color space.
let gamma: number = colorSpace.getGamma();
```

## getWhitePoint

```TypeScript
getWhitePoint(): collections.Array<number>
```

获取色域白点值，返回色度坐标[x, y]，表示色彩空间中白色点的坐标位置。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-ColorSpaceManager-getWhitePoint(): collections.Array<number>--><!--Device-ColorSpaceManager-getWhitePoint(): collections.Array<number>-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| collections.Array&lt;number&gt; | 返回色域白点值[x, y]。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 18600001 | The parameter value is abnormal.<br>**Applicable version:** 12 - 22 |

## Examples

```TypeScript
import { collections } from '@kit.ArkTS';
// Obtain the white point value [x, y] of the color space.
let point: collections.Array<number> = colorSpace.getWhitePoint();
```

