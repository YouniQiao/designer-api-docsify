# SaveModeFlag

Enumerates the application state saving modes. This enum is used as an input parameter of [enableAppRecovery]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-appRecovery-enum SaveModeFlag--><!--Device-appRecovery-enum SaveModeFlag-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## SAVE_WITH_FILE

```TypeScript
SAVE_WITH_FILE = 0x0001
```

The application state is saved and written to the local file cache.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveModeFlag-SAVE_WITH_FILE = 0x0001--><!--Device-SaveModeFlag-SAVE_WITH_FILE = 0x0001-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## SAVE_WITH_SHARED_MEMORY

```TypeScript
SAVE_WITH_SHARED_MEMORY = 0x0002
```

The application state is saved in the memory. When the application exits due to a fault, it is written to the local file cache.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SaveModeFlag-SAVE_WITH_SHARED_MEMORY = 0x0002--><!--Device-SaveModeFlag-SAVE_WITH_SHARED_MEMORY = 0x0002-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

