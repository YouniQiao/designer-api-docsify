# ConnectionStateParam

Describes the connection state parameters.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-remoteDevice-interface ConnectionStateParam--><!--Device-remoteDevice-interface ConnectionStateParam-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { remoteDevice } from 'remoteDevice';
```

## address

```TypeScript
address: string
```

Indicates the device address. The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionStateParam-address: string--><!--Device-ConnectionStateParam-address: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## connectionReason

```TypeScript
connectionReason: ConnectionReason
```

Connection reason.

**Type:** [ConnectionReason](arkts-connectivity-remotedevice-connectionreason-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionStateParam-connectionReason: ConnectionReason--><!--Device-ConnectionStateParam-connectionReason: ConnectionReason-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## preState

```TypeScript
preState: ConnectionState
```

Indicates the previous connection state.

**Type:** ConnectionState

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionStateParam-preState: ConnectionState--><!--Device-ConnectionStateParam-preState: ConnectionState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## reasonMsg

```TypeScript
reasonMsg?: string
```

Indicates reason message. This field is intended for log information only and should not be used for logic processing.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionStateParam-reasonMsg?: string--><!--Device-ConnectionStateParam-reasonMsg?: string-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## state

```TypeScript
state: ConnectionState
```

Indicates the current connection state.

**Type:** ConnectionState

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ConnectionStateParam-state: ConnectionState--><!--Device-ConnectionStateParam-state: ConnectionState-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

