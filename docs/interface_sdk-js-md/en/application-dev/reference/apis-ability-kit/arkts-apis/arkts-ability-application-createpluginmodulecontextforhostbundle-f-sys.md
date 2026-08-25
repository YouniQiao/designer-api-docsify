# createPluginModuleContextForHostBundle (System API)

## Modules to Import

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## createPluginModuleContextForHostBundle

```TypeScript
export function createPluginModuleContextForHostBundle(context: Context, pluginBundleName: string, pluginModuleName: string,
    hostBundleName: string): Promise<Context>
```

Creates the context for a plugin based on a given context, plugin bundle name, plugin module name, and application bundle name to obtain the basic information about the plugin. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes |
| [pluginBundleName](arkts-ability-pluginbundleinfo-i.md) | string | Yes |
| pluginModuleName | string | Yes |
| [hostBundleName](../../apis-form-kit/arkts-apis/arkts-form-forminfo-runningforminfo-i-sys.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Context](arkts-ability-context-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
