# DataMoveOperation

移动数据操作。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface DataMoveOperation--><!--Device-unnamed-interface DataMoveOperation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: MoveIndex
```

移动位置。取值范围是[0, 数据源长度-1]。超出取值范围时渲染异常。

**Type:** [MoveIndex](arkts-arkui-moveindex-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataMoveOperation-index: MoveIndex--><!--Device-DataMoveOperation-index: MoveIndex-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key?: string
```

为被移动的数据分配新的键值，默认使用原键值。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataMoveOperation-key?: string--><!--Device-DataMoveOperation-key?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: DataOperationType.MOVE
```

数据移动类型。

**Type:** DataOperationType.MOVE

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataMoveOperation-type: DataOperationType.MOVE--><!--Device-DataMoveOperation-type: DataOperationType.MOVE-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

