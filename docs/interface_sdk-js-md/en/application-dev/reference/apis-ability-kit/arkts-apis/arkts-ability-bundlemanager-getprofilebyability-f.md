# getProfileByAbility

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getProfileByAbility

```TypeScript
function getProfileByAbility(moduleName: string, abilityName: string, metadataName: string, callback: AsyncCallback<Array<string>>): void
```

Obtains the JSON string array of the current application's configuration file based on the given module name, ability name, and metadata name (name configured under **metadata** in [abilities](../../../quick-start/module-configuration-file.md#abilities) of the **module.json5** file). This API uses an asynchronous callback to return the result.

> NOTE&gt;
> If the profile uses the resource reference format, the return value retains this format (for example,
> **\$string:res_id**). You can obtain the referenced resources through related APIs of the
> [resource manager module](../../apis-localization-kit/arkts-apis/arkts-resourcemanager.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| abilityName | string | Yes |
| metadataName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700003](../errorcode-bundle.md#17700003-ability-name-does-not-exist) |
| [17700024](../errorcode-bundle.md#17700024-profile-does-not-exist) |
| [17700029](../errorcode-bundle.md#17700029-disabled-ability) |


## getProfileByAbility

```TypeScript
function getProfileByAbility(moduleName: string, abilityName: string, metadataName?: string): Promise<Array<string>>
```

Obtains the JSON string array of the current application's configuration file based on the given module name, ability name, and metadata name (name configured under **metadata** in [abilities](../../../quick-start/module-configuration-file.md#abilities) of the **module.json5** file). This API uses a promise to return the result.

> NOTE&gt;
> If the profile uses the resource reference format, the return value retains this format (for example,
> **\$string:res_id**). You can obtain the referenced resources through related APIs of the
> [resource manager module](../../apis-localization-kit/arkts-apis/arkts-resourcemanager.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| abilityName | string | Yes |
| metadataName | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700003](../errorcode-bundle.md#17700003-ability-name-does-not-exist) |
| [17700024](../errorcode-bundle.md#17700024-profile-does-not-exist) |
| [17700029](../errorcode-bundle.md#17700029-disabled-ability) |
