# getForegroundUIAbilities (System API)

## Modules to Import

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
```

## getForegroundUIAbilities

```TypeScript
function getForegroundUIAbilities(callback: AsyncCallback<Array<AbilityStateData>>): void
```

Obtains the information about the UIAbility components of an application that is running in the foreground. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.GET_RUNNING_INFO

<!--Device-abilityManager-function getForegroundUIAbilities(callback: AsyncCallback<Array<AbilityStateData>>): void--><!--Device-abilityManager-function getForegroundUIAbilities(callback: AsyncCallback<Array<AbilityStateData>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;AbilityStateData&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

abilityManager.getForegroundUIAbilities((err: BusinessError, data: Array<abilityManager.AbilityStateData>) => {
  if (err) {
    console.error(`Get foreground ui abilities failed, error: ${JSON.stringify(err)}`);
  } else {
    console.info(`Get foreground ui abilities data is: ${JSON.stringify(data)}`);
  }
});
```


## getForegroundUIAbilities

```TypeScript
function getForegroundUIAbilities(): Promise<Array<AbilityStateData>>
```

Obtains the information about the UIAbility components of an application that is running in the foreground. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.GET_RUNNING_INFO

<!--Device-abilityManager-function getForegroundUIAbilities(): Promise<Array<AbilityStateData>>--><!--Device-abilityManager-function getForegroundUIAbilities(): Promise<Array<AbilityStateData>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;AbilityStateData & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

abilityManager.getForegroundUIAbilities().then((data: Array<abilityManager.AbilityStateData>) => {
  console.info(`Get foreground ui abilities data is: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`Get foreground ui abilities failed, error: ${JSON.stringify(error)}`);
});
```
