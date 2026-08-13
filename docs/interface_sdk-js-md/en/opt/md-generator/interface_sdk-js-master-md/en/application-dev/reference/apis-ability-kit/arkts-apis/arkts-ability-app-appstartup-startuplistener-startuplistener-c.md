# StartupListener

The module defines the task listener used in [App Startup](../../../application-models/app-startup.md).

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare class StartupListener--><!--Device-unnamed-declare class StartupListener-End-->

**System capability:** SystemCapability.Ability.AppStartup

## Modules to Import

```TypeScript
import { StartupListener } from '@kit.AbilityKit';
```

## onCompleted

```TypeScript
onCompleted?(error: BusinessError<void>): void
```

Called when all startup tasks complete.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupListener-onCompleted?(error: BusinessError<void>): void--><!--Device-StartupListener-onCompleted?(error: BusinessError<void>): void-End-->

**System capability:** SystemCapability.Ability.AppStartup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| error | [BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&lt;void&gt; | Yes |

## Examples

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
        hilog.error(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code,
          error.message);
      } else {
        hilog.info(0x0000, 'testTag', `onCompletedCallback: success.`);
      }
    };
    let startupListener: StartupListener = {
      'onCompleted': onCompletedCallback
    };
    let config: StartupConfig = {
      'timeoutMs': 10000,
      'startupListener': startupListener
    };
    return config;
  }
}
```

## onCompleted

```TypeScript
onCompleted?: OnCompletedFn
```

Called when all startup tasks complete.

**Type:** [OnCompletedFn](arkts-ability-oncompletedfn-t.md)

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupListener-onCompleted?: OnCompletedFn--><!--Device-StartupListener-onCompleted?: OnCompletedFn-End-->

**System capability:** SystemCapability.Ability.AppStartup
