# AbilityStage

AbilityStage是一个[Module](../../../quick-start/application-package-overview.md#应用的多module设计机制)级别的组件管理器，用于进行Module级别的资源预加载、线程创建等初始化操作，以及维护Module下的应用状态。AbilityStage与Module一一对应，即一个Module拥有一个AbilityStage。

应用的[HAP](../../../quick-start/hap-package.md)/[HSP](../../../quick-start/in-app-hsp.md)在首次加载时会创建一个AbilityStage实例。当一个Module中存在AbilityStage和其他组件（UIAbility/ExtensionAbility组件），AbilityStage实例会早于其他组件实例创建。

AbilityStage拥有[onCreate()](arkts-ability-app-ability-abilitystage-abilitystage-c.md#oncreate)、[onDestroy()](arkts-ability-app-ability-abilitystage-abilitystage-c.md#ondestroy)生命周期回调和  
[onAcceptWant()](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onacceptwant)、[onConfigurationUpdate()](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onconfigurationupdate)、[onMemoryLevel()](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onmemorylevel)事件回调等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class AbilityStage--><!--Device-unnamed-declare class AbilityStage-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { AbilityStage } from 'kits/@kit.AbilityKit';
```

## onAboutToCreateAbility

```TypeScript
onAboutToCreateAbility(): void
```

无

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityStage-onAboutToCreateAbility(): void--><!--Device-AbilityStage-onAboutToCreateAbility(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onAcceptWant

```TypeScript
onAcceptWant(want: Want): string
```

当启动模式配置为[specified](../../../application-models/uiability-launch-type.md#specified启动模式)的UIAbility被拉起时，会触发该回调，并返回一个string作为待启动的UIAbility实例的唯一标识。同步接口，不支持异步回调。

如果系统中已经有相同标识的UIAbility实例存在，则复用已有实例，否则创建新的实例。

> **说明：**
> 
> 从API version 20开始，当[AbilityStage.onAcceptWantAsync](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onacceptwantasync)实现时，本回调函数将不会被触发。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStage-onAcceptWant(want: Want): string--><!--Device-AbilityStage-onAcceptWant(want: Want): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | Want类型参数，此处表示调用方传入的启动参数，如Ability名称，Bundle名称等。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回开发者自定义的UIAbility标识。如果已经启动了相同标识的UIAbility，则复用该UIAbility，否则创建新的实例并启动。 |

## Examples

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

当启动模式配置为[specified](../../../application-models/uiability-launch-type.md#specified启动模式)的UIAbility被拉起时，会触发该回调，并返回一个string作为待启动的UIAbility实例的唯一标识。使用Promise异步回调。

如果系统中已经有相同标识的UIAbility实例存在，则复用已有实例，否则创建新的实例。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AbilityStage-onAcceptWantAsync(want: Want): Promise<string>--><!--Device-AbilityStage-onAcceptWantAsync(want: Want): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | Want类型参数，传入需要启动的UIAbility的信息，如UIAbility名称、Bundle名称等。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回一个string作为待启动的UIAbility实例的唯一标识。如果系统中已经有该标识的UIAbility实例存在，则复用已有实例，否则创建新的实例。 |

## Examples

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

当系统全局配置（例如系统语言、深浅色等）发生变更时，会触发该回调。配置项均定义在[Configuration](arkts-ability-app-ability-configuration-configuration-i.md)类中。同步接口，不支持异步回调。

> **说明：**
> 
> 该回调方法在实际触发时存在一定限制。例如如果开发者通过[setLanguage](arkts-ability-applicationcontext-c.md#setlanguage)接口
> 设置应用的语言，即便系统语言发生变化，系统也不再触发onConfigurationUpdate回调。详见
> [使用场景](../../../application-models/subscribe-system-environment-variable-changes.md#使用场景)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStage-onConfigurationUpdate(newConfig: Configuration): void--><!--Device-AbilityStage-onConfigurationUpdate(newConfig: Configuration): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newConfig | [Configuration](arkts-ability-app-ability-configuration-configuration-i.md) | Yes | 发生全局配置变更时触发回调，当前全局配置包括系统语言、深浅色模式。 |

## Examples

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

在加载Module的第一个Ability实例前，系统会先创建对应的AbilityStage实例，并在AbilityStage创建完成后，自动触发该回调。

开发者可以在该回调中执行Module的初始化操作（如资源预加载、线程创建等）。同步接口，不支持异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStage-onCreate(): void--><!--Device-AbilityStage-onCreate(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Examples

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

在对应Module的最后一个Ability实例退出后会触发该回调。此方法将在正常的调度生命周期中调用，当应用程序异常退出或被终止时，将不会调用此方法。同步接口，不支持异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityStage-onDestroy(): void--><!--Device-AbilityStage-onDestroy(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Examples

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

进程从镜像启动时调用

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityStage-onLaunchFromHyperSnap(): void--><!--Device-AbilityStage-onLaunchFromHyperSnap(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onMemoryLevel

```TypeScript
onMemoryLevel(level: AbilityConstant.MemoryLevel): void
```

该接口用于监听系统内存状态变化。当整机可用内存变化到指定程度时，系统会触发该回调。开发者可通过实现此接口，在收到内存紧张事件时，及时释放非必要资源（如缓存数据、临时对象等），以避免应用进程被系统强制终止。

同步接口，不支持异步回调。

> **说明：**
> 
> onMemoryLevel回调运行在当前进程的主线程中，如果在该回调中做耗时的UI组件释放，会阻塞主线程任务，因此不建议在该回调中释放UI组件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStage-onMemoryLevel(level: AbilityConstant.MemoryLevel): void--><!--Device-AbilityStage-onMemoryLevel(level: AbilityConstant.MemoryLevel): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | AbilityConstant.MemoryLevel | Yes | 整机可用内存级别，对应的触发场景详见 [AbilityConstant.MemoryLevel](arkts-ability-abilityconstant-memorylevel-e.md)。 |

## Examples

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

如果UIAbility&lt;!--Del--&gt;或UIExtensionAbility&lt;!--DelEnd--&gt;配置了在独立进程中运行（即  
[module.json5配置文件](../../../quick-start/module-configuration-file.md)中UIAbility&lt;!--Del--&gt;或UIExtensionAbility&lt;!--DelEnd--&gt;的isolationProcess字段取值为true），当该UIAbility&lt;!--Del--&gt;或UIExtensionAbility&lt;!--DelEnd--&gt;被拉起时，会触发该回调，并返回一个string作为进程唯一标识。同步接口，不支持异步回调。

如果该应用已有相同标识的进程存在，则待启动的UIAbility&lt;!--Del--&gt;或UIExtensionAbility&lt;!--DelEnd--&gt;运行在此进程中，否则创建新的进程。

如果开发者同时实现onNewProcessRequest和[onAcceptWant](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onacceptwant)，将先收到onNewProcessRequest回调，再收到onAcceptWant回调。

&lt;!--Del--&gt;

仅支持sys/commonUI类型的UIExtensionAbility组件在[module.json5配置文件](../../../quick-start/module-configuration-file.md)配置文件中配置isolationProcess字段为true。

&lt;!--DelEnd--&gt;

> **说明：**
> 
> - 在API version 19及之前版本，仅支持在指定进程中启动UIAbility。&lt;!--Del--&gt;从API version 20开始，新增支持在指定进程中启动UIExtensionAbility。&lt;!--DelEnd
&gt; -->
> 
> - 从API version 20开始，当[AbilityStage.onNewProcessRequestAsync](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onnewprocessrequestasync)实现时，本回调函
> 数将不执行。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityStage-onNewProcessRequest(want: Want): string--><!--Device-AbilityStage-onNewProcessRequest(want: Want): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | Want类型参数，此处表示调用方传入的启动参数，如UIAbility&lt;!--Del--&gt;或UIExtensionAbility&lt;!--DelEnd--&gt;名称、Bundle名称等。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回一个由开发者自行决定的进程字符串标识，如果之前此标识对应的进程已被创建，就让ability在此进程中运行，否则创建新的进程。 |

## Examples

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

如果UIAbility&lt;!--Del--&gt;或UIExtensionAbility&lt;!--DelEnd--&gt;配置了在独立进程中运行（即  
[module.json5配置文件](../../../quick-start/module-configuration-file.md)中UIAbility&lt;!--Del--&gt;或UIExtensionAbility&lt;!--DelEnd--&gt;的isolationProcess字段取值为true），当该UIAbility&lt;!--Del--&gt;或UIExtensionAbility&lt;!--DelEnd--&gt;被拉起时，会触发该回调，并返回一个string作为进程唯一标识。使用Promise异步回调。

如果该应用已有相同标识的进程存在，则待启动的UIAbility&lt;!--Del--&gt;或UIExtensionAbility&lt;!--DelEnd--&gt;运行在此进程中，否则创建新的进程。

&lt;!--Del--&gt;

仅支持sys/commonUI类型的UIExtensionAbility组件在[module.json5配置文件](../../../quick-start/module-configuration-file.md)中配置isolationProcess字段为true。

&lt;!--DelEnd--&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AbilityStage-onNewProcessRequestAsync(want: Want): Promise<string>--><!--Device-AbilityStage-onNewProcessRequestAsync(want: Want): Promise<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | Want类型参数，此处表示调用方传入的启动参数，如UIAbility&lt;!--Del--&gt;或UIExtensionAbility&lt;!--DelEnd--&gt;名称、Bundle名称等。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise对象，返回一个由开发者自定义的进程字符串标识。如果该应用已有相同标识的进程存在，则UIAbility&lt;!--Del--&gt;或UIExtensionAbility &lt;!--DelEnd--&gt;在此进程中运行，否则创建新的进程。 |

## Examples

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

当应用被用户关闭时调用，可用于询问用户选择立即执行操作还是取消操作。同步接口，不支持异步回调。

> **说明：**
> 
> - 仅当应用正常退出（例如，通过doc栏/托盘关闭应用，或者应用随设备关机而退出）时会调用该接口。如果应用被强制关闭，则不会调用该接口。
> 
> - 当[AbilityStage.onPrepareTerminationAsync](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onprepareterminationasync)实现时，本回调函数将不执行。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PREPARE_APP_TERMINATE

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-AbilityStage-onPrepareTermination(): AbilityConstant.PrepareTermination--><!--Device-AbilityStage-onPrepareTermination(): AbilityConstant.PrepareTermination-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| AbilityConstant.PrepareTermination | The user's choice. |

## Examples

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

当应用被用户关闭时调用，可用于询问用户选择立即执行操作还是取消操作。使用Promise异步回调。

> **说明：**
> 
> - 仅当应用正常退出（例如，通过doc栏/托盘关闭应用，或者应用随设备关机而退出）时会调用该接口。如果应用被强制关闭，则不会调用该接口。
> 
> - 若异步回调内发生crash，按超时处理，执行等待超过10秒未响应，应用将被强制关闭。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PREPARE_APP_TERMINATE

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-AbilityStage-onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination>--><!--Device-AbilityStage-onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AbilityConstant.PrepareTermination&gt; | Promise used to return the user's choice. |

## Examples

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

AbilityStage上下文。

**Type:** [AbilityStageContext](arkts-ability-abilitystagecontext-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityStage-context: AbilityStageContext--><!--Device-AbilityStage-context: AbilityStageContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

