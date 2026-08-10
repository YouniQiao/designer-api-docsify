# RectShape

用于clipShape和maskShape接口的矩形形状。

继承自[BaseShape](arkts-arkui-arkui-shape-baseshape-c.md)。

**Inheritance/Implementation:** RectShape extends [BaseShape](arkts-arkui-arkui-shape-baseshape-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class RectShape extends BaseShape--><!--Device-unnamed-export declare class RectShape extends BaseShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape, CircleShape, EllipseShape, PathShape } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: RectShapeOptions | RoundRectShapeOptions)
```

创建RectShape对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectShape-constructor(options?: RectShapeOptions | RoundRectShapeOptions)--><!--Device-RectShape-constructor(options?: RectShapeOptions | RoundRectShapeOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectShapeOptions](arkts-arkui-arkui-shape-rectshapeoptions-i.md) \| RoundRectShapeOptions | No | 矩形形状参数。 |

## radius

```TypeScript
radius(radius: double | string | Array<double | string>): this
```

设置矩形形状的圆角半径。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectShape-radius(radius: double | string | Array<double | string>): this--><!--Device-RectShape-radius(radius: double | string | Array<double | string>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | double \| string \| Array&lt;double \| string&gt; | Yes | Array<double |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回RectShape对象。 |

## radiusHeight

```TypeScript
radiusHeight(rHeight: double | string): this
```

设置矩形形状圆角半径的高度。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectShape-radiusHeight(rHeight: double | string): this--><!--Device-RectShape-radiusHeight(rHeight: double | string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rHeight | double \| string | Yes | 矩形形状圆角半径的高度。 &lt;br/&gt; 类型为number时取值范围是 [0, +∞)，类型为string时是[Length](arkts-arkui-length-t.md)。&lt;br/&gt;单位：vp&lt;br/&gt;取值为异常值时按照0vp处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回RectShape对象。 |

## radiusWidth

```TypeScript
radiusWidth(rWidth: double | string): this
```

设置矩形形状圆角半径的宽度。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RectShape-radiusWidth(rWidth: double | string): this--><!--Device-RectShape-radiusWidth(rWidth: double | string): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rWidth | double \| string | Yes | 矩形形状圆角半径的宽度。&lt;br/&gt; 类型为double时取值范围是 [0, +∞)，类型为string时是[Length](arkts-arkui-length-t.md)。&lt;br/&gt;单位：vp&lt;br/&gt;取值为异常值时按照0vp处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前对象。 |

