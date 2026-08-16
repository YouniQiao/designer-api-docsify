# BaseShape

This API inherits from [CommonShapeMethod](../../apis-na/arkts-apis/arkts-na-arkui-shape-commonshapemethod-c.md#CommonShapeMethod).

**Inheritance/Implementation:** BaseShape extends CommonShapeMethod<T>

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-declare class BaseShape--><!--Device-unnamed-declare class BaseShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape } from 'RectShape';
import { CircleShape } from 'CircleShape';
import { EllipseShape } from 'EllipseShape';
import { PathShape } from 'PathShape';
```

## height

```TypeScript
height(height: Length): T
```

Sets the height of a shape.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BaseShape-height(height: Length): T--><!--Device-BaseShape-height(height: Length): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| height | Length | Yes | Height of the shape.<br>Unit: vp.<br>If the value is invalid, 0 vp is used. |

**Return value:**

| Type | Description |
| --- | --- |
| T | Current object. |

## size

```TypeScript
size(size: SizeOptions): T
```

Sets the size of a shape.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BaseShape-size(size: SizeOptions): T--><!--Device-BaseShape-size(size: SizeOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | SizeOptions | Yes | Size of the shape. |

**Return value:**

| Type | Description |
| --- | --- |
| T | Current object. |

## width

```TypeScript
width(width: Length): T
```

Sets the width of a shape.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BaseShape-width(width: Length): T--><!--Device-BaseShape-width(width: Length): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | Length | Yes | Width of the shape.<br>Unit: vp.<br>If the value is invalid, 0 vp is used. |

**Return value:**

| Type | Description |
| --- | --- |
| T | Current object. |

