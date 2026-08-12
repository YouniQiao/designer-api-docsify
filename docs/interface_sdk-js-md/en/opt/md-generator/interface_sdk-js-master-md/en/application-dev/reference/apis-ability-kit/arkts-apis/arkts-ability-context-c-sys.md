# Context

Context is the context base class of the stage model. It is used to access application-specific resources and perform callbacks for application-level operations.../../../

**Inheritance/Implementation:** Context extends [BaseContext](BaseContext)

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
> [application.createModuleContext](arkts-ability-application-createmodulecontext-f.md#createModuleContext-1)
> instead.
> 
> This API has been supported since API version 9 and deprecated since API version 12. You are advised to use
> [application.createBundleContext](arkts-ability-application-createbundlecontext-f-sys.md#createBundleContext)
> instead.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [createBundleContext](arkts-ability-application-createbundlecontext-f-sys.md#createBundleContext)

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
| [Context](arkts-ability-context-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { common, UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate');
    let bundleContext: common.Context;
    try {
      bundleContext = this.context.createBundleContext('com.example.test');
    } catch (error) {
      console.error(`createBundleContext failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}`);
    }
  }
}
```

## createModuleContext

```TypeScript
createModuleContext(bundleName: string, moduleName: string): Context
```

Creates the context based on the bundle name and module name.

> **NOTE：**
> 
> This API has been supported since API version 9 and deprecated since API version 12. You are advised to use
> [application.createModuleContext](arkts-ability-application-createmodulecontext-f.md#createModuleContext-1)
> instead.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [createModuleContext](arkts-ability-application-createmodulecontext-f.md#createModuleContext)

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
| [Context](arkts-ability-context-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { common, UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate');
    let moduleContext: common.Context;
    try {
      moduleContext = this.context.createModuleContext('com.example.test', 'entry');
    } catch (error) {
      console.error(`createModuleContext failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}`);
    }
  }
}
```

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate');
    let ModuleResourceManager: resourceManager.ResourceManager;
    try {
      ModuleResourceManager = this.context.createModuleResourceManager('com.example.test', 'entry');
    } catch (error) {
      console.error(`createModuleResourceManager failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}`);
    }
  }
}
```

## createSystemHspModuleResourceManager

```TypeScript
createSystemHspModuleResourceManager(bundleName: string, moduleName: string): resmgr.ResourceManager
```

Creates a  
[resource manager](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-getresourcemanager-f.md#getResourceManager)for an OEM-preset [system-level HSP](../../../quick-start/application-package-glossary.md#system-level-hsp).

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16400001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16400001-target-application-type-is-not-a-system-hsp) |

## Examples

```TypeScript
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate');
    this.context.createSystemHspModuleResourceManager("com.example.myapplication", "library");
  }
}
```
