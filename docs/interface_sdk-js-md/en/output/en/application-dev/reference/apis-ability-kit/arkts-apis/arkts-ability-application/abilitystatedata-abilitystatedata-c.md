# AbilityStateData

The AbilityStateData module defines a struct for ability state information. Once a lifecycle change listener is registered using [on]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ , you can obtain an instance of this struct from the input parameter of the **onAbilityStateChanged** callback of [ApplicationStateObserver]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class AbilityStateData--><!--Device-unnamed-declare class AbilityStateData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## abilityName

```TypeScript
abilityName: string
```

Ability name.

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-abilityName: string--><!--Device-AbilityStateData-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## abilityType

```TypeScript
abilityType: int
```

\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_, which can be [UIAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ or [ExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_.

**Type:** int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-abilityType: int--><!--Device-AbilityStateData-abilityType: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## appCloneIndex

```TypeScript
appCloneIndex?: int
```

Index of an \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-appCloneIndex?: int--><!--Device-AbilityStateData-appCloneIndex?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## bundleName

```TypeScript
bundleName: string
```

Bundle name.

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-bundleName: string--><!--Device-AbilityStateData-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## callerBundleName

```TypeScript
callerBundleName?: string
```

Bundle name of the application that triggers the creation of the ability.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-AbilityStateData-callerBundleName?: string--><!--Device-AbilityStateData-callerBundleName?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## isAtomicService

```TypeScript
isAtomicService: boolean
```

Whether the ability belongs to an atomic service. **true**: The ability belongs to an atomic service. **false**: The ability does not belong to an atomic service.

**Type:** boolean

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-isAtomicService: boolean--><!--Device-AbilityStateData-isAtomicService: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## moduleName

```TypeScript
moduleName: string
```

Module name to which the ability belongs.

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-moduleName: string--><!--Device-AbilityStateData-moduleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pid

```TypeScript
pid: int
```

Process ID.

**Type:** int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-pid: int--><!--Device-AbilityStateData-pid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## state

```TypeScript
state: int
```

Ability state. - \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_: For the [UIAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_, see \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ . For the [ExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_7\_\_\_, see \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ . For the [UIExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_8\_\_\_, see \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_ . - \_\_\_MD\_LINK\_DESC\_USD\_4\_\_\_: For the ability, see \_\_\_MD\_LINK\_DESC\_USD\_5\_\_\_ .

**Type:** int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-state: int--><!--Device-AbilityStateData-state: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uid

```TypeScript
uid: int
```

UID of the application.

**Type:** int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-uid: int--><!--Device-AbilityStateData-uid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

