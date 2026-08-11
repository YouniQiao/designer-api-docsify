# RectShape

Represents a rectangle shape used in the **clipShape** and **maskShape** APIs.

This API inherits from [BaseShape](arkts-arkui-arkui-shape-baseshape-c.md).

**Inheritance/Implementation:** RectShape extends [BaseShape<RectShape>](BaseShape<RectShape>)

**Since:** 12

<!--Device-unnamed-export declare class RectShape extends BaseShape<RectShape>--><!--Device-unnamed-export declare class RectShape extends BaseShape<RectShape>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape, CircleShape, EllipseShape, PathShape } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: RectShapeOptions | RoundRectShapeOptions)
```

A constructor used to create a **RectShape** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-RectShape-constructor(options?: RectShapeOptions | RoundRectShapeOptions)--><!--Device-RectShape-constructor(options?: RectShapeOptions | RoundRectShapeOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RectShapeOptions](arkts-arkui-arkui-shape-rectshapeoptions-i.md) \| [RoundRectShapeOptions](arkts-arkui-arkui-shape-roundrectshapeoptions-i.md) | No |

## radius

```TypeScript
radius(radius: number | string | Array<number | string>): RectShape
```

Sets the radius of the rectangle border corners.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-RectShape-radius(radius: number | string | Array<number | string>): RectShape--><!--Device-RectShape-radius(radius: number | string | Array<number | string>): RectShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [radius](#radius) | number \| string \| Array&lt;number \| string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RectShape](arkts-arkui-arkui-shape-rectshape-c.md) |

## radiusHeight

```TypeScript
radiusHeight(rHeight: number | string): RectShape
```

Sets the radius height of the rectangle border corners.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-RectShape-radiusHeight(rHeight: number | string): RectShape--><!--Device-RectShape-radiusHeight(rHeight: number | string): RectShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rHeight | number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RectShape](arkts-arkui-arkui-shape-rectshape-c.md) |

## radiusWidth

```TypeScript
radiusWidth(rWidth: number | string): RectShape
```

Sets the radius width of the rectangle border corners.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-RectShape-radiusWidth(rWidth: number | string): RectShape--><!--Device-RectShape-radiusWidth(rWidth: number | string): RectShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rWidth | number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RectShape](arkts-arkui-arkui-shape-rectshape-c.md) |
