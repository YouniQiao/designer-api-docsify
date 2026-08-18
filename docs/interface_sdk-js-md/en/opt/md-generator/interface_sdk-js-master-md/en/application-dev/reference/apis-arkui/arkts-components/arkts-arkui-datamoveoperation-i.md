# DataMoveOperation

Represents an operation for moving data.

**Since:** 12

<!--Device-unnamed-interface DataMoveOperation--><!--Device-unnamed-interface DataMoveOperation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## index

```TypeScript
index: MoveIndex
```

Positions for the movement. The value range is [0, data source length - 1].

**Type:** [MoveIndex](arkts-arkui-moveindex-i.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataMoveOperation-index: MoveIndex--><!--Device-DataMoveOperation-index: MoveIndex-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key?: string
```

New key to assign to the moved data. The original key is used by default.

**Type:** string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataMoveOperation-key?: string--><!--Device-DataMoveOperation-key?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: DataOperationType.MOVE
```

Type of data movement.

**Type:** [DataOperationType.MOVE](arkts-arkui-dataoperationtype-e.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataMoveOperation-type: DataOperationType.MOVE--><!--Device-DataMoveOperation-type: DataOperationType.MOVE-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
