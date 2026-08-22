# StartupTask

The module provides capabilities related to startup tasks in [AppStartup](../../../application-models/app-startup.md).

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-declare class StartupTask--><!--Device-unnamed-declare class StartupTask-End-->

**System capability:** SystemCapability.Ability.AppStartup

## Modules to Import

```TypeScript
```

## init

```TypeScript
init(context: AbilityStageContext): Promise<Any> | Promise<void>
```

Initializes current startup task. A developer could override this function to init current task and return a result for other tasks.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupTask-init(context: AbilityStageContext): Promise<Any> | Promise<void>--><!--Device-StartupTask-init(context: AbilityStageContext): Promise<Any> | Promise<void>-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [AbilityStageContext](../../apis-ability-kit/arkts-apis/arkts-ability-abilitystagecontext-c.md) | Yes | Indicates ability stage context. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Any&gt; \| Promise&lt;void&gt; | The result of initialization. |

## onDependencyCompleted

```TypeScript
onDependencyCompleted(dependency: string, result: Any): void
```

Called when specific dependent task complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupTask-onDependencyCompleted(dependency: string, result: Any): void--><!--Device-StartupTask-onDependencyCompleted(dependency: string, result: Any): void-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dependency | string | Yes | Indicates name of specific dependent startup task. |
| result | Any | Yes | Indicates result of specific dependent startup task. |

