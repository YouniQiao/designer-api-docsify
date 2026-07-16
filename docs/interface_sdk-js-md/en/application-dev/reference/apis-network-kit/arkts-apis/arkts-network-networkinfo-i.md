# NetworkInfo

Parameters for obtaining detailed information on specified network traffic usage.

**Since:** 22

<!--Device-statistics-export interface NetworkInfo--><!--Device-statistics-export interface NetworkInfo-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## endTime

```TypeScript
endTime: number
```

End time for querying traffic.

**Type:** number

**Since:** 22

<!--Device-NetworkInfo-endTime: int--><!--Device-NetworkInfo-endTime: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## simId

```TypeScript
simId?: number
```

SIM card id for querying traffic.

**Type:** number

**Since:** 22

<!--Device-NetworkInfo-simId?: int--><!--Device-NetworkInfo-simId?: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## startTime

```TypeScript
startTime: number
```

Start time for querying traffic.

**Type:** number

**Since:** 22

<!--Device-NetworkInfo-startTime: int--><!--Device-NetworkInfo-startTime: int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## type

```TypeScript
type: NetBearType
```

Network type for querying traffic.

**Type:** NetBearType

**Since:** 22

<!--Device-NetworkInfo-type: NetBearType--><!--Device-NetworkInfo-type: NetBearType-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

