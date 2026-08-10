# DataDeleteOperation

删除单个数据。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface DataDeleteOperation--><!--Device-unnamed-export interface DataDeleteOperation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count?: int
```

删除数据数量，默认为1。

**Type:** int

**Default:** 1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataDeleteOperation-count?: int--><!--Device-DataDeleteOperation-count?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: int
```

起始删除位置索引值。取值范围是[0, 数据源长度-1]。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataDeleteOperation-index: int--><!--Device-DataDeleteOperation-index: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: DataOperationType
```

数据删除类型。

**Type:** [DataOperationType](arkts-arkui-lazyforeach-dataoperationtype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataDeleteOperation-type: DataOperationType--><!--Device-DataDeleteOperation-type: DataOperationType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

