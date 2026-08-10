# LaunchParam

启动参数，主要包括Ability启动原因以及上次退出原因。Ability启动时由系统自动传入，开发者无需修改。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AbilityConstant-export interface LaunchParam--><!--Device-AbilityConstant-export interface LaunchParam-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { AbilityConstant } from 'kits/@kit.AbilityKit';
```

## lastExitDetailInfo

```TypeScript
lastExitDetailInfo?: LastExitDetailInfo
```

表示Ability上次退出时的关键运行信息（含进程ID、退出时间戳、RSS内存值等）。

**Type:** [LastExitDetailInfo](arkts-ability-abilityconstant-lastexitdetailinfo-i.md)

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

表示Ability上次退出的详细原因。

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

枚举类型，表示Ability上次退出原因。

**Type:** [LastExitReason](arkts-ability-abilityconstant-lastexitreason-e.md)

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

枚举类型，表示Ability启动原因（如故障恢复拉起、意图调用拉起、原子化服务分享拉起等），详见[LaunchReason](arkts-ability-abilityconstant-launchreason-e.md)。

**Type:** [LaunchReason](arkts-ability-abilityconstant-launchreason-e.md)

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

表示Ability启动的详细原因。

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

表示UIAbility开始启动的UTC时间戳，单位为毫秒。

**约束：**

该功能仅在启动UIAbility时生效。对于其他类型的Ability（例如UIExtensionAbility），所获取的启动时间为默认值0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

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

表示UIAbility开始启动时系统已运行的时间（自系统开机启动以来的时间），单位为毫秒。

**约束：**

该功能仅在启动UIAbility时生效。对于其他类型的Ability（例如UIExtensionAbility），所获取的启动时间为默认值0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-LaunchParam-launchUptime?: long--><!--Device-LaunchParam-launchUptime?: long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

