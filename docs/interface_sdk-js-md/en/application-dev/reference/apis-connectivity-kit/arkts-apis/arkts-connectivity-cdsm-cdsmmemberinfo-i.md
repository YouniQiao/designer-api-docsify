# CdsmMemberInfo

Describes the member information of coordinated devices set.

**Since:** 26.0.0

<!--Device-cdsm-interface CdsmMemberInfo--><!--Device-cdsm-interface CdsmMemberInfo-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { cdsm } from '@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

Indicates the device address.The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CdsmMemberInfo-address: string--><!--Device-CdsmMemberInfo-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## state

```TypeScript
state: CdsmConnectionState
```

Member's connection state.

**Type:** CdsmConnectionState

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-CdsmMemberInfo-state: CdsmConnectionState--><!--Device-CdsmMemberInfo-state: CdsmConnectionState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

