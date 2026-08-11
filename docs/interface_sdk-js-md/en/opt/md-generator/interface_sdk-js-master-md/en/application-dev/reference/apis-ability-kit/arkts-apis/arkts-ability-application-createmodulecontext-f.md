# createModuleContext

## Modules to Import

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## createModuleContext

```TypeScript
export function createModuleContext(context: Context, moduleName: string): Promise<Context>
```

Creates the context for a module. The  
[resourceManager.Configuration](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-configuration-c.md/arkts-localization-resourcemanager-configuration-c.md) in the created module context inherits from the input context, making it convenient for you to access  
[application resources across HAP/HSP packages](../../../quick-start/resource-categories-and-access.md#cross-haphsp-resources). This API uses a promise to return the result.

> **NOTE：**
> 
> Creating a module context involves resource querying and initialization, which can be time-consuming. In
> scenarios where application fluidity is critical, avoid frequently or repeatedly calling the
> **createModuleContext** API to create multiple context instances, as this may negatively impact user experience.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-application-export function createModuleContext(context: Context, moduleName: string): Promise<Context>--><!--Device-application-export function createModuleContext(context: Context, moduleName: string): Promise<Context>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes |
| moduleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Context](arkts-ability-context-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, application, common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let moduleContext: common.Context;
    try {
      application.createModuleContext(this.context, 'entry').then((data: Context) => {
        moduleContext = data;
        console.info('createModuleContext success!');
      }).catch((error: BusinessError) => {
        let code: number = (error as BusinessError).code;
        let message: string = (error as BusinessError).message;
        console.error(`createModuleContext failed, error.code: ${code}, error.message: ${message}`);
      });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`createModuleContext failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```
