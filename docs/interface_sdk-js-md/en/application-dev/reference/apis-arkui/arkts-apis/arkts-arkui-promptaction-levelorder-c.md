# LevelOrder

弹窗层级，可以控制弹窗显示的顺序。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class LevelOrder--><!--Device-unnamed-export declare class LevelOrder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## clamp

```TypeScript
static clamp(order: double): LevelOrder
```

创建指定顺序的弹窗层级。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LevelOrder-static clamp(order: double): LevelOrder--><!--Device-LevelOrder-static clamp(order: double): LevelOrder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| order | double | Yes | 弹窗显示顺序。取值范围为[-100000.0, 100000.0]，如果值小于-100000.0则设置为-100000.0，如果值大于100000.0则设置为100000.0。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LevelOrder](arkts-arkui-promptaction-levelorder-c.md) | 返回当前对象实例。 |

## getOrder

```TypeScript
getOrder(): double
```

获取弹窗显示顺序。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LevelOrder-getOrder(): double--><!--Device-LevelOrder-getOrder(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | 返回显示顺序数值。 |

