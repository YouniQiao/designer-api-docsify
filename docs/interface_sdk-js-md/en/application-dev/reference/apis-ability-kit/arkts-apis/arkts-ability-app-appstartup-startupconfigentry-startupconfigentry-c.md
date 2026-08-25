# StartupConfigEntry

The module provides the capability to configure [AppStartup](../../../application-models/app-startup.md).

**Since:** 12

**System capability:** SystemCapability.Ability.AppStartup

## Modules to Import

```TypeScript
import { StartupConfigEntry } from 'kits/@kit.AbilityKit';
```

## onConfig

```TypeScript
onConfig?(): StartupConfig
```

Called if the HAP of the AbilityStage has [defined the AppStartup configuration file](../../../application-models/app-startup.md#defining-startup-parameter-configuration). This callback is triggered before [AbilityStage.onCreate](arkts-ability-app-ability-abilitystage-abilitystage-c.md#oncreate).You can set the AppStartup configuration within this callback. For details, see [Setting Startup Parameters](../../../application-models/app-startup.md#setting-startup-parameters).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AppStartup

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [StartupConfig](arkts-ability-app-appstartup-startupconfig-startupconfig-i.md) |

## onRequestCustomMatchRule

```TypeScript
onRequestCustomMatchRule(want: Want): string
```

Called if the HAP of the AbilityStage has [defined the AppStartup configuration file](../../../application-models/app-startup.md#defining-startup-parameter-configuration). This callback is triggered after StartupConfigEntry.onConfig but before [AbilityStage.onCreate](arkts-ability-app-ability-abilitystage-abilitystage-c.md#oncreate).You can use this callback to return different custom matching rules based on parameters in the Want object passed by the caller to start the UIAbility. . AppStartup matches these rules with the **customization** field in **matchRules** of the startup task configuration. If a match is successful, the task is executed automatically. For details about the matching rules, see [Adding Task Matching Rules](../../../application-models/app-startup.md#adding-task-matching-rules).This API is typically used in scenarios where tasks cannot be matched directly using URI, action, or intent name rules. It allows for further refinement of matching rules.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
