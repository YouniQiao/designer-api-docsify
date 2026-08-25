# run

## Modules to Import

```TypeScript
import { startupManager } from 'kits/@kit.AbilityKit';
```

## run

```TypeScript
function run(startupTasks: Array<string>, config?: StartupConfig): Promise<void>
```

Runs startup tasks or loads .so files.

> **NOTE：**&gt;
> This API cannot be used to run startup tasks defined in a feature-type HAP. To run those tasks, use
> [startupManager.run](#run)
> .

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startupTasks | Array & lt;string & gt; | Yes |
| config | [StartupConfig](arkts-ability-app-appstartup-startupconfig-startupconfig-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [28800001](../errorcode-ability.md#28800001-startup-task-or-dependency-not-found) |
| [28800002](../errorcode-ability.md#28800002-circular-dependencies-between-startup-tasks) |
| [28800003](../errorcode-ability.md#28800003-error-occurs-during-task-startup) |
| [28800004](../errorcode-ability.md#28800004-executing-the-startup-task-times-out) |


## run

```TypeScript
function run(startupTasks: Array<string>, context: common.AbilityStageContext, config: StartupConfig): Promise<void>
```

Runs startup tasks or loads .so files. You can specify [AbilityStageContext](arkts-ability-abilitystagecontext-c.md) for loading startup tasks. This API uses a promise to return the result.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| startupTasks | Array & lt;string & gt; | Yes |
| context | common.AbilityStageContext | Yes |
| config | [StartupConfig](arkts-ability-app-appstartup-startupconfig-startupconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [28800001](../errorcode-ability.md#28800001-startup-task-or-dependency-not-found) |
| [28800002](../errorcode-ability.md#28800002-circular-dependencies-between-startup-tasks) |
| [28800003](../errorcode-ability.md#28800003-error-occurs-during-task-startup) |
| [28800004](../errorcode-ability.md#28800004-executing-the-startup-task-times-out) |
