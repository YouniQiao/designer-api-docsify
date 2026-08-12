# Summary

Summarizes the data information of the **unifiedData** object, including the data type and size.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class Summary--><!--Device-unifiedDataChannel-class Summary-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

## overview

```TypeScript
get overview(): Record<string, long>
```

Indicates the overview information of unifiedData.

**Type:** ArkTS-Dyn: Record&lt;string, number&gt;  <br>ArkTS-Sta：Record&lt;string, long&gt;

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Summary-get overview(): Record<string, long>--><!--Device-Summary-get overview(): Record<string, long>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## summary

```TypeScript
set summary(value: Record<string, long>)
```

A map for each type and data size, key is data type, value is the corresponding data size

**Type:** ArkTS-Dyn: Record&lt;string, number&gt;  <br>ArkTS-Sta：Record&lt;string, long&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Summary-set summary(value: Record<string, long>)--><!--Device-Summary-set summary(value: Record<string, long>)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## totalSize

```TypeScript
set totalSize(value: long)
```

Total data size of data in Bytes

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Summary-set totalSize(value: long)--><!--Device-Summary-set totalSize(value: long)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

