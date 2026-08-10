# DataAddOperation

添加数据操作。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface DataAddOperation--><!--Device-unnamed-interface DataAddOperation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
count?: number
```

添加数量，必须是正整数（大于0），默认为1。传入0或负数时可能导致渲染效果异常。

**Type:** number

**Default:** 1

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataAddOperation-count?: number--><!--Device-DataAddOperation-count?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: number
```

添加数据索引值。取值范围是[0, 数据源长度]。超出取值范围时渲染异常。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataAddOperation-index: number--><!--Device-DataAddOperation-index: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key?: string | Array<string>
```

为添加的数据分配键值，默认使用原键值。键值支持string或Array&lt;string&gt;类型；当键值为数组且长度大于count时报参数无效错误。

**Type:** string \| Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataAddOperation-key?: string | Array<string>--><!--Device-DataAddOperation-key?: string | Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: DataOperationType.ADD
```

数据添加类型。

**Type:** DataOperationType.ADD

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataAddOperation-type: DataOperationType.ADD--><!--Device-DataAddOperation-type: DataOperationType.ADD-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

