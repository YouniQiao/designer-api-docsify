# FilterAbilityStateType (System API)

Enumerates the types of ability states to filter. It can be used with [AppStateFilter]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to filter the ability state types you want to listen for.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-appManager-export enum FilterAbilityStateType--><!--Device-appManager-export enum FilterAbilityStateType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## CREATE

```TypeScript
CREATE = 1 << 0
```

The ability is being created. It corresponds to the state **ABILITY\_STATE\_CREATE** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ .

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterAbilityStateType-CREATE = 1 << 0--><!--Device-FilterAbilityStateType-CREATE = 1 << 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## FOREGROUND

```TypeScript
FOREGROUND = 1 << 1
```

The ability is running in the foreground. It corresponds to the state **ABILITY\_STATE\_FOREGROUND** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ .

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterAbilityStateType-FOREGROUND = 1 << 1--><!--Device-FilterAbilityStateType-FOREGROUND = 1 << 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## BACKGROUND

```TypeScript
BACKGROUND = 1 << 2
```

The ability is running in the background. It corresponds to the state **ABILITY\_STATE\_BACKGROUND** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ .

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterAbilityStateType-BACKGROUND = 1 << 2--><!--Device-FilterAbilityStateType-BACKGROUND = 1 << 2-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## DESTROY

```TypeScript
DESTROY = 1 << 3
```

The ability has been destroyed. It corresponds to the state **ABILITY\_STATE\_TERMINATED** in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ .

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-FilterAbilityStateType-DESTROY = 1 << 3--><!--Device-FilterAbilityStateType-DESTROY = 1 << 3-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

