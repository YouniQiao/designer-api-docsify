# BatchResult

[batchAdd](arkts-assetstore-asset-batchadd-f.md#batchadd)、[batchUpdate](arkts-assetstore-asset-batchupdate-f.md#batchupdate)和[batchRemove](arkts-assetstore-asset-batchremove-f.md#batchremove)批量操作的结果。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-asset-interface BatchResult--><!--Device-asset-interface BatchResult-End-->

**System capability:** SystemCapability.Security.Asset

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## failedCount

```TypeScript
failedCount: number
```

批量操作的失败数量，0表示全部成功。

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-BatchResult-failedCount: number--><!--Device-BatchResult-failedCount: number-End-->

**System capability:** SystemCapability.Security.Asset

## failedErrorInfos

```TypeScript
failedErrorInfos: Array<BatchErrInfo>
```

批量操作中失败的关键资产的错误信息数组，全部成功时为空数组。

**Type:** Array&lt;BatchErrInfo&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-BatchResult-failedErrorInfos: Array<BatchErrInfo>--><!--Device-BatchResult-failedErrorInfos: Array<BatchErrInfo>-End-->

**System capability:** SystemCapability.Security.Asset

