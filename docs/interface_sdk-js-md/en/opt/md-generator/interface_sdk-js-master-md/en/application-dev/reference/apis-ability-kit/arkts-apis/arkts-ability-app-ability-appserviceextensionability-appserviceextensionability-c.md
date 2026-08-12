# AppServiceExtensionAbility

The AppServiceExtensionAbility module provides extended capabilities for background services, including lifecycle callbacks for creating, destroying, connecting, and disconnecting background services.

**Inheritance/Implementation:** AppServiceExtensionAbility extends [ExtensionAbility](ExtensionAbility)

**Since:** 20

<!--Device-unnamed-declare class AppServiceExtensionAbility extends ExtensionAbility--><!--Device-unnamed-declare class AppServiceExtensionAbility extends ExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { AppServiceExtensionAbility } from '@kit.AbilityKit';
```

## onConnect

```TypeScript
onConnect(want: Want): rpc.RemoteObject
```

Called when an AppServiceExtensionAbility instance is connected by calling  
[connectAppServiceExtensionAbility()](arkts-ability-uiabilitycontext-c.md#connectAppServiceExtensionAbility).

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppServiceExtensionAbility-onConnect(want: Want): rpc.RemoteObject--><!--Device-AppServiceExtensionAbility-onConnect(want: Want): rpc.RemoteObject-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| rpc.RemoteObject |

## Examples

```TypeScript
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtAbility]';

class StubTest extends rpc.RemoteObject {
  constructor(des: string) {
    super(des);
  }

  onConnect(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption) {
  }
}

export default class AppServiceExtAbility extends AppServiceExtensionAbility {
  onConnect(want: Want) {
    hilog.info(0x0000, TAG, `onConnect, want: ${want.abilityName}`);
    return new StubTest('test');
  }
}
```

## onCreate

```TypeScript
onCreate(want: Want): void
```

Called when an AppServiceExtensionAbility instance is created.Applications can perform initialization operations, such as registering common event listeners, in this callback.

> **NOTE：**
> 
> If an AppServiceExtensionAbility instance has already been created, the **onCreate()** callback is not invoked
> again when the instance is started or connected.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppServiceExtensionAbility-onCreate(want: Want): void--><!--Device-AppServiceExtensionAbility-onCreate(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

## Examples

```TypeScript
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtAbility]';

export default class AppServiceExtAbility extends AppServiceExtensionAbility {
  onCreate(want: Want) {
    hilog.info(0x0000, TAG, `onCreate, want: ${want.abilityName}`);
  }
}
```

## onDestroy

```TypeScript
onDestroy(): void
```

Called when an AppServiceExtensionAbility instance is destroyed. Applications can perform resource cleanup operations, such as unregistering listeners, in this callback.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppServiceExtensionAbility-onDestroy(): void--><!--Device-AppServiceExtensionAbility-onDestroy(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Examples

```TypeScript
import { AppServiceExtensionAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtAbility]';

export default class AppServiceExtAbility extends AppServiceExtensionAbility {
  onDestroy() {
    hilog.info(0x0000, TAG, `onDestroy`);
  }
}
```

## onDisconnect

```TypeScript
onDisconnect(want: Want): void
```

Called when all connections to an AppServiceExtensionAbility instance are interrupted.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppServiceExtensionAbility-onDisconnect(want: Want): void--><!--Device-AppServiceExtensionAbility-onDisconnect(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

## Examples

```TypeScript
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtAbility]';

export default class AppServiceExtAbility extends AppServiceExtensionAbility {
  onDisconnect(want: Want) {
    hilog.info(0x0000, TAG, `onDisconnect, want: ${want.abilityName}`);
  }
}
```

## onRequest

```TypeScript
onRequest(want: Want, startId: number): void
```

Called each time an AppServiceExtensionAbility instance is started by calling  
[startAppServiceExtensionAbility()](arkts-ability-uiabilitycontext-c.md#startAppServiceExtensionAbility).

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppServiceExtensionAbility-onRequest(want: Want, startId: int): void--><!--Device-AppServiceExtensionAbility-onRequest(want: Want, startId: int): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| startId | number | Yes |

## Examples

```TypeScript
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtAbility]';

export default class AppServiceExtAbility extends AppServiceExtensionAbility {
  onRequest(want: Want, startId: number) {
    hilog.info(0x0000, TAG, `onRequest, want: ${want.abilityName}, startId: ${startId}`);
  }
}
```

## context

```TypeScript
context: AppServiceExtensionContext
```

Context environment for an AppServiceExtensionAbility. This context inherits from  
[ExtensionContext](arkts-ability-extensioncontext-c.md#ExtensionContext).

**Type:** [AppServiceExtensionContext](arkts-ability-appserviceextensioncontext-c.md)

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppServiceExtensionAbility-context: AppServiceExtensionContext--><!--Device-AppServiceExtensionAbility-context: AppServiceExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
