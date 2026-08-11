# LockInfo (System API)

Represents the cloud database lock information.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudExtension-export interface LockInfo--><!--Device-cloudExtension-export interface LockInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## interval

```TypeScript
interval: int
```

Lock period of the cloud database, in seconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-LockInfo-interval: int--><!--Device-LockInfo-interval: int-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## lockId

```TypeScript
lockId: int
```

Lock ID.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-LockInfo-lockId: int--><!--Device-LockInfo-lockId: int-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

