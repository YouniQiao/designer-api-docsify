# createModuleContextSync

## Modules to Import

```TypeScript
import { application } from '@kit.AbilityKit';
```

## createModuleContextSync

```TypeScript
export function createModuleContextSync(context: Context, moduleName: string): Context
```

Creates the context for a module. The  
[resourceManager.Configuration](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-configuration-c.md#Configuration) in the created module context inherits from the input context, making it convenient for you to access  
[application resources across HAP/HSP packages](../../../quick-start/resource-categories-and-access.md#cross-haphsp-resources)

> **NOTE：**
> 
> Creating a module context involves resource querying and initialization, which can be time-consuming. In
> scenarios where application fluidity is critical, avoid frequently or repeatedly calling the
> **createModuleContext** API to create multiple context instances, as this may negatively impact user experience.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-application-export function createModuleContextSync(context: Context, moduleName: string): Context--><!--Device-application-export function createModuleContextSync(context: Context, moduleName: string): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes |
| moduleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Context](arkts-ability-context-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| 16000021 |
| [16000011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |
