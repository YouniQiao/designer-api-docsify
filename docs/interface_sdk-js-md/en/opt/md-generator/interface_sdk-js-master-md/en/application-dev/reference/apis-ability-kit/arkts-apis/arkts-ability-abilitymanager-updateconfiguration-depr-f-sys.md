# updateConfiguration (System API)

## updateConfiguration

```TypeScript
function updateConfiguration(config: Configuration, callback: AsyncCallback<void>): void
```

Updates the configuration. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [updateConfiguration](ohos.app.ability.abilityManager/abilityManager#updateConfiguration)

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-abilityManager-function updateConfiguration(config: Configuration, callback: AsyncCallback<void>): void--><!--Device-abilityManager-function updateConfiguration(config: Configuration, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [Configuration](arkts-ability-application-configuration-configuration-depr-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## updateConfiguration

```TypeScript
function updateConfiguration(config: Configuration): Promise<void>
```

Updates the configuration. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [updateConfiguration](ohos.app.ability.abilityManager/abilityManager#updateConfiguration)

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-abilityManager-function updateConfiguration(config: Configuration): Promise<void>--><!--Device-abilityManager-function updateConfiguration(config: Configuration): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [Configuration](arkts-ability-application-configuration-configuration-depr-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
