# StartupTask

The module provides capabilities related to startup tasks in  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-declare class StartupTask--><!--Device-unnamed-declare class StartupTask-End-->

**System capability:** SystemCapability.Ability.AppStartup

## init

```TypeScript
init(context: AbilityStageContext): Promise<Any> | Promise<void>
```

Initializes current startup task.A developer could override this function to init current task and return a result for other tasks.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupTask-init(context: AbilityStageContext): Promise<Any> | Promise<void>--><!--Device-StartupTask-init(context: AbilityStageContext): Promise<Any> | Promise<void>-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates ability stage context. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Any&gt; | The result of initialization. |

## onDependencyCompleted

```TypeScript
onDependencyCompleted(dependency: string, result: Any): void
```

Called when specific dependent task complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupTask-onDependencyCompleted(dependency: string, result: Any): void--><!--Device-StartupTask-onDependencyCompleted(dependency: string, result: Any): void-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dependency | string | Yes | Indicates name of specific dependent startup task. |
| result | Any | Yes | Indicates result of specific dependent startup task. |

