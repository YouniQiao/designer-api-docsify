# BaseShape

继承自[CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)。

**Inheritance/Implementation:** BaseShape extends [CommonShapeMethod](arkts-arkui-arkui-shape-commonshapemethod-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class BaseShape extends CommonShapeMethod--><!--Device-unnamed-export declare class BaseShape extends CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape, CircleShape, EllipseShape, PathShape } from 'kits/@kit.ArkUI';
```

## height

```TypeScript
height(height: Length): this
```

设置形状的高度。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseShape-height(height: Length): this--><!--Device-BaseShape-height(height: Length): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| height | [Length](arkts-arkui-length-t.md) | Yes | 形状的高度。&lt;br/&gt;单位：vp&lt;br/&gt;取值为异常值时按照0vp处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前对象。 |

## size

```TypeScript
size(size: SizeOptions): this
```

设置形状的大小。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseShape-size(size: SizeOptions): this--><!--Device-BaseShape-size(size: SizeOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | [SizeOptions](arkts-arkui-sizeoptions-i.md) | Yes | 形状的大小。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前对象。 |

## width

```TypeScript
width(width: Length): this
```

设置形状的宽度。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseShape-width(width: Length): this--><!--Device-BaseShape-width(width: Length): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | [Length](arkts-arkui-length-t.md) | Yes | 形状的宽度。&lt;br/&gt;单位：vp&lt;br/&gt;取值为异常值时按照0vp处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前对象。 |

