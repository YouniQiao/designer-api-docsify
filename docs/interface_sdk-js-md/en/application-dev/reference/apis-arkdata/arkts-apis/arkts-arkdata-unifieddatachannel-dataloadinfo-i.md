# DataLoadInfo

用于描述被加载数据的类型与数量。

- 在**数据发送方**中使用，表示实际可提供的数据范围，必须设置该字段。  
- 在**数据接收方**中使用，表示期望加载的数据类型与数量，可根据需要设置该字段。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-interface DataLoadInfo--><!--Device-unifiedDataChannel-interface DataLoadInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## recordCount

```TypeScript
recordCount?: long
```

表示期望或可提供的最大数据记录数，默认值为0，取值范围为[0, 2&lt;sup&gt;32&lt;/sup&gt;-1]。超过取值范围时会按默认值处理。设置为浮点数时，仅使用整数部分。当用于拖拽时，会作为角标数量显示，最大支持2&lt;sup&gt;31&lt;/sup&gt;-1，超过此数值时不显示角标。作为角标数量时，优先级低于[DragPreviewOptions](../../apis-arkui/arkts-apis/arkts-arkui-common-dragpreviewoptions-i.md/arkts-arkui-common-dragpreviewoptions-i.md)中的numberBadge方法。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataLoadInfo-recordCount?: long--><!--Device-DataLoadInfo-recordCount?: long-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## types

```TypeScript
types?: Set<string>
```

表示数据类型集合，默认为空集合。

**Type:** Set&lt;string&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DataLoadInfo-types?: Set<string>--><!--Device-DataLoadInfo-types?: Set<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

