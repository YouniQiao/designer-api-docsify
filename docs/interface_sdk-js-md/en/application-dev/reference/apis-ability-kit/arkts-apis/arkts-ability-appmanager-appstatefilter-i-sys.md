# AppStateFilter (System API)

Describes the filter for application lifecycle change events. It can be used as a parameter of  
[on]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to filter application lifecycle change events you want to listen for.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-appManager-export interface AppStateFilter--><!--Device-appManager-export interface AppStateFilter-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## abilityStateTypes

```TypeScript
abilityStateTypes?: int
```

Type of ability state to filter. The options are as follows:

- **0**: Do not listen for any ability state.  
- A bitwise OR combination of the enumerated values of \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_, for  
example, "appManager.FilterAbilityStateType.CREATE | appManager.FilterAbilityStateType.FOREGROUND" listens for both the creating and foreground states of ability components.  
- If this parameter is not set, all ability state types are listened for by default.

**Type:** int

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-AppStateFilter-abilityStateTypes?: int--><!--Device-AppStateFilter-abilityStateTypes?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## appStateTypes

```TypeScript
appStateTypes?: int
```

Type of application state to filter. The options are as follows:

- **0**: Do not listen for any application state.  
- A bitwise OR combination of the enumerated values of \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_, for example,  
"appManager.FilterAppStateType.CREATE | appManager.FilterAppStateType.FOREGROUND" listens for both the creating and foreground states of applications.  
- If this parameter is not set, all application state types are listened for by default.

**Type:** int

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-AppStateFilter-appStateTypes?: int--><!--Device-AppStateFilter-appStateTypes?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleTypes

```TypeScript
bundleTypes?: int
```

Type of application to filter. The options are as follows:

- **0**: Do not listen for any application type.  
- A bitwise OR combination of the enumerated values of \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_, for example, "  
appManager.FilterBundleType.APP | appManager.FilterBundleType.ATOMIC\_SERVICE" listens for lifecycle change events for both applications and atomic services.  
- If this parameter is not set, all application types are listened for by default.

**Type:** int

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-AppStateFilter-bundleTypes?: int--><!--Device-AppStateFilter-bundleTypes?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## callbacks

```TypeScript
callbacks?: int
```

Callback to filter. The options are as follows:

- **0**: Do not listen for any callback.  
- A bitwise OR combination of the enumerated values of \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_, for example, "  
appManager.FilterCallback.ON\_ABILITY\_STATE\_CHANGED | appManager.FilterCallback.ON\_PROCESS\_STATE\_CHANGED" listens for both  
\_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_and  
\_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_.  
- If this parameter is not set, all callbacks enumerated in \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_ are listened for  
by default.

**Type:** int

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-AppStateFilter-callbacks?: int--><!--Device-AppStateFilter-callbacks?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## processStateTypes

```TypeScript
processStateTypes?: int
```

Type of process state to filter. The options are as follows:

- **0**: Do not listen for any process state.  
- A bitwise OR combination of the enumerated values of \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_, for  
example, "appManager.FilterProcessStateType.CREATE | appManager.FilterProcessStateType.FOREGROUND" listens for both the creating and foreground states of processes.  
- If this parameter is not set, all process state types are listened for by default.

**Type:** int

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-AppStateFilter-processStateTypes?: int--><!--Device-AppStateFilter-processStateTypes?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

