# createModuleContextSync

## Modules to Import

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## createModuleContextSync

```TypeScript
export function createModuleContextSync(context: Context, moduleName: string): Context
```

创建指定模块的上下文。创建出的模块上下文中[resourceManager.Configuration](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-configuration-c.md/arkts-localization-resourcemanager-configuration-c.md)资源继承自入参上下文，便于开发者获取[跨HAP/HSP包应用资源](../../../quick-start/resource-categories-and-access.md#跨haphsp包应用资源)。

> **说明：**
> 
> 由于创建模块上下文的过程涉及资源查询与初始化，耗时相对较长，在对应用流畅性要求较高的场景下，不建议频繁或多次调用createModuleContext接口创建多个Context实例，以免影响用户体验。

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-application-export function createModuleContextSync(context: Context, moduleName: string): Context--><!--Device-application-export function createModuleContextSync(context: Context, moduleName: string): Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes | 表示应用上下文。 |
| moduleName | string | Yes | 表示应用模块名。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Context](arkts-ability-context-c.md) | 返回创建的上下文。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000021 | 模块不存在。 |
| 16000011 | 上下文不存在。 |

