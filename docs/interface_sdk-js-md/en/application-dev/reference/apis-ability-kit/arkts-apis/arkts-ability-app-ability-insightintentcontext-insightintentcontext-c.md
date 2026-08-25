# InsightIntentContext

The module provides the context for intent execution. It is used as a property in both the [intent execution base class](arkts-ability-app-ability-insightintentexecutor-insightintentexecutor-c.md) and [base class decorated with @InsightIntentEntry](arkts-ability-app-ability-insightintententryexecutor-insightintententryexecutor-c.md), offering essential capabilities for intent implementation, for example, starting [UIAbility components](arkts-ability-app-ability-uiability-uiability-c.md) within the same application.

**Since:** 11

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { InsightIntentContext } from 'kits/@kit.AbilityKit';
```

## setReturnModeForUIAbilityForeground

```TypeScript
setReturnModeForUIAbilityForeground(returnMode: insightIntent.ReturnMode): void
```

Sets the return mode of the intent execution result. This API is applicable to intents with the execution mode set to [UI_ABILITY_FOREGROUND](arkts-ability-insightintent-executemode-e.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| returnMode | insightIntent.ReturnMode | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## setReturnModeForUIExtensionAbility

```TypeScript
setReturnModeForUIExtensionAbility(returnMode: insightIntent.ReturnMode): void
```

Sets the return mode of the intent execution result. This API is applicable to intents with the execution mode set to [UI_EXTENSION_ABILITY](arkts-ability-insightintent-executemode-e.md).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| returnMode | insightIntent.ReturnMode | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startAbility

```TypeScript
startAbility(want: Want, callback: AsyncCallback<void>): void
```

Starts a UIAbility. This API can only be used to start UIAbility components within the same application. This API uses an asynchronous callback to return the result.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-cross-user-operation-is-not-allowed) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installation-free-timeout) |
| [16000061](../errorcode-ability.md#16000061-unsupported-operation) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |

## startAbility

```TypeScript
startAbility(want: Want): Promise<void>
```

Starts a UIAbility. This API can only be used to start UIAbility components within the same application. This API uses a promise to return the result.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-cross-user-operation-is-not-allowed) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installation-free-timeout) |
| [16000061](../errorcode-ability.md#16000061-unsupported-operation) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |

## instanceId

```TypeScript
instanceId: number
```

Unique ID of an intent instance. Its execution result can be returned through [insightIntentProvider.sendExecuteResult] [sendExecuteResult](arkts-ability-insightintentprovider-sendexecuteresult-f.md) and [insightIntentProvider.sendIntentResult] [sendIntentResult](arkts-ability-insightintentprovider-sendintentresult-f.md).

**Type:** number

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
