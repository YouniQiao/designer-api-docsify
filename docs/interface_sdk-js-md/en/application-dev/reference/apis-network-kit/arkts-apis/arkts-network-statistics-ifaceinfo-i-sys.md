# IfaceInfo (System API)

Defines the parameters for querying historical traffic of an NIC.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

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

End time of the query, which is a timestamp in seconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## iface

```TypeScript
iface: string
```

NIC name.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## startTime

```TypeScript
startTime: int
```

Start time of the query, which is a timestamp in seconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.
