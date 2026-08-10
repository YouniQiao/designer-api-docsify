# create

## Modules to Import

```TypeScript
import { sendableColorSpaceManager } from 'kits/@kit.ArkGraphics2D';
```

## create

```TypeScript
function create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager
```

创建标准可共享的色彩管理实例。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-sendableColorSpaceManager-function create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager--><!--Device-sendableColorSpaceManager-function create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorSpaceName | colorSpaceManager.ColorSpace | Yes | 标准色域类型枚举值。 &lt;br&gt;UNKNOWN与CUSTOM不可用于直接创建色域对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorSpaceManager](arkts-arkgraphics2d-colorspacemanager-colorspacemanager-i.md) | 返回当前创建的可共享的色彩管理实例。 &lt;br&gt;该实例继承ISendable，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考 [Sendable使用场景](../../../arkts-utils/sendable-guide.md)。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

## Examples

```TypeScript
import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
// Create a color management instance for the criterion sRGB color space.
colorSpace = sendableColorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);
```


## create

```TypeScript
function create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager
```

创建用户自定义可共享的色彩管理实例。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-sendableColorSpaceManager-function create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager--><!--Device-sendableColorSpaceManager-function create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| primaries | colorSpaceManager.ColorSpacePrimaries | Yes | 色域标准三原色。 |
| gamma | number | Yes | 色域gamma值，取值为大于0的浮点数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ColorSpaceManager](arkts-arkgraphics2d-colorspacemanager-colorspacemanager-i.md) | 返回当前创建的可共享的色彩管理实例。 &lt;br&gt;色域类型定义为[colorSpaceManager.ColorSpace]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

## Examples

```TypeScript
import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
// Define the color space criterion primary colors parameter.
let primaries: colorSpaceManager.ColorSpacePrimaries = {
  redX: 0.1,
  redY: 0.1,
  greenX: 0.2,
  greenY: 0.2,
  blueX: 0.3,
  blueY: 0.3,
  whitePointX: 0.4,
  whitePointY: 0.4
};
// Define the color space gamma value.
let gamma: number = 2.2;
// Create a custom color space management instance that is sendable.
colorSpace = sendableColorSpaceManager.create(primaries, gamma);
```

