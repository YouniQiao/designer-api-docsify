# ColorSpaceManager(Color Space Management)

Implements management of color space objects. Before calling any of the following APIs, you must use [create()](arkts-arkgraphics2d-colorspacemanager-create-f.md) to create a color space manager.

**Since:** 23

<!--Device-colorSpaceManager-interface ColorSpaceManager--><!--Device-colorSpaceManager-interface ColorSpaceManager-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

## Modules to Import

```TypeScript
import { colorSpaceManager } from '@kit.ArkGraphics2D';
```

## getColorSpaceName

```TypeScript
getColorSpaceName(): ColorSpace
```

Obtains the color space type.

**Since:** 23

<!--Device-ColorSpaceManager-getColorSpaceName(): ColorSpace--><!--Device-ColorSpaceManager-getColorSpaceName(): ColorSpace-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| ColorSpace | Color space type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) | The parameter value is abnormal.<br>**Applicable version:** 9 - 22 |

**Examples**

```TypeScript
try {
    let spaceName = colorSpace.getColorSpaceName();
} catch (err) {
    console.error(`Fail to get colorSpace's name. Cause: ` + JSON.stringify(err));
}
```

## getGamma

```TypeScript
getGamma(): double
```

Obtains the gamma of the color space.

**Since:** 23

<!--Device-ColorSpaceManager-getGamma(): double--><!--Device-ColorSpaceManager-getGamma(): double-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| double | Gamma of the color space. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) | The parameter value is abnormal.<br>**Applicable version:** 9 - 22 |

**Examples**

```TypeScript
try {
    let gamma = colorSpace.getGamma();
} catch (err) {
    console.error(`Failed to get gamma. Cause: ` + JSON.stringify(err));
}
```

## getWhitePoint

```TypeScript
getWhitePoint(): Array<double>
```

Obtains the coordinates of the white point in the color space.

**Since:** 23

<!--Device-ColorSpaceManager-getWhitePoint(): Array<double>--><!--Device-ColorSpaceManager-getWhitePoint(): Array<double>-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;double&gt; | Coordinates [x, y] of the white point. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [18600001](../errorcode-colorspace-manager.md#18600001-abnormal-parameter-value) | The parameter value is abnormal.<br>**Applicable version:** 9 - 22 |

**Examples**

```TypeScript
try {
    let point = colorSpace.getWhitePoint();
} catch (err) {
    console.error(`Failed to get white point. Cause: ` + JSON.stringify(err));
}
```

