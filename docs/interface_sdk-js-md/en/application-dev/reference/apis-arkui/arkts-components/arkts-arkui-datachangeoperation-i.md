# DataChangeOperation

改变数据操作。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface DataChangeOperation--><!--Device-unnamed-interface DataChangeOperation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: number
```

改变的数据的索引值。取值范围是[0, 数据源长度-1]。超出取值范围时渲染异常。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataChangeOperation-index: number--><!--Device-DataChangeOperation-index: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key?: string
```

为改变的数据分配新的键值，默认使用原键值。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataChangeOperation-key?: string--><!--Device-DataChangeOperation-key?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: DataOperationType.CHANGE
```

数据改变类型。

**Type:** DataOperationType.CHANGE

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataChangeOperation-type: DataOperationType.CHANGE--><!--Device-DataChangeOperation-type: DataOperationType.CHANGE-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

