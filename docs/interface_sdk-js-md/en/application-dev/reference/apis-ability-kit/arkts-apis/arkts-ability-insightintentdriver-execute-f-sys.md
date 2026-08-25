# execute (System API)

## Modules to Import

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## execute

```TypeScript
function execute(param: ExecuteParam, callback: AsyncCallback<insightIntent.ExecuteResult>): void
```

Executes a call to an intent. This API uses an asynchronous callback to return the result. When the caller is in the background, the ohos.permission.START_ABILITIES_FROM_BACKGROUND permission is required. When [ExecuteMode](arkts-ability-insightintent-executemode-e.md) of the intent call is set to **UI_ABILITY_BACKGROUND**, the ohos.permission.ABILITY_BACKGROUND_COMMUNICATION permission is required. On API 26.0.0 and above, intent can be executed across devices. When the intent call is cross-device, the ohos.permission.EXECUTE_DISTRIBUTED_INTENT permission is required.

**Since:** 11

**Required permissions:** ohos.permission.EXECUTE_INSIGHT_INTENT

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [ExecuteParam](arkts-ability-insightintentdriver-executeparam-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;insightIntent.ExecuteResult&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-cross-user-operation-is-not-allowed) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000010](../errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installation-free-timeout) |
| 16000137 |
| 16000138 |


## execute

```TypeScript
function execute(param: ExecuteParam): Promise<insightIntent.ExecuteResult>
```

Executes a call to an intent. This API uses a promise to return the result. When the caller is in the background, the ohos.permission.START_ABILITIES_FROM_BACKGROUND permission is required. When [ExecuteMode](arkts-ability-insightintent-executemode-e.md) of the intent call is set to **UI_ABILITY_BACKGROUND**, the ohos.permission.ABILITY_BACKGROUND_COMMUNICATION permission is required. When the intent call is cross-device, the ohos.permission.EXECUTE_DISTRIBUTED_INTENT permission is required. On API 26.0.0 and above, intent can be executed across devices. When the intent call is cross-device, the ohos.permission.EXECUTE_DISTRIBUTED_INTENT permission is required.

**Since:** 11

**Required permissions:** ohos.permission.EXECUTE_INSIGHT_INTENT

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [ExecuteParam](arkts-ability-insightintentdriver-executeparam-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;insightIntent.ExecuteResult & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-cross-user-operation-is-not-allowed) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000010](../errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installation-free-timeout) |
| 16000137 |
| 16000138 |
