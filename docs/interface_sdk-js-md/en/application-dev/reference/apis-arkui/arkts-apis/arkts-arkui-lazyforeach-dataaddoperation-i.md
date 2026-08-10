# DataAddOperation

添加单个数据。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface DataAddOperation--><!--Device-unnamed-export interface DataAddOperation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count?: int
```

插入数量，默认为1。

**Type:** int

**Default:** 1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataAddOperation-count?: int--><!--Device-DataAddOperation-count?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: int
```

插入数据索引值。取值范围是[0, 数据源长度-1]。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataAddOperation-index: int--><!--Device-DataAddOperation-index: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key?: string | Array<string>
```

为插入的数据分配键值。

**Type:** string \| Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataAddOperation-key?: string | Array<string>--><!--Device-DataAddOperation-key?: string | Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: DataOperationType
```

数据添加类型。

**Type:** [DataOperationType](arkts-arkui-lazyforeach-dataoperationtype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataAddOperation-type: DataOperationType--><!--Device-DataAddOperation-type: DataOperationType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

