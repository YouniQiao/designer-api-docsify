# startAbilityForResult

## Modules to Import

```TypeScript
import { featureAbility } from 'kits/@kit.AbilityKit';
```

## startAbilityForResult

```TypeScript
function startAbilityForResult(parameter: StartAbilityParameter, callback: AsyncCallback<AbilityResult>): void
```

Starts an ability. This API uses an asynchronous callback to return the result. The following situations may be possible for a started ability:  
- Normally, you can call  
[terminateSelfWithResult](arkts-ability-featureability-terminateselfwithresult-f.md) to terminate the ability. The result is returned to the caller.  
- If an exception occurs, for example, the ability is killed, an exception message, in which **resultCode** is  
**-1**, is returned to the caller.  
- If different applications call this API to start an ability that uses the singleton mode and then call  
[terminateSelfWithResult](arkts-ability-featureability-terminateselfwithresult-f.md) to terminate the ability, the normal result is returned to the last caller, and an exception message, in which **resultCode** is **-1**, is returned to others.

> **NOTE：**&gt;
> For details about the startup rules for the components in the FA model, see
> [Component Startup Rules (FA Model)](../../../application-models/component-startup-rules-fa.md).

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [StartAbilityParameter](arkts-ability-startabilityparameter-startabilityparameter-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Yes |


## startAbilityForResult

```TypeScript
function startAbilityForResult(parameter: StartAbilityParameter): Promise<AbilityResult>
```

Starts an ability. This API uses a promise to return the result. The following situations may be possible for a started ability:  
- Normally, you can call  
[terminateSelfWithResult](arkts-ability-featureability-terminateselfwithresult-f.md) to terminate the ability. The result is returned to the caller.  
- If an exception occurs, for example, the ability is killed, an exception message, in which **resultCode** is  
**-1**, is returned to the caller.  
- If different applications call this API to start an ability that uses the singleton mode and then call  
[terminateSelfWithResult](arkts-ability-featureability-terminateselfwithresult-f.md) to terminate the ability, the normal result is returned to the last caller, and an exception message, in which **resultCode** is **-1**, is returned to others.

> **NOTE：**&gt;
> For details about the startup rules for the components in the FA model, see
> [Component Startup Rules (FA Model)](../../../application-models/component-startup-rules-fa.md).

**Since:** 7

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [StartAbilityParameter](arkts-ability-startabilityparameter-startabilityparameter-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; |
