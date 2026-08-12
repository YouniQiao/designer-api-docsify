# create

## Modules to Import

```TypeScript
import { sendableColorSpaceManager } from '@kit.ArkGraphics2D';
```

## create

```TypeScript
function create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager
```

Creates a criterion color space management instance that is sendable.

**Since:** 12

<!--Device-sendableColorSpaceManager-function create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager--><!--Device-sendableColorSpaceManager-function create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorSpaceName | colorSpaceManager.ColorSpace | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorSpaceManager](arkts-arkgraphics2d-colorspacemanager-colorspacemanager-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [18600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkgraphics2d/errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) |

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

Creates a custom color space object that is sendable.

**Since:** 12

<!--Device-sendableColorSpaceManager-function create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager--><!--Device-sendableColorSpaceManager-function create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| primaries | colorSpaceManager.ColorSpacePrimaries | Yes |
| gamma | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorSpaceManager](arkts-arkgraphics2d-colorspacemanager-colorspacemanager-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [18600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkgraphics2d/errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) |

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
