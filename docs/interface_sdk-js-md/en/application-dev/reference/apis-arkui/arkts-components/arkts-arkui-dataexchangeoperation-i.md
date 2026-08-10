# DataExchangeOperation

交换数据操作。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface DataExchangeOperation--><!--Device-unnamed-interface DataExchangeOperation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: ExchangeIndex
```

交换位置。取值范围是[0, 数据源长度-1]。超出取值范围时渲染异常。

**Type:** [ExchangeIndex](arkts-arkui-exchangeindex-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataExchangeOperation-index: ExchangeIndex--><!--Device-DataExchangeOperation-index: ExchangeIndex-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key?: ExchangeKey
```

分配新的键值，默认使用原键值。

**Type:** [ExchangeKey](arkts-arkui-exchangekey-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataExchangeOperation-key?: ExchangeKey--><!--Device-DataExchangeOperation-key?: ExchangeKey-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: DataOperationType.EXCHANGE
```

数据交换类型。

**Type:** DataOperationType.EXCHANGE

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DataExchangeOperation-type: DataOperationType.EXCHANGE--><!--Device-DataExchangeOperation-type: DataOperationType.EXCHANGE-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

