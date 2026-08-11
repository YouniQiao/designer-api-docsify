# getAbilityRunningInfos (System API)

## getAbilityRunningInfos

```TypeScript
function getAbilityRunningInfos(): Promise<Array<AbilityRunningInfo>>
```

Obtains the ability running information. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.app.ability.abilityManager/abilityManager#getAbilityRunningInfos

**Required permissions:** ohos.permission.GET_RUNNING_INFO

<!--Device-abilityManager-function getAbilityRunningInfos(): Promise<Array<AbilityRunningInfo>>--><!--Device-abilityManager-function getAbilityRunningInfos(): Promise<Array<AbilityRunningInfo>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AbilityRunningInfo](arkts-ability-abilityrunninginfo-i.md)&gt;&gt; |


## getAbilityRunningInfos

```TypeScript
function getAbilityRunningInfos(callback: AsyncCallback<Array<AbilityRunningInfo>>): void
```

Obtains the ability running information. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.app.ability.abilityManager/abilityManager#getAbilityRunningInfos

**Required permissions:** ohos.permission.GET_RUNNING_INFO

<!--Device-abilityManager-function getAbilityRunningInfos(callback: AsyncCallback<Array<AbilityRunningInfo>>): void--><!--Device-abilityManager-function getAbilityRunningInfos(callback: AsyncCallback<Array<AbilityRunningInfo>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AbilityRunningInfo](arkts-ability-abilityrunninginfo-i.md)&gt;&gt; | Yes |
