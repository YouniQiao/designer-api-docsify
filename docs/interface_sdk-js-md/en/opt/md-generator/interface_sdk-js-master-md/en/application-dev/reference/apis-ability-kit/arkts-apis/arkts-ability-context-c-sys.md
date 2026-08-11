# Context

Context is the context base class of the stage model. It is used to access application-specific resources and perform callbacks for application-level operations.../../../

**Inheritance/Implementation:** Context extends [BaseContext](arkts-ability-basecontext-c.md)

**Since:** 9

<!--Device-unnamed-declare class Context extends BaseContext--><!--Device-unnamed-declare class Context extends BaseContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## createBundleContext

```TypeScript
createBundleContext(bundleName: string): Context
```

Creates the context based on the bundle name.

> **NOTE：**
> 
> If there are multiple modules in the stage model, resource ID conflicts may occur. You are advised to use
> [application.createModuleContext](arkts-ability-application-createmodulecontext-f.md#createmodulecontext)
> instead.
> 
> This API has been supported since API version 9 and deprecated since API version 12. You are advised to use
> [application.createBundleContext](arkts-ability-application-createbundlecontext-f-sys.md#createbundlecontext)
> instead.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [@ohos.app.ability.application:application.createBundleContext](arkts-ability-application-createbundlecontext-f-sys.md#createbundlecontext)

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-Context-createBundleContext(bundleName: string): Context--><!--Device-Context-createBundleContext(bundleName: string): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## createModuleContext

```TypeScript
createModuleContext(bundleName: string, moduleName: string): Context
```

Creates the context based on the bundle name and module name.

> **NOTE：**
> 
> This API has been supported since API version 9 and deprecated since API version 12. You are advised to use
> [application.createModuleContext](arkts-ability-application-createmodulecontext-f.md#createmodulecontext)
> instead.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [@ohos.app.ability.application:application.createModuleContext](arkts-ability-application-createmodulecontext-f.md#createmodulecontext)

**Model restriction:** This API can be used only in the stage model.

<!--Device-Context-createModuleContext(bundleName: string, moduleName: string): Context--><!--Device-Context-createModuleContext(bundleName: string, moduleName: string): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## createModuleResourceManager

```TypeScript
createModuleResourceManager(bundleName: string, moduleName: string): resmgr.ResourceManager
```

Creates a resource management object for a module.

**Since:** 11

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-Context-createModuleResourceManager(bundleName: string, moduleName: string): resmgr.ResourceManager--><!--Device-Context-createModuleResourceManager(bundleName: string, moduleName: string): resmgr.ResourceManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| resmgr.ResourceManager |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## createSystemHspModuleResourceManager

```TypeScript
createSystemHspModuleResourceManager(bundleName: string, moduleName: string): resmgr.ResourceManager
```

Creates a  
[resource manager](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-getresourcemanager-f.md/arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager)for an OEM-preset [system-level HSP](../../../quick-start/application-package-glossary.md#system-level-hsp).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-Context-createSystemHspModuleResourceManager(bundleName: string, moduleName: string): resmgr.ResourceManager--><!--Device-Context-createSystemHspModuleResourceManager(bundleName: string, moduleName: string): resmgr.ResourceManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| resmgr.ResourceManager |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16400001](../errorcode-ability.md#16400001-target-application-type-is-not-a-system-hsp) |
