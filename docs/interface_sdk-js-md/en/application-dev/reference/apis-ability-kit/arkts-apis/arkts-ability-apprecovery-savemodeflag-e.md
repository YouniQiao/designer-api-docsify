# SaveModeFlag

状态保存标志，[enableAppRecovery](arkts-ability-apprecovery-enableapprecovery-f.md#enableapprecovery)接口状态保存方式的参数，该类型为枚举。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-appRecovery-enum SaveModeFlag--><!--Device-appRecovery-enum SaveModeFlag-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## SAVE_WITH_FILE

```TypeScript
SAVE_WITH_FILE = 0x0001
```

每次状态保存都会写入到本地文件缓存。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveModeFlag-SAVE_WITH_FILE = 0x0001--><!--Device-SaveModeFlag-SAVE_WITH_FILE = 0x0001-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## SAVE_WITH_SHARED_MEMORY

```TypeScript
SAVE_WITH_SHARED_MEMORY = 0x0002
```

状态先保存在内存中，应用故障退出时写入到本地文件缓存。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveModeFlag-SAVE_WITH_SHARED_MEMORY = 0x0002--><!--Device-SaveModeFlag-SAVE_WITH_SHARED_MEMORY = 0x0002-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

