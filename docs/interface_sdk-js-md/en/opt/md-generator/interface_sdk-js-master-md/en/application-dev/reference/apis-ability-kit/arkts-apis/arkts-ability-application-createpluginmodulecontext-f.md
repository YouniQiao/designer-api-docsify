# createPluginModuleContext

## Modules to Import

```TypeScript
import { application } from '@kit.AbilityKit';
```

## createPluginModuleContext

```TypeScript
export function createPluginModuleContext(context: Context, pluginBundleName: string, pluginModuleName: string): Promise<Context>
```

Creates the context of a plugin under the current application based on the context, plugin bundle name, and plugin module name, so as to obtain the basic information about the plugin. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-application-export function createPluginModuleContext(context: Context, pluginBundleName: string, pluginModuleName: string): Promise<Context>--><!--Device-application-export function createPluginModuleContext(context: Context, pluginBundleName: string, pluginModuleName: string): Promise<Context>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes |
| [pluginBundleName](arkts-ability-pluginbundleinfo-i-sys.md) | string | Yes |
| pluginModuleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Context](arkts-ability-context-c.md)&gt; |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, application, common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let moduleContext: common.Context;
    try {
      application.createPluginModuleContext(this.context, 'com.example.pluginBundleName', 'pluginModuleName')
        .then((data: Context) => {
          moduleContext = data;
          console.info('createPluginModuleContext success!');
        })
        .catch((error: BusinessError) => {
          let code: number = (error as BusinessError).code;
          let message: string = (error as BusinessError).message;
          console.error(`createPluginModuleContext failed, error.code: ${code}, error.message: ${message}`);
        });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`createPluginModuleContext failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```
