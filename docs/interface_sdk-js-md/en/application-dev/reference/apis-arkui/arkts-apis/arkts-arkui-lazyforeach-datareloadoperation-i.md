# DataReloadOperation

重载所有数据操作。当onDatasetChange含有DataOperationType.RELOAD操作时，其余操作全部失效，框架会自己调用keyGenerator进行键值比对。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface DataReloadOperation--><!--Device-unnamed-export interface DataReloadOperation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: DataOperationType
```

数据全部重载类型。

**Type:** [DataOperationType](arkts-arkui-lazyforeach-dataoperationtype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataReloadOperation-type: DataOperationType--><!--Device-DataReloadOperation-type: DataOperationType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

