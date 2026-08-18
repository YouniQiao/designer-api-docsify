# AbilityStateData

The AbilityStateData module defines a struct for ability state information. Once a lifecycle change listener is registered using [on](arkts-ability-appmanager-onapplicationstate-f.md#onapplicationstate) , you can obtain an instance of this struct from the input parameter of the **onAbilityStateChanged** callback of ApplicationStateObserver.

**Since:** 23

<!--Device-unnamed-declare class AbilityStateData--><!--Device-unnamed-declare class AbilityStateData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## abilityName

```TypeScript
abilityName: string
```

Ability name.

**Type:** string

**Since:** 23

<!--Device-AbilityStateData-abilityName: string--><!--Device-AbilityStateData-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## abilityType

```TypeScript
abilityType: number
```

Ability type, which can be [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#uiability) or [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md#extensionability).

**Type:** number

**Since:** 23

<!--Device-AbilityStateData-abilityType: int--><!--Device-AbilityStateData-abilityType: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## appCloneIndex

```TypeScript
appCloneIndex?: number
```

Index of an [application clone](../../../quick-start/app-clone.md).

**Type:** number

**Since:** 23

<!--Device-AbilityStateData-appCloneIndex?: int--><!--Device-AbilityStateData-appCloneIndex?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## bundleName

```TypeScript
bundleName: string
```

Bundle name.

**Type:** string

**Since:** 23

<!--Device-AbilityStateData-bundleName: string--><!--Device-AbilityStateData-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## callerBundleName

```TypeScript
callerBundleName?: string
```

Bundle name of the application that triggers the creation of the ability.

**Type:** string

**Since:** 23

<!--Device-AbilityStateData-callerBundleName?: string--><!--Device-AbilityStateData-callerBundleName?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## isAtomicService

```TypeScript
isAtomicService: boolean
```

Whether the ability belongs to an atomic service. **true**: The ability belongs to an atomic service. **false**: The ability does not belong to an atomic service.

**Type:** boolean

**Since:** 23

<!--Device-AbilityStateData-isAtomicService: boolean--><!--Device-AbilityStateData-isAtomicService: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## moduleName

```TypeScript
moduleName: string
```

Module name to which the ability belongs.

**Type:** string

**Since:** 23

<!--Device-AbilityStateData-moduleName: string--><!--Device-AbilityStateData-moduleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pid

```TypeScript
pid: number
```

Process ID.

**Type:** number

**Since:** 23

<!--Device-AbilityStateData-pid: int--><!--Device-AbilityStateData-pid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## state

```TypeScript
state: number
```

Ability state. - [Stage model](../../../application-models/ability-terminology.md#stage-model): For the [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#uiability), see UIAbility States . For the [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md#extensionability), see ExtensionAbility States . For the [UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#uiextensionability), see UIExtensionAbility States . - [FA model](../../../application-models/ability-terminology.md#fa-model): For the ability, see Ability States .

**Type:** number

**Since:** 23

<!--Device-AbilityStateData-state: int--><!--Device-AbilityStateData-state: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uid

```TypeScript
uid: number
```

UID of the application.

**Type:** number

**Since:** 23

<!--Device-AbilityStateData-uid: int--><!--Device-AbilityStateData-uid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
