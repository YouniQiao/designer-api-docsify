# create

## Modules to Import

```TypeScript
import { colorSpaceManager } from '@kit.ArkGraphics2D';
```

## create

```TypeScript
function create(colorSpaceName: ColorSpace): ColorSpaceManager
```

Creates a standard color space object.

**Since:** 23

**Deprecated since:** -1

<!--Device-colorSpaceManager-function create(colorSpaceName: ColorSpace): ColorSpaceManager--><!--Device-colorSpaceManager-function create(colorSpaceName: ColorSpace): ColorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorSpaceName | [ColorSpace](../../apis-arkui/arkts-apis/arkts-arkui-window-colorspace-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorSpaceManager](arkts-arkgraphics2d-colorspacemanager-colorspacemanager-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) |

## Examples

```TypeScript
try {
  // Create a color management instance for the criterion sRGB color space.
  let colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);
} catch (err) {
  console.error(`Failed to create SRGB colorSpace. Code: ${err.code}, message: ${err.message}`);
}
```


## create

```TypeScript
function create(primaries: ColorSpacePrimaries, gamma: number): ColorSpaceManager
```

Creates a custom color space object.

**Since:** 23

**Deprecated since:** -1

<!--Device-colorSpaceManager-function create(primaries: ColorSpacePrimaries, gamma: double): ColorSpaceManager--><!--Device-colorSpaceManager-function create(primaries: ColorSpacePrimaries, gamma: double): ColorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| primaries | [ColorSpacePrimaries](arkts-arkgraphics2d-colorspacemanager-colorspaceprimaries-i.md) | Yes |
| gamma | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorSpaceManager](arkts-arkgraphics2d-colorspacemanager-colorspacemanager-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) |

## Examples

```TypeScript
try {
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
  let gamma = 2.2;
  // Create a custom color space object.
  let colorSpace = colorSpaceManager.create(primaries, gamma);
} catch (err) {
  console.error(`Failed to create colorSpace with customized primaries and gamma. Code: ${err.code}, message: ${err.message}`);
}
```
