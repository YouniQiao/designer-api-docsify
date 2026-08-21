# EllipseShape

Represents an ellipse shape used in the **clipShape** and **maskShape** APIs.

This API inherits from [BaseShape](../../apis-default/arkts-apis/arkts-arkuishape-baseshape-c.md).

**Inheritance/Implementation:** EllipseShape extends BaseShape<EllipseShape>

**Since:** 12

<!--Device-unnamed-export declare class EllipseShape--><!--Device-unnamed-export declare class EllipseShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape, CircleShape, EllipseShape, PathShape } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ShapeSize)
```

A constructor used to create a **EllipseShape** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-EllipseShape-constructor(options?: ShapeSize)--><!--Device-EllipseShape-constructor(options?: ShapeSize)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ShapeSize](../../apis-default/arkts-apis/arkts-arkuishape-shapesize-i.md) | No | Size of the shape. |

