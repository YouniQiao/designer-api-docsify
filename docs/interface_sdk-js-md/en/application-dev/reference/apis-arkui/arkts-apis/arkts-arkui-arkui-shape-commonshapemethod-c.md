# CommonShapeMethod

常见的形状方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class CommonShapeMethod--><!--Device-unnamed-export declare class CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape, CircleShape, EllipseShape, PathShape } from 'kits/@kit.ArkUI';
```

## fill

```TypeScript
fill(color: ResourceColor): this
```

设置形状的填充区域的透明度，黑色表示完全透明，白色表示完全不透明。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonShapeMethod-fill(color: ResourceColor): this--><!--Device-CommonShapeMethod-fill(color: ResourceColor): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) | Yes | 形状的填充区域的透明度，黑色表示完全透明，白色表示完全不透明。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前对象。 |

## offset

```TypeScript
offset(offset: Position): this
```

设置相对于组件布局位置的坐标偏移。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonShapeMethod-offset(offset: Position): this--><!--Device-CommonShapeMethod-offset(offset: Position): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | [Position](arkts-arkui-position-i.md) | Yes | 相对于组件布局位置的坐标偏移。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前对象。 |

## position

```TypeScript
position(position: Position): this
```

设置形状的位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CommonShapeMethod-position(position: Position): this--><!--Device-CommonShapeMethod-position(position: Position): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [Position](arkts-arkui-position-i.md) | Yes | 设置形状的位置。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前对象。 |

