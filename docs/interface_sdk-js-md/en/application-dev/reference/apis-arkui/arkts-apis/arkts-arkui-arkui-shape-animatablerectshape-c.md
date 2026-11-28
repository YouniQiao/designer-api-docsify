# AnimatableRectShape

```TypeScript
export declare class AnimatableRectShape extends BaseShape<AnimatableRectShape>
```

Represents an animatable rectangle shape used in the [clipShape](../arkts-components/arkts-arkui-common-comp-commonmethod-c.md#clipshape) API. Unlike [RectShape](arkts-arkui-arkui-shape-rectshape-c.md), the width and height of an **AnimatableRectShape** can be animated through [animateTo](arkts-arkui-arkui-uicontext-uicontext-c.md#animateto) or animation.

This API inherits from [BaseShape](arkts-arkui-arkui-shape-baseshape-c.md).

**Inheritance/Implementation:** AnimatableRectShape extends BaseShape&lt;AnimatableRectShape&gt;

**Since:** 26.1.0

<!--Device-unnamed-export declare class AnimatableRectShape extends BaseShape<AnimatableRectShape>--><!--Device-unnamed-export declare class AnimatableRectShape extends BaseShape<AnimatableRectShape>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape, AnimatableRectShape, CircleShape, EllipseShape, PathShape } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: RectShapeOptions | RoundRectShapeOptions)
```

A constructor used to create an **AnimatableRectShape** object.

> **NOTE:** 
> 
> - **radius**, **radiusWidth**, and **radiusHeight** in the constructor parameters set the same properties as
> **radius()**, **radiusWidth()**, and **radiusHeight()**.
> 
> - A method call overrides the corresponding property value set in the constructor.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AnimatableRectShape-constructor(options?: RectShapeOptions | RoundRectShapeOptions)--><!--Device-AnimatableRectShape-constructor(options?: RectShapeOptions | RoundRectShapeOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RectShapeOptions](arkts-arkui-arkui-shape-rectshapeoptions-i.md) &#124; [RoundRectShapeOptions](arkts-arkui-arkui-shape-roundrectshapeoptions-i.md) | No | Rectangle parameters. If not passed in, the default size is used, with a default width of 0 vp, a default height of 0 vp, and a default corner radius of 0 vp. |

## radius

```TypeScript
radius(radius: number | string | Array<number | string>): AnimatableRectShape
```

Sets the radius of the rectangle border corners. After setting, the arc width and height of each corner are equal (circular arc). Unlike **radiusWidth** or **radiusHeight**, which sets the arc width or height separately (allowing the elliptical arc), **radius** can specify the radius values of the four corners separately through an array. Use **radius** when circular corners are required, and use **radiusWidth** and **radiusHeight** when elliptical corners are required.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AnimatableRectShape-radius(radius: number | string | Array<number | string>): AnimatableRectShape--><!--Device-AnimatableRectShape-radius(radius: number | string | Array<number | string>): AnimatableRectShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | number &#124; string &#124; Array&lt;number &#124; string&gt; | Yes | Corner radius of the rectangle shape. Only the first four elements of the array are accepted, which represent the corner radii of the top-left, top-right, bottom-left, and bottom-right corners of the rectangle, respectively. <br>If the type is number, the value range is [0, +∞); if the type is string, the value is specified by [Length](arkts-arkui-length-t.md). <br>Unit: vp <br>If the value is abnormal, 0 vp is used. |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatableRectShape](arkts-arkui-arkui-shape-animatablerectshape-c.md) | **AnimatableRectShape** object, which can be used for chained calls. |

## radiusHeight

```TypeScript
radiusHeight(rHeight: number | string): AnimatableRectShape
```

Sets the radius height of the rectangle border corners.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AnimatableRectShape-radiusHeight(rHeight: number | string): AnimatableRectShape--><!--Device-AnimatableRectShape-radiusHeight(rHeight: number | string): AnimatableRectShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rHeight | number &#124; string | Yes | Height of the corner radius of the rectangle shape. If the type is number, the value range is [0, +∞); if the type is string, the value is specified by [Length](arkts-arkui-length-t.md). Unit: vp. If the value is abnormal, 0 vp is used. |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatableRectShape](arkts-arkui-arkui-shape-animatablerectshape-c.md) | **AnimatableRectShape** object, which can be used for chained calls. |

## radiusWidth

```TypeScript
radiusWidth(rWidth: number | string): AnimatableRectShape
```

Sets the radius width of the rectangle border corners.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AnimatableRectShape-radiusWidth(rWidth: number | string): AnimatableRectShape--><!--Device-AnimatableRectShape-radiusWidth(rWidth: number | string): AnimatableRectShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rWidth | number &#124; string | Yes | Width of the corner radius of the rectangle shape. <br>If the type is number, the value range is [0, +∞); if the type is string, the value is specified by [Length](arkts-arkui-length-t.md). <br>Unit: vp <br>If the value is abnormal, 0 vp is used. |

**Return value:**

| Type | Description |
| --- | --- |
| [AnimatableRectShape](arkts-arkui-arkui-shape-animatablerectshape-c.md) | **AnimatableRectShape** object, which can be used for chained calls. |
