# ColorSpaceManager

当前色域对象实例。

下列API示例中都需先使用[create()](arkts-arkgraphics2d-colorspacemanager-create-f.md#create)获取到ColorSpaceManager实例，再通过此实例调用对应方法。

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

获取色域类型。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ColorSpaceManager-getColorSpaceName(): ColorSpace--><!--Device-ColorSpaceManager-getColorSpaceName(): ColorSpace-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ColorSpace](../../apis-arkui/arkts-apis/arkts-arkui-window-colorspace-e.md) | 返回色域类型枚举值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 18600001 | The parameter value is abnormal.<br>**Applicable version:** 9 - 22 |

## Examples

```TypeScript
try {
  // Obtain the color space type.
  let spaceName = colorSpace.getColorSpaceName();
  console.info(`spaceName: ` + spaceName.toString());
} catch (err) {
  console.error(`Failed to get colorSpace's name. Code: ${err.code}, message: ${err.message}`);
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

获取色域gamma值。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ColorSpaceManager-getGamma(): double--><!--Device-ColorSpaceManager-getGamma(): double-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 返回色域gamma值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 18600001 | The parameter value is abnormal.<br>**Applicable version:** 9 - 22 |

## Examples

```TypeScript
try {
  // Obtain the gamma value of the color space.
  let gamma = colorSpace.getGamma();
  console.info(`gamma: ` + gamma.toString());
} catch (err) {
  console.error(`Failed to get gamma. Code: ${err.code}, message: ${err.message}`);
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

获取色域白点值。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ColorSpaceManager-getWhitePoint(): Array<double>--><!--Device-ColorSpaceManager-getWhitePoint(): Array<double>-End-->

**System capability:** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt; | 返回色域白点值[x, y]。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 18600001 | The parameter value is abnormal.<br>**Applicable version:** 9 - 22 |

## Examples

```TypeScript
try {
  // Obtain the white point value of the color space.
  let point = colorSpace.getWhitePoint();
  console.info(`point: ` + point.toString());
} catch (err) {
  console.error(`Failed to get white point. Code: ${err.code}, message: ${err.message}`);
}
```

