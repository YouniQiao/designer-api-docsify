# createPluginModuleContext

## Modules to Import

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## createPluginModuleContext

```TypeScript
export function createPluginModuleContext(context: Context, pluginBundleName: string, pluginModuleName: string): Promise<Context>
```

Creates the context of a plugin under the current application based on the context, plugin bundle name, and plugin module name, so as to obtain the basic information about the plugin. This API uses a promise to return the result.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes |
| [pluginBundleName](arkts-ability-pluginbundleinfo-i.md) | string | Yes |
| pluginModuleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Context](arkts-ability-context-c.md)&gt; |
