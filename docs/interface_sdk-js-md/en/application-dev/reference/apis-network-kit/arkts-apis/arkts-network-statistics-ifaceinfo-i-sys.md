# IfaceInfo (System API)

Parameters for obtaining detailed information on network interface traffic usage.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-statistics-export interface IfaceInfo--><!--Device-statistics-export interface IfaceInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## endTime

```TypeScript
endTime: int
```

End time for querying traffic.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-IfaceInfo-endTime: int--><!--Device-IfaceInfo-endTime: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## iface

```TypeScript
iface: string
```

Network interface for querying traffic.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-IfaceInfo-iface: string--><!--Device-IfaceInfo-iface: string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## startTime

```TypeScript
startTime: int
```

Start time for querying traffic.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-IfaceInfo-startTime: int--><!--Device-IfaceInfo-startTime: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

