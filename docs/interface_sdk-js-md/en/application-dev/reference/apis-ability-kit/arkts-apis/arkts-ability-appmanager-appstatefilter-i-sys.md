# AppStateFilter (System API)

Describes the filter for application lifecycle change events. It can be used as a parameter of [on](arkts-ability-appmanager-onapplicationstate-f.md#onapplicationstate) to filter application lifecycle change events you want to listen for.

**Since:** 23

<!--Device-appManager-export interface AppStateFilter--><!--Device-appManager-export interface AppStateFilter-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { appManager } from '@kit.AbilityKit';
```

## abilityStateTypes

```TypeScript
abilityStateTypes?: int
```

Type of ability state to filter. The options are as follows: - **0**: Do not listen for any ability state. - A bitwise OR combination of the enumerated values of [FilterAbilityStateType](arkts-ability-appmanager-filterabilitystatetype-e-sys.md#filterabilitystatetype-system-api), for example, "appManager.FilterAbilityStateType.CREATE | appManager.FilterAbilityStateType.FOREGROUND" listens for both the creating and foreground states of ability components. - If this parameter is not set, all ability state types are listened for by default.

**Type:** int

**Since:** 23

<!--Device-AppStateFilter-abilityStateTypes?: int--><!--Device-AppStateFilter-abilityStateTypes?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## appStateTypes

```TypeScript
appStateTypes?: int
```

Type of application state to filter. The options are as follows: - **0**: Do not listen for any application state. - A bitwise OR combination of the enumerated values of [FilterAppStateType](arkts-ability-appmanager-filterappstatetype-e-sys.md#filterappstatetype-system-api), for example, "appManager.FilterAppStateType.CREATE | appManager.FilterAppStateType.FOREGROUND" listens for both the creating and foreground states of applications. - If this parameter is not set, all application state types are listened for by default.

**Type:** int

**Since:** 23

<!--Device-AppStateFilter-appStateTypes?: int--><!--Device-AppStateFilter-appStateTypes?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleTypes

```TypeScript
bundleTypes?: int
```

Type of application to filter. The options are as follows: - **0**: Do not listen for any application type. - A bitwise OR combination of the enumerated values of [FilterBundleType](arkts-ability-appmanager-filterbundletype-e-sys.md#filterbundletype-system-api), for example, " appManager.FilterBundleType.APP | appManager.FilterBundleType.ATOMIC_SERVICE" listens for lifecycle change events for both applications and atomic services. - If this parameter is not set, all application types are listened for by default.

**Type:** int

**Since:** 23

<!--Device-AppStateFilter-bundleTypes?: int--><!--Device-AppStateFilter-bundleTypes?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## callbacks

```TypeScript
callbacks?: int
```

Callback to filter. The options are as follows: - **0**: Do not listen for any callback. - A bitwise OR combination of the enumerated values of [FilterCallback](arkts-ability-appmanager-filtercallback-e-sys.md#filtercallback-system-api), for example, " appManager.FilterCallback.ON_ABILITY_STATE_CHANGED | appManager.FilterCallback.ON_PROCESS_STATE_CHANGED" listens for both ApplicationStateObserver.onAbilityStateChanged and ApplicationStateObserver.onProcessStateChanged . - If this parameter is not set, all callbacks enumerated in [FilterCallback](arkts-ability-appmanager-filtercallback-e-sys.md#filtercallback-system-api) are listened for by default.

**Type:** int

**Since:** 23

<!--Device-AppStateFilter-callbacks?: int--><!--Device-AppStateFilter-callbacks?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## processStateTypes

```TypeScript
processStateTypes?: int
```

Type of process state to filter. The options are as follows: - **0**: Do not listen for any process state. - A bitwise OR combination of the enumerated values of [FilterProcessStateType](arkts-ability-appmanager-filterprocessstatetype-e-sys.md#filterprocessstatetype-system-api), for example, "appManager.FilterProcessStateType.CREATE | appManager.FilterProcessStateType.FOREGROUND" listens for both the creating and foreground states of processes. - If this parameter is not set, all process state types are listened for by default.

**Type:** int

**Since:** 23

<!--Device-AppStateFilter-processStateTypes?: int--><!--Device-AppStateFilter-processStateTypes?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

