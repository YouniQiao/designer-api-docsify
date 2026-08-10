# DataOperation

```TypeScript
declare type DataOperation =
  DataAddOperation | DataDeleteOperation | DataChangeOperation | DataMoveOperation | DataExchangeOperation | DataReloadOperation
```

数据操作类型。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type DataOperation =  DataAddOperation | DataDeleteOperation | DataChangeOperation | DataMoveOperation | DataExchangeOperation | DataReloadOperation--><!--Device-unnamed-declare type DataOperation =  DataAddOperation | DataDeleteOperation | DataChangeOperation | DataMoveOperation | DataExchangeOperation | DataReloadOperation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| --- | --- |
| DataAddOperation | 添加数据操作。 |
| DataDeleteOperation | 删除数据操作。 |
| DataChangeOperation | 改变数据操作。 |
| DataMoveOperation | 移动数据操作。 |
| DataExchangeOperation | 交换数据操作。 |
| DataReloadOperation | 重载所有数据操作。 |

