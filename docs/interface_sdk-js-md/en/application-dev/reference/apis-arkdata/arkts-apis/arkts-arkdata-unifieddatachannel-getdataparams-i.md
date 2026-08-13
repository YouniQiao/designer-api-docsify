# GetDataParams

Represents the parameters for obtaining data from UDMF, including the destination directory, option for resolving file conflicts, and progress indicator type. For details, see [Obtaining Data Asynchronously Through Drag-and-Drop].

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unifiedDataChannel-interface GetDataParams--><!--Device-unifiedDataChannel-interface GetDataParams-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

## acceptableInfo

```TypeScript
acceptableInfo?: DataLoadInfo
```

Indicates the supported data information.

**Type:** [DataLoadInfo](arkts-arkdata-unifieddatachannel-dataloadinfo-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GetDataParams-acceptableInfo?: DataLoadInfo--><!--Device-GetDataParams-acceptableInfo?: DataLoadInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## dataProgressListener

```TypeScript
dataProgressListener: DataProgressListener
```

Indicates progress and data listener when getting unified data.

**Type:** [DataProgressListener](arkts-arkdata-unifieddatachannel-dataprogresslistener-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GetDataParams-dataProgressListener: DataProgressListener--><!--Device-GetDataParams-dataProgressListener: DataProgressListener-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## destUri

```TypeScript
destUri?: string
```

Indicates the dest path uri where copy file will be copied to sandbox of application.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GetDataParams-destUri?: string--><!--Device-GetDataParams-destUri?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## fileConflictOptions

```TypeScript
fileConflictOptions?: FileConflictOptions
```

Indicates file conflict options when dest path has file with same name.

**Type:** FileConflictOptions

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GetDataParams-fileConflictOptions?: FileConflictOptions--><!--Device-GetDataParams-fileConflictOptions?: FileConflictOptions-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## progressIndicator

```TypeScript
progressIndicator: ProgressIndicator
```

Indicates whether to use default system progress indicator.

**Type:** ProgressIndicator

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GetDataParams-progressIndicator: ProgressIndicator--><!--Device-GetDataParams-progressIndicator: ProgressIndicator-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

