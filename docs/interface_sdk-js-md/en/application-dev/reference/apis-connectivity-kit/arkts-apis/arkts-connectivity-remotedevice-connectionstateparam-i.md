# ConnectionStateParam

连接状态参数。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-remoteDevice-interface ConnectionStateParam--><!--Device-remoteDevice-interface ConnectionStateParam-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { remoteDevice } from 'kits/@kit.ConnectivityKit';
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

<!--Device-ConnectionStateParam-address: string--><!--Device-ConnectionStateParam-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## connectionReason

```TypeScript
connectionReason: ConnectionReason
```

连接原因。

**Type:** [ConnectionReason](arkts-connectivity-remotedevice-connectionreason-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionStateParam-connectionReason: ConnectionReason--><!--Device-ConnectionStateParam-connectionReason: ConnectionReason-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## preState

```TypeScript
preState: ConnectionState
```

上一个连接状态。

**Type:** [ConnectionState](arkts-connectivity-ssap-connectionstate-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionStateParam-preState: ConnectionState--><!--Device-ConnectionStateParam-preState: ConnectionState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## reasonMsg

```TypeScript
reasonMsg?: string
```

原因消息。此字段仅用于日志信息，不应该用于逻辑处理。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionStateParam-reasonMsg?: string--><!--Device-ConnectionStateParam-reasonMsg?: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## state

```TypeScript
state: ConnectionState
```

当前连接状态。

**Type:** [ConnectionState](arkts-connectivity-ssap-connectionstate-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionStateParam-state: ConnectionState--><!--Device-ConnectionStateParam-state: ConnectionState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

