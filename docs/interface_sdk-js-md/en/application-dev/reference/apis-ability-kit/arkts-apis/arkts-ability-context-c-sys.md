# Context

Context is the context base class of the stage model. It is used to access application-specific resources and perform callbacks for application-level operations. ../../../

**Inheritance/Implementation:** Context extends BaseContext

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## createBundleContext

```TypeScript
createBundleContext(bundleName: string): Context
```

Creates the context based on the bundle name.

> **NOTE：**&gt;
> If there are multiple modules in the stage model, resource ID conflicts may occur. You are advised to use
> [application.createModuleContext](arkts-ability-application-createmodulecontext-f.md)
> instead.&gt;
> This API has been supported since API version 9 and deprecated since API version 12. You are advised to use
> [application.createBundleContext](arkts-ability-application-createbundlecontext-f-sys.md)
> instead.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [createBundleContext](arkts-ability-application-createbundlecontext-f-sys.md)

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Context](arkts-ability-context-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createModuleContext

```TypeScript
createModuleContext(bundleName: string, moduleName: string): Context
```

Creates the context based on the bundle name and module name.

> **NOTE：**&gt;
> This API has been supported since API version 9 and deprecated since API version 12. You are advised to use
> [application.createModuleContext](arkts-ability-application-createmodulecontext-f.md)
> instead.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [createModuleContext](arkts-ability-application-createmodulecontext-f.md)

**Model restriction:** This API can be used only in the stage model.

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
| [Context](arkts-ability-context-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createModuleResourceManager

```TypeScript
createModuleResourceManager(bundleName: string, moduleName: string): resmgr.ResourceManager
```

Creates a resource management object for a module.

**Since:** 11

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createSystemHspModuleResourceManager

```TypeScript
createSystemHspModuleResourceManager(bundleName: string, moduleName: string): resmgr.ResourceManager
```

Creates a [resource manager](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-getresourcemanager-f.md) for an OEM-preset [system-level HSP](../../../quick-start/application-package-glossary.md#system-level-hsp).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16400001](../errorcode-ability.md#16400001-target-application-type-is-not-a-system-hsp) |
