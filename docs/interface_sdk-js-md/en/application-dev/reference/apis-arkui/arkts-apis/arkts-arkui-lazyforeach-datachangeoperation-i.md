# DataChangeOperation

执行单个数据的插入、更新或删除。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface DataChangeOperation--><!--Device-unnamed-export interface DataChangeOperation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: int
```

改变的数据的索引值。取值范围是[0, 数据源长度-1]。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataChangeOperation-index: int--><!--Device-DataChangeOperation-index: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key?: string
```

为改变的数据分配新的键值，默认使用原键值。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataChangeOperation-key?: string--><!--Device-DataChangeOperation-key?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: DataOperationType
```

数据改变类型。

**Type:** [DataOperationType](arkts-arkui-lazyforeach-dataoperationtype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataChangeOperation-type: DataOperationType--><!--Device-DataChangeOperation-type: DataOperationType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

