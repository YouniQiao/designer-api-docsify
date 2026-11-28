# AnimatableRectShape

```TypeScript
export declare class AnimatableRectShape extends BaseShape<AnimatableRectShape>
```

表示用于[clipShape](../arkts-components/arkts-arkui-common-comp-commonmethod-c.md#clipshape)接口的可动画矩形形状。与[RectShape](arkts-arkui-arkui-shape-rectshape-c.md)不同，AnimatableRectShape的宽高可以通过[animateTo](arkts-arkui-arkui-uicontext-uicontext-c.md#animateto)或animation产生动画。

继承自[BaseShape](arkts-arkui-arkui-shape-baseshape-c.md)。

**继承/实现关系：** AnimatableRectShape extends BaseShape&lt;AnimatableRectShape&gt;

**起始版本：** 26.1.0

<!--Device-unnamed-export declare class AnimatableRectShape extends BaseShape<AnimatableRectShape>--><!--Device-unnamed-export declare class AnimatableRectShape extends BaseShape<AnimatableRectShape>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { RectShape, AnimatableRectShape, CircleShape, EllipseShape, PathShape } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: RectShapeOptions | RoundRectShapeOptions)
```

用于创建AnimatableRectShape对象的构造函数。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-AnimatableRectShape-constructor(options?: RectShapeOptions | RoundRectShapeOptions)--><!--Device-AnimatableRectShape-constructor(options?: RectShapeOptions | RoundRectShapeOptions)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RectShapeOptions](arkts-arkui-arkui-shape-rectshapeoptions-i.md) &#124; [RoundRectShapeOptions](arkts-arkui-arkui-shape-roundrectshapeoptions-i.md) | 否 | 矩形参数。如果不传入，使用默认尺寸，默认宽度为0vp，默认高度为0vp，默认圆角半径为0vp。 |

## radius

```TypeScript
radius(radius: number | string | Array<number | string>): AnimatableRectShape
```

设置矩形边框圆角的半径。设置后，每个角的弧宽和弧高相等（圆弧）。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-AnimatableRectShape-radius(radius: number | string | Array<number | string>): AnimatableRectShape--><!--Device-AnimatableRectShape-radius(radius: number | string | Array<number | string>): AnimatableRectShape-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number &#124; string &#124; Array&lt;number &#124; string&gt; | 是 | 矩形形状的圆角半径。仅接受数组的前四个元素，分别为矩形左上、右上、左下、右下的圆角半径。<br>若类型为number，有效值范围为[0, +∞)，若类型为string，该值必须符合[Length](arkts-arkui-length-t.md)类型规范。<br>单位：vp。<br>取值为异常值时按照0vp处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimatableRectShape](arkts-arkui-arkui-shape-animatablerectshape-c.md) | AnimatableRectShape对象，可用于链式调用。 |

## radiusHeight

```TypeScript
radiusHeight(rHeight: number | string): AnimatableRectShape
```

设置矩形边框圆角的半径高度。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-AnimatableRectShape-radiusHeight(rHeight: number | string): AnimatableRectShape--><!--Device-AnimatableRectShape-radiusHeight(rHeight: number | string): AnimatableRectShape-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rHeight | number &#124; string | 是 | 矩形形状圆角半径的高度。 <br> 若类型为number，有效值范围为[0, +∞)，若类型为string，该值必须符合[Length](arkts-arkui-length-t.md)类型规范。<br>单位：vp<br>取值为异常值时按照0vp处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimatableRectShape](arkts-arkui-arkui-shape-animatablerectshape-c.md) | AnimatableRectShape对象，可用于链式调用。 |

## radiusWidth

```TypeScript
radiusWidth(rWidth: number | string): AnimatableRectShape
```

设置矩形边框圆角的半径宽度。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-AnimatableRectShape-radiusWidth(rWidth: number | string): AnimatableRectShape--><!--Device-AnimatableRectShape-radiusWidth(rWidth: number | string): AnimatableRectShape-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rWidth | number &#124; string | 是 | 矩形形状圆角半径的宽度。<br> 若类型为number，有效值范围为[0, +∞)，若类型为string，该值必须符合[Length](arkts-arkui-length-t.md)类型规范。<br>单位：vp<br>取值为异常值时按照0vp处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimatableRectShape](arkts-arkui-arkui-shape-animatablerectshape-c.md) | AnimatableRectShape对象，可用于链式调用。 |
