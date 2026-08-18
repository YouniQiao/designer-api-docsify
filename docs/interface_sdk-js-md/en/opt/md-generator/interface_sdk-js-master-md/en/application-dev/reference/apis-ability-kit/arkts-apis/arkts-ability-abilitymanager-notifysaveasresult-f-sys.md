# notifySaveAsResult (System API)

## Modules to Import

```TypeScript
```

## notifySaveAsResult

```TypeScript
function notifySaveAsResult(parameter: AbilityResult, requestCode: number, callback: AsyncCallback<void>): void
```

Used by the [Data Loss Prevention (DLP)](../../apis-data-protection-kit/arkts-apis/arkts-dlppermission.md#ohosdlppermission) management application to notify a sandbox application of the data saving result. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-function notifySaveAsResult(parameter: AbilityResult, requestCode: int, callback: AsyncCallback<void>): void--><!--Device-abilityManager-function notifySaveAsResult(parameter: AbilityResult, requestCode: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | Yes |
| requestCode | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## notifySaveAsResult

```TypeScript
function notifySaveAsResult(parameter: AbilityResult, requestCode: number): Promise<void>
```

Used by the [Data Loss Prevention (DLP)](../../apis-data-protection-kit/arkts-apis/arkts-dlppermission.md#ohosdlppermission) management application to notify a sandbox application of the data saving result. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-function notifySaveAsResult(parameter: AbilityResult, requestCode: int): Promise<void>--><!--Device-abilityManager-function notifySaveAsResult(parameter: AbilityResult, requestCode: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | Yes |
| requestCode | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
