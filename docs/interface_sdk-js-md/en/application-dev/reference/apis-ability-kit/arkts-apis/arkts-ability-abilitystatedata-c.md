# AbilityStateData

AbilityStateData是Ability状态信息的数据结构。使用  
[on](./../@ohos.app.ability.appManager:appManager.on(type: 'applicationState', observer: ApplicationStateObserver))注册生命周期变化监听后，可以通过[ApplicationStateObserver](arkts-ability-applicationstateobserver-c.md)的onAbilityStateChanged回调的入参获取该数据结构。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class AbilityStateData--><!--Device-unnamed-declare class AbilityStateData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## abilityName

```TypeScript
abilityName: string
```

Ability名称。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-abilityName: string--><!--Device-AbilityStateData-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## abilityType

```TypeScript
abilityType: int
```

[Ability类型](../../../reference/apis-ability-kit/js-apis-inner-application-abilityStateData.md#ability类型)：  
[UIAbility](arkts-app-ability-uiability.md)或  
[ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md)等。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-abilityType: int--><!--Device-AbilityStateData-abilityType: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## appCloneIndex

```TypeScript
appCloneIndex?: int
```

应用包的[分身](../../../quick-start/app-clone.md)索引标识。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-appCloneIndex?: int--><!--Device-AbilityStateData-appCloneIndex?: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## bundleName

```TypeScript
bundleName: string
```

应用Bundle名称。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-bundleName: string--><!--Device-AbilityStateData-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## callerBundleName

```TypeScript
callerBundleName?: string
```

Ability创建时的拉起方Bundle名称。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-AbilityStateData-callerBundleName?: string--><!--Device-AbilityStateData-callerBundleName?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## isAtomicService

```TypeScript
isAtomicService: boolean
```

判断Ability所属应用是否为原子化服务。

true: 是原子化服务。

false: 不是原子化服务。

**Type:** boolean

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-isAtomicService: boolean--><!--Device-AbilityStateData-isAtomicService: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## moduleName

```TypeScript
moduleName: string
```

Ability所属的模块名称。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-moduleName: string--><!--Device-AbilityStateData-moduleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pid

```TypeScript
pid: int
```

进程ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-pid: int--><!--Device-AbilityStateData-pid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## state

```TypeScript
state: int
```

Ability状态。

- [Stage模型](../../../application-models/ability-terminology.md#stage模型)：  
[UIAbility](arkts-app-ability-uiability.md)的状态参见  
[UIAbility状态](../../../reference/apis-ability-kit/js-apis-inner-application-abilityStateData.md#uiability状态)；  
[ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md)的状态参见  
[ExtensionAbility状态](../../../reference/apis-ability-kit/js-apis-inner-application-abilityStateData.md#extensionability状态)；[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)的状态参见  
[UIExtensionAbility状态](../../../reference/apis-ability-kit/js-apis-inner-application-abilityStateData.md#uiextensionability状态)。  
- [FA模型](../../../application-models/ability-terminology.md#fa模型)：参见  
[Ability状态](../../../reference/apis-ability-kit/js-apis-inner-application-abilityStateData.md#ability状态)。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-state: int--><!--Device-AbilityStateData-state: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uid

```TypeScript
uid: int
```

所属应用程序的UID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-AbilityStateData-uid: int--><!--Device-AbilityStateData-uid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

