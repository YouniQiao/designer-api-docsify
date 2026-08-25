# NetworkInfo

Defines the network information.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## endTime

```TypeScript
endTime: int
```

End timestamp, in seconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

## simId

```TypeScript
simId?: int
```

SIM card ID. The default value is the maximum value of the uint32_t type.  
**Note：**: If **type** is set to **cellular**, this field must be specified.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

## startTime

```TypeScript
startTime: int
```

Start timestamp, in seconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core

## type

```TypeScript
type: NetBearType
```

Network type.  
**Note：**: If **type** is set to **cellular**, the **simId** field must be specified.

**Type:** NetBearType

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetManager.Core
