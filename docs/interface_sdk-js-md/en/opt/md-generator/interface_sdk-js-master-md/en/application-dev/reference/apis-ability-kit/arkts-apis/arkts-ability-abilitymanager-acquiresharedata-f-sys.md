# acquireShareData (System API)

## Modules to Import

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## acquireShareData

```TypeScript
function acquireShareData(missionId: number, callback: AsyncCallback<Record<string, Object>>): void
```

Called by a system dialog box to obtain shared data, which is set by the target UIAbility through  
[onShare](arkts-ability-app-ability-uiability-uiability-c.md#onshare). This API uses an  asynchronous callback to return the result.

**Since:** 10

<!--Device-abilityManager-function acquireShareData(missionId: int, callback: AsyncCallback<Record<string, Object>>): void--><!--Device-abilityManager-function acquireShareData(missionId: int, callback: AsyncCallback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| missionId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Record&lt;string, Object&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## acquireShareData

```TypeScript
function acquireShareData(missionId: number): Promise<Record<string, Object>>
```

Called by a system dialog box to obtain shared data, which is set by the target UIAbility through  
[onShare](arkts-ability-app-ability-uiability-uiability-c.md#onshare). This API uses a promise to return the result.

**Since:** 10

<!--Device-abilityManager-function acquireShareData(missionId: int): Promise<Record<string, Object>>--><!--Device-abilityManager-function acquireShareData(missionId: int): Promise<Record<string, Object>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| missionId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;{ [key: string]: Object |
| Promise&lt;Record&lt;string, Object&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
