# StateChangeParam

Profile state change parameters.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-baseProfile-export interface StateChangeParam--><!--Device-baseProfile-export interface StateChangeParam-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## cause

```TypeScript
cause: DisconnectCause
```

Cause of disconnect

**Type:** DisconnectCause

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StateChangeParam-cause: DisconnectCause--><!--Device-StateChangeParam-cause: DisconnectCause-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## deviceId

```TypeScript
deviceId: string
```

The address of device

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StateChangeParam-deviceId: string--><!--Device-StateChangeParam-deviceId: string-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## role

```TypeScript
role?: PanRole
```

PAN role of the device

**Type:** PanRole

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StateChangeParam-role?: PanRole--><!--Device-StateChangeParam-role?: PanRole-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## state

```TypeScript
state: ProfileConnectionState
```

Profile state value

**Type:** ProfileConnectionState

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StateChangeParam-state: ProfileConnectionState--><!--Device-StateChangeParam-state: ProfileConnectionState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

