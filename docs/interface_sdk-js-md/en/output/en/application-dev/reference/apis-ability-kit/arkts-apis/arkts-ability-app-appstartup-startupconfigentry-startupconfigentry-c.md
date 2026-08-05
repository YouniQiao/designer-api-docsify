# StartupConfigEntry

The module provides the capability to configure \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class StartupConfigEntry--><!--Device-unnamed-declare class StartupConfigEntry-End-->

**System capability:** SystemCapability.Ability.AppStartup

## onConfig

```TypeScript
onConfig?(): StartupConfig
```

Called if the HAP of the AbilityStage has \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ . This callback is triggered before [AbilityStage.onCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_. You can set the AppStartup configuration within this callback. For details, see \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupConfigEntry-onConfig?(): StartupConfig--><!--Device-StartupConfigEntry-onConfig?(): StartupConfig-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | AppStartup configuration. |

**Example**

```TypeScript
import { StartupConfig, StartupConfigEntry, StartupListener } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyStartupConfigEntry extends StartupConfigEntry {
  onConfig() {
    hilog.info(0x0000, 'testTag', `onConfig`);
    let onCompletedCallback = (error: BusinessError<void>) => {
      hilog.info(0x0000, 'testTag', `onCompletedCallback`);
      if (error) {
        hilog.info(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code,
          error.message);
      } else {
        hilog.info(0x0000, 'testTag', `onCompletedCallback: success.`);
      }
    }
    let startupListener: StartupListener = {
      'onCompleted': onCompletedCallback
    }
    let config: StartupConfig = {
      'timeoutMs': 10000,
      'startupListener': startupListener
    }
    return config;
  }
}
```

## onConfig

```TypeScript
onConfig(): StartupConfig
```

Called when startup initialization to configure startup mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupConfigEntry-onConfig(): StartupConfig--><!--Device-StartupConfigEntry-onConfig(): StartupConfig-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The developer returns a startup configuration. |

## onRequestCustomMatchRule

```TypeScript
onRequestCustomMatchRule(want: Want): string
```

Called if the HAP of the AbilityStage has \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ . This callback is triggered after [StartupConfigEntry.onConfig]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ but before [AbilityStage.onCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_. You can use this callback to return different custom matching rules based on parameters in the Want object passed by the caller to start the UIAbility. . AppStartup matches these rules with the **customization** field in **matchRules** of the startup task configuration. If a match is successful, the task is executed automatically. For details about the matching rules, see \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_. This API is typically used in scenarios where tasks cannot be matched directly using URI, action, or intent name rules. It allows for further refinement of matching rules.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupConfigEntry-onRequestCustomMatchRule(want: Want): string--><!--Device-StartupConfigEntry-onRequestCustomMatchRule(want: Want): string-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Want information about the target UIAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Custom matching rule, which is used to determine whether to automatically execute the task. |

**Example**

```TypeScript
import { StartupConfigEntry, Want } from '@kit.AbilityKit';

export default class MyStartupConfigEntry extends StartupConfigEntry {
  // ...

  onRequestCustomMatchRule(want: Want): string {
    if (want?.parameters?.customParam == 'param1') {
      return 'customRule1';
    }
    return '';
  }
}
```

