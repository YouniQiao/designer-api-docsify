# UidInfo (System API)

Parameters for obtaining detailed information on application traffic usage.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-statistics-export interface UidInfo--><!--Device-statistics-export interface UidInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## ifaceInfo

```TypeScript
ifaceInfo: IfaceInfo
```

See {@link IfaceInfo}

**Type:** [IfaceInfo](arkts-network-statistics-ifaceinfo-i-sys.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-UidInfo-ifaceInfo: IfaceInfo--><!--Device-UidInfo-ifaceInfo: IfaceInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## uid

```TypeScript
uid: int
```

Uid of app for querying traffic.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-UidInfo-uid: int--><!--Device-UidInfo-uid: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

