# AbilityStage

AbilityStage is a [module](../../../quick-start/application-package-overview.md#multi-module-design-mechanism)-level component manager. It is used for initializing operations such as resource preloading and thread creation at the module level, as well as maintaining the application state under the module. An AbilityStage instance corresponds to a module. When the [HAP](../../../quick-start/hap-package.md) or [HSP](../../../quick-start/in-app-hsp.md) of an application is first loaded, an AbilityStage instance is created. If a module contains both AbilityStage and other components ( like UIAbility or ExtensionAbility), the AbilityStage instance is created before the other component instances. An AbilityStage has the lifecycle callbacks [onCreate()](#oncreate) and [onDestroy()](#ondestroy), and the event callbacks [onAcceptWant()](#onacceptwant), [onConfigurationUpdate()](#onconfigurationupdate), and [onMemoryLevel()](#onmemorylevel).

**Since:** 23

<!--Device-unnamed-declare class AbilityStage--><!--Device-unnamed-declare class AbilityStage-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
```

## onAboutToCreateAbility

```TypeScript
onAboutToCreateAbility(): void
```

Called when the ability stage is about to create the first ability. If both this method and [onAboutToCreateAbilityAsync](#onabouttocreateabilityasync) are overridden, only [onAboutToCreateAbilityAsync](#onabouttocreateabilityasync) takes effect.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityStage-onAboutToCreateAbility(): void--><!--Device-AbilityStage-onAboutToCreateAbility(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onAboutToCreateAbilityAsync

```TypeScript
onAboutToCreateAbilityAsync(): Promise<void>
```

Called when the ability stage is about to create the first ability. This API uses a promise to return the result. Subsequent lifecycle callbacks will be suspended until the returned Promise is resolved. If both [onAboutToCreateAbility](#onabouttocreateability) and this method are overridden, only this method takes effect.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityStage-onAboutToCreateAbilityAsync(): Promise<void>--><!--Device-AbilityStage-onAboutToCreateAbilityAsync(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## onAcceptWant

```TypeScript
onAcceptWant(want: Want): string
```

Called when a UIAbility with the launch mode set to [specified](../../../application-models/uiability-launch-type.md#specified) is launched. This API returns a string representing the unique ID of the UIAbility instance. This API returns the result synchronously and does not support asynchronous callbacks. If a UIAbility instance with the same ID already exists in the system, that instance is reused. Otherwise, a new instance is created. > **NOTE：**> > Starting from API version 20, this callback is not triggered when > [AbilityStage.onAcceptWantAsync](#onacceptwantasync) is implemented.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStage-onAcceptWant(want: Want): string--><!--Device-AbilityStage-onAcceptWant(want: Want): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
import { AbilityStage, Want } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onAcceptWant(want: Want) {
    console.info('MyAbilityStage.onAcceptWant called');
    return 'com.example.test';
  }
}
```

## onAcceptWantAsync

```TypeScript
onAcceptWantAsync(want: Want): Promise<string>
```

Called when a UIAbility with the launch mode set to [specified](../../../application-models/uiability-launch-type.md#specified) is launched. This API returns a string representing the unique ID of the UIAbility instance. This API uses a promise to return the result. If a UIAbility instance with the same ID already exists in the system, that instance is reused. Otherwise, a new instance is created.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AbilityStage-onAcceptWantAsync(want: Want): Promise<string>--><!--Device-AbilityStage-onAcceptWantAsync(want: Want): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Examples**

```TypeScript
import { AbilityStage } from '@kit.AbilityKit';

class MyAbilityStage extends AbilityStage {
  async onAcceptWantAsync(): Promise<string> {
    await new Promise<string>((res, rej) => {
      setTimeout(res, 1000); // Execute the operation after 1 second.
    });
    return 'default';
  }
}
```

## onConfigurationUpdate

```TypeScript
onConfigurationUpdate(newConfig: Configuration): void
```

Called when the system global configuration (such as the system language and dark/light color mode) changes. All the configuration items are defined in the [Configuration](arkts-ability-app-ability-configuration-configuration-i.md#configuration) class. This API returns the result synchronously and does not support asynchronous callbacks. > **NOTE：**> > There are certain restrictions when this callback is actually triggered. For example, if you set the application > language by calling [setLanguage](arkts-ability-applicationcontext-c.md#setlanguage), the > system does not trigger the **onConfigurationUpdate** callback even if the system language changes. For details, > see [When to Use](../../../application-models/subscribe-system-environment-variable-changes.md#when-to-use).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStage-onConfigurationUpdate(newConfig: Configuration): void--><!--Device-AbilityStage-onConfigurationUpdate(newConfig: Configuration): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newConfig | [Configuration](arkts-ability-app-ability-configuration-configuration-i.md) | Yes |

**Examples**

```TypeScript
import { AbilityStage, Configuration } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onConfigurationUpdate(config: Configuration) {
    console.info(`MyAbilityStage.onConfigurationUpdate, language: ${config.language}`);
  }
}
```

## onCreate

```TypeScript
onCreate(): void
```

Called when an AbilityStage instance is created. Such an instance is automatically created by the system before it loads the first Ability instance of the module. You can initialize the module (for example, preload resources or create threads) in this callback. This API returns the result synchronously and does not support asynchronous callbacks.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStage-onCreate(): void--><!--Device-AbilityStage-onCreate(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Examples**

```TypeScript
import { AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    console.info('MyAbilityStage.onCreate is called');
  }
}
```

## onDestroy

```TypeScript
onDestroy(): void
```

Called when the last Ability instance of the corresponding module exits. This API is called during the normal lifecycle. If the application exits abnormally or is terminated, this API is not called. This API returns the result synchronously and does not support asynchronous callbacks.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AbilityStage-onDestroy(): void--><!--Device-AbilityStage-onDestroy(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Examples**

```TypeScript
import { AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onDestroy() {
    console.info('MyAbilityStage.onDestroy is called');
  }
}
```

## onLaunchFromHyperSnap

```TypeScript
onLaunchFromHyperSnap(): void
```

Called when the process is launched from HyperSnap.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityStage-onLaunchFromHyperSnap(): void--><!--Device-AbilityStage-onLaunchFromHyperSnap(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onMemoryLevel

```TypeScript
onMemoryLevel(level: AbilityConstant.MemoryLevel): void
```

Listens for changes in the system memory level status. Called when the available memory of the entire device changes to a specified level. You can implement this callback to promptly release non-essential resources (such as cached data or temporary objects) upon receiving a memory shortage event, thereby preventing the application process from being forcibly terminated by the system. This API returns the result synchronously and does not support asynchronous callbacks. > **NOTE：**> > Releasing UI components in the **onMemoryLevel** callback may block the main thread tasks of the current process. > Therefore, you are advised not to release UI components in this callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStage-onMemoryLevel(level: AbilityConstant.MemoryLevel): void--><!--Device-AbilityStage-onMemoryLevel(level: AbilityConstant.MemoryLevel): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| level | AbilityConstant.MemoryLevel | Yes |

**Examples**

```TypeScript
import { AbilityStage, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onMemoryLevel(level: AbilityConstant.MemoryLevel) {
    console.info(`MyAbilityStage.onMemoryLevel, level: ${JSON.stringify(level)}`);
  }
}
```

## onNewProcessRequest

```TypeScript
onNewProcessRequest(want: Want): string
```

Called when a UIAbility&lt;!--Del--&gt; or UIExtensionAbility&lt;!--DelEnd--&gt;, which is configured to run in an independent process (with **isolationProcess** set to **true** in the [module.json5](../../../quick-start/module-configuration-file.md) file), is launched. This API returns a string representing the unique process ID. This API returns the result synchronously and does not support asynchronous callbacks. If the application already has a process with the same ID, the UIAbility&lt;!--Del--&gt; or UIExtensionAbility&lt;!--DelEnd- -&gt; runs in that process. Otherwise, a new process is created. If you implement both **onNewProcessRequest** and [onAcceptWant](#onacceptwant), the system first invokes the **onNewProcessRequest** callback, and then the **onAcceptWant** callback. &lt;!--Del--&gt; The **isolationProcess** field can be set to **true** in the [module.json5](../../../quick-start/module-configuration-file.md) file, but only for the UIExtensionAbility of the sys/commonUI type. &lt;!--DelEnd--&gt; > **NOTE：**> > - In API version 19 and earlier, only a UIAbility can be launched in the specified process. &lt;!--Del--&gt;Starting > from API version 20, a UIExtensionAbility can also be launched in the specified process.&lt;!--DelEnd--&gt; > > - Starting from API version 20, this callback is not executed when > [AbilityStage.onNewProcessRequestAsync](#onnewprocessrequestasync) is implemented.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityStage-onNewProcessRequest(want: Want): string--><!--Device-AbilityStage-onNewProcessRequest(want: Want): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
import { AbilityStage, Want } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onNewProcessRequest(want: Want) {
    console.info('MyAbilityStage.onNewProcessRequest called');
    return 'com.example.test';
  }
}
```

## onNewProcessRequestAsync

```TypeScript
onNewProcessRequestAsync(want: Want): Promise<string>
```

Called when a UIAbility&lt;!--Del--&gt; or UIExtensionAbility&lt;!--DelEnd--&gt;, which is configured to run in an independent process (with **isolationProcess** set to **true** in the [module.json5](../../../quick-start/module-configuration-file.md) file), is launched. This API returns a string representing the unique process ID. This API uses a promise to return the result. If the application already has a process with the same ID, the UIAbility&lt;!--Del--&gt; or UIExtensionAbility&lt;!--DelEnd- -&gt; runs in that process. Otherwise, a new process is created. &lt;!--Del--&gt; The **isolationProcess** field can be set to **true** in the [module.json5](../../../quick-start/module-configuration-file.md) file, but only for the UIExtensionAbility of the sys/commonUI type. &lt;!--DelEnd--&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AbilityStage-onNewProcessRequestAsync(want: Want): Promise<string>--><!--Device-AbilityStage-onNewProcessRequestAsync(want: Want): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Examples**

```TypeScript
import { AbilityStage } from '@kit.AbilityKit';

class MyAbilityStage extends AbilityStage {
  async onNewProcessRequestAsync(): Promise<string> {
    await new Promise<string>((res, rej) => {
      setTimeout(res, 1000); // Execute the operation after 1 second.
    });
    return '';
  }
}
```

## onPrepareTermination

```TypeScript
onPrepareTermination(): AbilityConstant.PrepareTermination
```

Called when the application is closed by the user, allowing the user to choose between immediate termination or cancellation. This API returns the result synchronously and does not support asynchronous callbacks. > **NOTE：**> > - The API is called only when the application exits under normal circumstances (for example, when the application > is closed through the doc bar or tray, or when the application shuts down along with the device). It will not be > called if the application is terminated forcibly. > > - This API is not executed when > [AbilityStage.onPrepareTerminationAsync](#onprepareterminationasync) is implemented.

**Since:** 23

**Required permissions:** ohos.permission.PREPARE_APP_TERMINATE

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AbilityStage-onPrepareTermination(): AbilityConstant.PrepareTermination--><!--Device-AbilityStage-onPrepareTermination(): AbilityConstant.PrepareTermination-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| AbilityConstant.PrepareTermination |

**Examples**

```TypeScript
import { AbilityConstant, AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  onPrepareTermination(): AbilityConstant.PrepareTermination {
    console.info('MyAbilityStage.onPrepareTermination is called');
    return AbilityConstant.PrepareTermination.CANCEL;
  }
}
```

## onPrepareTerminationAsync

```TypeScript
onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination>
```

Called when the application is closed by the user, allowing the user to choose between immediate termination or cancellation. This API uses a promise to return the result. > **NOTE：**> > - The API is called only when the application exits under normal circumstances (for example, when the application > is closed through the doc bar or tray, or when the application shuts down along with the device). It will not be > called if the application is terminated forcibly. > > - If an asynchronous callback crashes, it will be handled as a timeout. If the application does not respond > within 10 seconds, it will be terminated forcibly.

**Since:** 23

**Required permissions:** ohos.permission.PREPARE_APP_TERMINATE

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AbilityStage-onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination>--><!--Device-AbilityStage-onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;AbilityConstant.PrepareTermination & gt; |

**Examples**

```TypeScript
import { AbilityConstant, AbilityStage } from '@kit.AbilityKit';

export default class MyAbilityStage extends AbilityStage {
  async onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination> {
    await new Promise<AbilityConstant.PrepareTermination>((res, rej) => {
      setTimeout(res, 3000); // Execute the operation after 3 seconds.
    });
    return AbilityConstant.PrepareTermination.CANCEL;
  }
}
```

## context

```TypeScript
context: AbilityStageContext
```

Context of an AbilityStage.

**Type:** [AbilityStageContext](arkts-ability-abilitystagecontext-c.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStage-context: AbilityStageContext--><!--Device-AbilityStage-context: AbilityStageContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
