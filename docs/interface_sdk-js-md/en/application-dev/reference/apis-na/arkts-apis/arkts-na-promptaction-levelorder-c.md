# LevelOrder

Defines level order.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class LevelOrder--><!--Device-unnamed-export declare class LevelOrder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## clamp

```TypeScript
static clamp(order: double): LevelOrder
```

Generate valid level order.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LevelOrder-static clamp(order: double): LevelOrder--><!--Device-LevelOrder-static clamp(order: double): LevelOrder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| order | double | Yes | Clamp order with minimum number -100000 and maximum number 100000. |

**Return value:**

| Type | Description |
| --- | --- |
| [LevelOrder](../../apis-arkui/arkts-apis/arkts-arkui-promptaction-levelorder-c.md) | the order object. |

## getOrder

```TypeScript
getOrder(): double
```

Get the order from LevelOrder object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LevelOrder-getOrder(): double--><!--Device-LevelOrder-getOrder(): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| double | the order number. |

