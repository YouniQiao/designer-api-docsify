# updateConfiguration (System API)

## updateConfiguration

```TypeScript
function updateConfiguration(config: Configuration, callback: AsyncCallback<void>): void
```

Updates the configuration. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** updateConfiguration

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-abilityManager-function updateConfiguration(config: Configuration, callback: AsyncCallback<void>): void--><!--Device-abilityManager-function updateConfiguration(config: Configuration, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [Configuration](../../apis-arkui/arkts-components/arkts-arkui-configuration-i.md) | Yes | New configuration. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-i.md)<void> | Yes | Callback used to return the result. If the configuration is updated, **err** is undefined; otherwise, **err** is an error object. |


## updateConfiguration

```TypeScript
function updateConfiguration(config: Configuration): Promise<void>
```

Updates the configuration. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** updateConfiguration

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-abilityManager-function updateConfiguration(config: Configuration): Promise<void>--><!--Device-abilityManager-function updateConfiguration(config: Configuration): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [Configuration](../../apis-arkui/arkts-components/arkts-arkui-configuration-i.md) | Yes | New configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| [Promise](../../apis-na/arkts-apis/arkts-na-promise-i.md)<void> | Promise that returns no value. |

