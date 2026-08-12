# getTopAbility (System API)

## Modules to Import

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
```

## getTopAbility

```TypeScript
function getTopAbility(): Promise<ElementName>
```

Obtains the top ability, which is the ability that has the window focus. This API uses a promise to return the result.

**Since:** 9

<!--Device-abilityManager-function getTopAbility(): Promise<ElementName>--><!--Device-abilityManager-function getTopAbility(): Promise<ElementName>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ElementName](arkts-ability-elementname-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## getTopAbility

```TypeScript
function getTopAbility(callback: AsyncCallback<ElementName>): void
```

Obtains the top ability, which is the ability that has the window focus. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-abilityManager-function getTopAbility(callback: AsyncCallback<ElementName>): void--><!--Device-abilityManager-function getTopAbility(callback: AsyncCallback<ElementName>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ElementName](arkts-ability-elementname-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
