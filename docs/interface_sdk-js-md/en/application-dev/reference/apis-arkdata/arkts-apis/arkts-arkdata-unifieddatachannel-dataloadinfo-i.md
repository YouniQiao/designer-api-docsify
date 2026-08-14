# DataLoadInfo

Defines type and quantity of the data to load. - Used by the **data sender** to define the data range that can be provided. This field is mandatory. - Used by the **data receiver** to define the expected data type and quantity. This field is optional.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unifiedDataChannel-interface DataLoadInfo--><!--Device-unifiedDataChannel-interface DataLoadInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'unifiedDataChannel';
```

## recordCount

```TypeScript
recordCount?: long
```

Indicates the maximum number of data records to be loaded.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-DataLoadInfo-recordCount?: long--><!--Device-DataLoadInfo-recordCount?: long-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## types

```TypeScript
types?: Set<string>
```

Represents the data type or supported types to load. <br>This parameter is mandatory when used by the data provider.

**Type:** Set&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-DataLoadInfo-types?: Set<string>--><!--Device-DataLoadInfo-types?: Set<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

