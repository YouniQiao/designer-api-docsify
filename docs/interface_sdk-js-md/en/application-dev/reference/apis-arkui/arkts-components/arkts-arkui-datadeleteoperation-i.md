# DataDeleteOperation

删除数据操作。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface DataDeleteOperation--><!--Device-unnamed-interface DataDeleteOperation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count?: number
```

删除数据数量，必须是正整数（大于0），且index与count之和不超过数据源长度，默认为1。传入负数时该操作会被忽略；传入0时会异常地将index处的数据项标记删除。index与count之和超过数据源长度时可能导致渲染异常。

**Type:** number

**Default:** 1

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataDeleteOperation-count?: number--><!--Device-DataDeleteOperation-count?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: number
```

起始删除位置索引值。取值范围是[0, 数据源长度-1]。超出取值范围时渲染异常。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataDeleteOperation-index: number--><!--Device-DataDeleteOperation-index: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: DataOperationType.DELETE
```

数据删除类型。

**Type:** DataOperationType.DELETE

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataDeleteOperation-type: DataOperationType.DELETE--><!--Device-DataDeleteOperation-type: DataOperationType.DELETE-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

