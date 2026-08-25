# create

## Modules to Import

```TypeScript
import { colorSpaceManager } from 'kits/@kit.ArkGraphics2D';
```

## create

```TypeScript
function create(colorSpaceName: ColorSpace): ColorSpaceManager
```

Creates a standard color space object.

**Since:** 9

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorSpaceName | [ColorSpace](../../apis-arkui/arkts-apis/arkts-arkui-window-colorspace-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorSpaceManager](arkts-arkgraphics2d-sendablecolorspacemanager-colorspacemanager-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) |


## create

```TypeScript
function create(primaries: ColorSpacePrimaries, gamma: number): ColorSpaceManager
```

Creates a custom color space object.

**Since:** 9

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| primaries | [ColorSpacePrimaries](arkts-arkgraphics2d-colorspacemanager-colorspaceprimaries-i.md) | Yes |
| gamma | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ColorSpaceManager](arkts-arkgraphics2d-sendablecolorspacemanager-colorspacemanager-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) |
