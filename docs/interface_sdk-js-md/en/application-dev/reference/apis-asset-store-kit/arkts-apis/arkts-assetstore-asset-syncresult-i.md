# SyncResult

关键资产同步的结果。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-asset-interface SyncResult--><!--Device-asset-interface SyncResult-End-->

**System capability:** SystemCapability.Security.Asset

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## failedCount

```TypeScript
readonly failedCount?: number
```

关键资产同步失败的数量。

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-SyncResult-readonly failedCount?: number--><!--Device-SyncResult-readonly failedCount?: number-End-->

**System capability:** SystemCapability.Security.Asset

## resultCode

```TypeScript
readonly resultCode: number
```

关键资产同步的结果码。同步成功时结果码为0，同步失败时结果码参考[ErrorCode](arkts-assetstore-asset-errorcode-e.md)。

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-SyncResult-readonly resultCode: number--><!--Device-SyncResult-readonly resultCode: number-End-->

**System capability:** SystemCapability.Security.Asset

## totalCount

```TypeScript
readonly totalCount?: number
```

触发同步的关键资产总数。

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-SyncResult-readonly totalCount?: number--><!--Device-SyncResult-readonly totalCount?: number-End-->

**System capability:** SystemCapability.Security.Asset

