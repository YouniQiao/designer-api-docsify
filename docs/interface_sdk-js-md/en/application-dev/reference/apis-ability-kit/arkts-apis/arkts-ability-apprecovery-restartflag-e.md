# RestartFlag

应用重启标志，[enableAppRecovery](arkts-ability-apprecovery-enableapprecovery-f.md#enableapprecovery)接口重启选项参数，该类型为枚举。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-appRecovery-enum RestartFlag--><!--Device-appRecovery-enum RestartFlag-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## ALWAYS_RESTART

```TypeScript
ALWAYS_RESTART = 0
```

总是重启应用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RestartFlag-ALWAYS_RESTART = 0--><!--Device-RestartFlag-ALWAYS_RESTART = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## RESTART_WHEN_JS_CRASH

```TypeScript
RESTART_WHEN_JS_CRASH = 0x0001
```

发生JS_CRASH时重启应用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RestartFlag-RESTART_WHEN_JS_CRASH = 0x0001--><!--Device-RestartFlag-RESTART_WHEN_JS_CRASH = 0x0001-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## RESTART_WHEN_APP_FREEZE

```TypeScript
RESTART_WHEN_APP_FREEZE = 0x0002
```

发生APP_FREEZE时重启应用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RestartFlag-RESTART_WHEN_APP_FREEZE = 0x0002--><!--Device-RestartFlag-RESTART_WHEN_APP_FREEZE = 0x0002-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## NO_RESTART

```TypeScript
NO_RESTART = 0xFFFF
```

总是不重启应用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RestartFlag-NO_RESTART = 0xFFFF--><!--Device-RestartFlag-NO_RESTART = 0xFFFF-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## RESTART_WHEN_CPP_CRASH

```TypeScript
RESTART_WHEN_CPP_CRASH = 0x0004
```

发生CPP_CRASH时重启应用。

**模型约束**：此接口仅可在Stage模型下使用。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RestartFlag-RESTART_WHEN_CPP_CRASH = 0x0004--><!--Device-RestartFlag-RESTART_WHEN_CPP_CRASH = 0x0004-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

