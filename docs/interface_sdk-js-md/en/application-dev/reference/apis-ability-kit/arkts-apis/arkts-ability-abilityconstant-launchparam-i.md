# LaunchParam

Describes the launch parameters, which mainly include the ability launch reasons and reasons for the last exit. The parameter values are automatically passed in by the system when the ability is launched. You do not need to change the values.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AbilityConstant-export interface LaunchParam--><!--Device-AbilityConstant-export interface LaunchParam-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## lastExitDetailInfo

```TypeScript
lastExitDetailInfo?: LastExitDetailInfo
```

Key runtime information for the last exit of the ability (including process ID, exit timestamp, and RSS memory value).

**Type:** LastExitDetailInfo

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LaunchParam-lastExitDetailInfo?: LastExitDetailInfo--><!--Device-LaunchParam-lastExitDetailInfo?: LastExitDetailInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## lastExitMessage

```TypeScript
lastExitMessage: string
```

Detailed message that describes the reason for the last exit of the ability.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LaunchParam-lastExitMessage: string--><!--Device-LaunchParam-lastExitMessage: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## lastExitReason

```TypeScript
lastExitReason: LastExitReason
```

An enumerated value indicating the reason for the last exit of the ability.

**Type:** LastExitReason

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LaunchParam-lastExitReason: LastExitReason--><!--Device-LaunchParam-lastExitReason: LastExitReason-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## launchReason

```TypeScript
launchReason: LaunchReason
```

An enumerated value indicating the reason for ability launch (for example, recovery from a fault, intent invocation, or atomic service sharing). For details, see [LaunchReason]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** LaunchReason

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LaunchParam-launchReason: LaunchReason--><!--Device-LaunchParam-launchReason: LaunchReason-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## launchReasonMessage

```TypeScript
launchReasonMessage?: string
```

Detailed message that describes the reason for the ability launch.

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LaunchParam-launchReasonMessage?: string--><!--Device-LaunchParam-launchReasonMessage?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## launchUTCTime

```TypeScript
launchUTCTime?: long
```

UTC timestamp when the UIAbility starts, in milliseconds.

This API can be used in atomic services since API version 23.

**Constraints**:

This feature takes effect only when the UIAbility is started. For other types of abilities (for example,UIExtensionAbility), the obtained start time is the default value **0**.

**Type:** long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LaunchParam-launchUTCTime?: long--><!--Device-LaunchParam-launchUTCTime?: long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## launchUptime

```TypeScript
launchUptime?: long
```

System uptime (the time elapsed since the system booted up) when the UIAbility starts, in milliseconds.

**Constraints**:

This feature takes effect only when the UIAbility is started. For other types of abilities (for example,UIExtensionAbility), the obtained start time is the default value **0**.

**Type:** long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LaunchParam-launchUptime?: long--><!--Device-LaunchParam-launchUptime?: long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

