# ColorSpaceManager

Implements management of color space objects.

Before calling any of the following APIs, you must use [create()](arkts-arkgraphics2d-colorspacemanager-create-f.md#create) to create a color space manager.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-colorSpaceManager-interface ColorSpaceManager--><!--Device-colorSpaceManager-interface ColorSpaceManager-End-->

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

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ColorSpaceManager-getColorSpaceName(): ColorSpace--><!--Device-ColorSpaceManager-getColorSpaceName(): ColorSpace-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ColorSpace](../../apis-arkui/arkts-apis/arkts-arkui-window-colorspace-e.md) | Color space type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) | The parameter value is abnormal.<br>**Applicable version:** 9 - 22 |

## Examples

```TypeScript
try {
    let spaceName = colorSpace.getColorSpaceName();
} catch (err) {
    console.error(`Fail to get colorSpace's name. Cause: ` + JSON.stringify(err));
}
```

## getGamma

ArkTS-Dyn:
```TypeScript
getGamma(): number
```

ArkTS-Sta:
```TypeScript
getGamma(): double
```

Obtains the gamma of the color space.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ColorSpaceManager-getGamma(): double--><!--Device-ColorSpaceManager-getGamma(): double-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Gamma of the color space. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) | The parameter value is abnormal.<br>**Applicable version:** 9 - 22 |

## Examples

```TypeScript
try {
    let gamma = colorSpace.getGamma();
} catch (err) {
    console.error(`Failed to get gamma. Cause: ` + JSON.stringify(err));
}
```

## getWhitePoint

ArkTS-Dyn:
```TypeScript
getWhitePoint(): Array<number>
```

ArkTS-Sta:
```TypeScript
getWhitePoint(): Array<double>
```

Obtains the coordinates of the white point in the color space.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ColorSpaceManager-getWhitePoint(): Array<double>--><!--Device-ColorSpaceManager-getWhitePoint(): Array<double>-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt; | Coordinates [x, y] of the white point. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) | The parameter value is abnormal.<br>**Applicable version:** 9 - 22 |

## Examples

```TypeScript
try {
    let point = colorSpace.getWhitePoint();
} catch (err) {
    console.error(`Failed to get white point. Cause: ` + JSON.stringify(err));
}
```

