# NetworkInfo (System API)

Defines the network information.

**Since:** 23

<!--Device-statistics-export interface NetworkInfo--><!--Device-statistics-export interface NetworkInfo-End-->

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

End timestamp, in seconds.

**Type:** int

**Since:** 23

<!--Device-NetworkInfo-endTime: int--><!--Device-NetworkInfo-endTime: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## simId

```TypeScript
simId?: int
```

SIM card ID. The default value is the maximum value of the uint32_t type.

**Note：**: If **type** is set to **cellular**, this field must be specified.

**Type:** int

**Since:** 23

<!--Device-NetworkInfo-simId?: int--><!--Device-NetworkInfo-simId?: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## startTime

```TypeScript
startTime: int
```

Start timestamp, in seconds.

**Type:** int

**Since:** 23

<!--Device-NetworkInfo-startTime: int--><!--Device-NetworkInfo-startTime: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## type

```TypeScript
type: NetBearType
```

Network type.

**Note：**: If **type** is set to **cellular**, the **simId** field must be specified.

**Type:** NetBearType

**Since:** 23

<!--Device-NetworkInfo-type: NetBearType--><!--Device-NetworkInfo-type: NetBearType-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

