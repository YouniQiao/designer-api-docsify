# getAbilityRunningInfos (System API)

## Modules to Import

```TypeScript
```

## getAbilityRunningInfos

```TypeScript
function getAbilityRunningInfos(): Promise<Array<AbilityRunningInfo>>
```

Obtains the ability running information. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f.md)

**Required permissions:** ohos.permission.GET_RUNNING_INFO

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[AbilityRunningInfo](arkts-ability-abilityrunninginfo-i.md)&gt;&gt; | Promise used to return the ability running information. |

**Examples**

```TypeScript
import abilityManager from '@ohos.application.abilityManager';
import { BusinessError } from '@ohos.base';

abilityManager.getAbilityRunningInfos().then((data) => {
  console.info(`getAbilityRunningInfos success, data: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`getAbilityRunningInfos error code : ${error.code}, error msg: ${error.message}.`);
});
```


## getAbilityRunningInfos

```TypeScript
function getAbilityRunningInfos(callback: AsyncCallback<Array<AbilityRunningInfo>>): void
```

Obtains the ability running information. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f.md)

**Required permissions:** ohos.permission.GET_RUNNING_INFO

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AbilityRunningInfo](arkts-ability-abilityrunninginfo-i.md)&gt;&gt; | Yes | Callback used to return the ability running information. |

**Examples**

```TypeScript
import abilityManager from '@ohos.application.abilityManager';
import { BusinessError } from '@ohos.base';

abilityManager.getAbilityRunningInfos((error: BusinessError, data) => {
  if (error) {
    console.error(`GetAbilityRunningInfos failed, error code: ${error.code}, error msg: ${error.message}.`);
    return;
  }
  console.info(`GetAbilityRunningInfos success, data: ${JSON.stringify(data)}.`);
});
```
