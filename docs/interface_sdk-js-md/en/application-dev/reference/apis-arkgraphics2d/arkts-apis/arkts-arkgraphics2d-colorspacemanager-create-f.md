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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-colorSpaceManager-function create(colorSpaceName: ColorSpace): ColorSpaceManager--><!--Device-colorSpaceManager-function create(colorSpaceName: ColorSpace): ColorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorSpaceName | ColorSpace | Yes | Type of the color space. &lt;br&gt;**UNKNOWN** and **CUSTOM** cannot be used when creating standard color space objects. |

**Return value:**

| Type | Description |
| --- | --- |
| ColorSpaceManager | Color space object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| [18600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkgraphics2d/errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) | The parameter value is abnormal. |

## Examples

```TypeScript
let colorSpace: colorSpaceManager.ColorSpaceManager;
try {
    colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);
} catch (err) {
    console.error(`Failed to create SRGB colorSpace. Cause: ` + JSON.stringify(err));
}
```


## create

```TypeScript
function create(primaries: ColorSpacePrimaries, gamma: double): ColorSpaceManager
```

Creates a custom color space object.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-colorSpaceManager-function create(primaries: ColorSpacePrimaries, gamma: double): ColorSpaceManager--><!--Device-colorSpaceManager-function create(primaries: ColorSpacePrimaries, gamma: double): ColorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| primaries | [ColorSpacePrimaries](arkts-arkgraphics2d-colorspacemanager-colorspaceprimaries-i.md) | Yes | Primaries of the color space. |
| gamma | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Gamma value of the color space, which is a floating point number greater than 0. |

**Return value:**

| Type | Description |
| --- | --- |
| ColorSpaceManager | Color space object created. &lt;br&gt;The color space type is **CUSTOM** of [ColorSpace]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| [18600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkgraphics2d/errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) | The parameter value is abnormal. |

## Examples

```TypeScript
let colorSpace: colorSpaceManager.ColorSpaceManager;
try {
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
    let gamma = 2.2;
    colorSpace = colorSpaceManager.create(primaries, gamma);
} catch (err) {
    console.error(`Failed to create colorSpace with customized primaries and gamma. Cause: ` + JSON.stringify(err));
}
```

