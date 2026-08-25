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

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f.md)

**Required permissions:** ohos.permission.GET_RUNNING_INFO

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AbilityRunningInfo](arkts-ability-abilityrunninginfo-i.md)&gt;&gt; |

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

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 9

**Substitutes:** [getAbilityRunningInfos](arkts-ability-abilitymanager-getabilityrunninginfos-f.md)

**Required permissions:** ohos.permission.GET_RUNNING_INFO

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AbilityRunningInfo](arkts-ability-abilityrunninginfo-i.md)&gt;&gt; | Yes |

**Examples**

See [getAbilityRunningInfos](#getabilityrunninginfos)
