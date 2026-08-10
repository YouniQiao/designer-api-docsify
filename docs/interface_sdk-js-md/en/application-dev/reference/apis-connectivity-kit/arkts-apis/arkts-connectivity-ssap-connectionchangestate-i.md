# ConnectionChangeState

描述SSAP连接状态。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-ssap-interface ConnectionChangeState--><!--Device-ssap-interface ConnectionChangeState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { ssap } from 'kits/@kit.ConnectivityKit';
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

<!--Device-ConnectionChangeState-address: string--><!--Device-ConnectionChangeState-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## state

```TypeScript
state: ConnectionState
```

连接状态。

**Type:** [ConnectionState](arkts-connectivity-ssap-connectionstate-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionChangeState-state: ConnectionState--><!--Device-ConnectionChangeState-state: ConnectionState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

