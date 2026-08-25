# NetworkMatchRule (System API)

Defines the network for which the quota policy is set.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## identity

```TypeScript
identity: string
```

ID of the SIM card on the metered cellular network.It is used for Ethernet and Wi-Fi networks.It is used together with **iccid**.

**Type:** string

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## netType

```TypeScript
netType: NetBearType
```

Network type.

**Type:** NetBearType

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

## simId

```TypeScript
simId: string
```

Identifier of the SIM card on the metered cellular network.It is not used for Ethernet and Wi-Fi networks.

**Type:** string

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.
