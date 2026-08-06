# createModuleContextSync

## createModuleContextSync

```TypeScript
export function createModuleContextSync(context: Context, moduleName: string): Context
```

Creates the context for a module. The  
[resourceManager.Configuration]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ in the created module context inherits from the input context, making it convenient for you to access  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_
    **NOTE**  
    
    Creating a module context involves resource querying and initialization, which can be time-consuming. In  
    scenarios where application fluidity is critical, avoid frequently or repeatedly calling the  
    **createModuleContext** API to create multiple context instances, as this may negatively impact user experience.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-application-export function createModuleContextSync(context: Context, moduleName: string): Context--><!--Device-application-export function createModuleContextSync(context: Context, moduleName: string): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Application context. |
| moduleName | string | Yes | Module name. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return the context created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| 16000021 | The module does not exist. |

