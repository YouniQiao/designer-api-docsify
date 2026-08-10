# CdsmMemberInfo

描述合作设备集的成员信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-cdsm-interface CdsmMemberInfo--><!--Device-cdsm-interface CdsmMemberInfo-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { cdsm } from 'kits/@kit.ConnectivityKit';
```

## address

```TypeScript
address: string
```

设备地址。长度必须为17，由16进制数字和冒号组成，形如 "11:22:33:AA:BB:FF"。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CdsmMemberInfo-address: string--><!--Device-CdsmMemberInfo-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## state

```TypeScript
state: CdsmConnectionState
```

成员的连接状态。

**Type:** [CdsmConnectionState](arkts-connectivity-cdsm-cdsmconnectionstate-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CdsmMemberInfo-state: CdsmConnectionState--><!--Device-CdsmMemberInfo-state: CdsmConnectionState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

