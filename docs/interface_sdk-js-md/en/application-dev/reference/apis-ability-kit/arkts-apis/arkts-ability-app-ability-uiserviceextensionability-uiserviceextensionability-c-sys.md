# UIServiceExtensionAbility (System API)

UIServiceExtensionAbility provides extended capabilities related to the floating window component. It inherits from [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md#ExtensionAbility). It is mainly used to provide services with UIs for third-party applications. > **NOTE：**> > The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

**Inheritance/Implementation:** UIServiceExtensionAbility extends ExtensionAbility

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare class UIServiceExtensionAbility--><!--Device-unnamed-declare class UIServiceExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { UIServiceExtensionAbility } from '@kit.AbilityKit';
```

## onConnect

```TypeScript
onConnect(want: Want, proxy: UIServiceHostProxy): void
```

Called when the connection to a [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)) is established. If the UIServiceExtensionAbility is started by calling [connectUIServiceExtensionAbility()](arkts-ability-uiextensioncontext-c.md#connectUIServiceExtensionAbility) , this callback will be invoked after [onCreate()](#onCreate). This callback receives a [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md#UIServiceHostProxy-(System-API)) object for communication between the client and server.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onConnect(want: Want, proxy: UIServiceHostProxy): void--><!--Device-UIServiceExtensionAbility-onConnect(want: Want, proxy: UIServiceHostProxy): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | [Want](arkts-ability-app-ability-want-want-c.md#Want) information about the [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)), including the ability name and bundle name. |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | Yes | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md#UIServiceHostProxy-(System-API)) object, used for communication between the client and server. |

## Examples

```TypeScript
import { UIServiceExtensionAbility, Want, common} from '@kit.AbilityKit';

class UIServiceExt extends UIServiceExtensionAbility {
  onConnect(want: Want, proxy: common.UIServiceHostProxy){
    console.info('onConnect, want:' + want.abilityName + '');
  }
}
```

## onCreate

```TypeScript
onCreate(want: Want): void
```

Called to initialize the service logic.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onCreate(want: Want): void--><!--Device-UIServiceExtensionAbility-onCreate(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | [Want](arkts-ability-app-ability-want-want-c.md#Want) information about the [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)), including the ability name and bundle name. |

## Examples

```TypeScript
import { UIServiceExtensionAbility, Want } from '@kit.AbilityKit';

class UIServiceExt extends UIServiceExtensionAbility {
  // Create a UIServiceExtensionAbility.
  onCreate(want: Want) {
    console.info(`onCreate, want: ${want.abilityName}`);
  }
}
```

## onData

```TypeScript
onData(proxy: UIServiceHostProxy, data: Record<string, Object>): void
```

Callback invoked when data is received.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, Object>): void--><!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, Object>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | Yes | Proxy that sends data to the client. |
| data | Record&lt;string, Object&gt; | Yes | Data received. |

## Examples

```TypeScript
import { UIServiceExtensionAbility, common} from '@kit.AbilityKit';

class ServiceExt extends UIServiceExtensionAbility {
  onData(proxy : common.UIServiceHostProxy, data : Record<string, Object> ){
    console.info('onData');
  }
}
```

## onData

```TypeScript
onData(proxy: UIServiceHostProxy, data: Record<string, RecordData>): void
```

Called back when data is sent.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, RecordData>): void--><!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, RecordData>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | Yes | Indicates the UI service host proxy. |
| data | Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes | Indicates the received data. |

## onDestroy

```TypeScript
onDestroy(): void
```

Called to clear resources when this [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)) is destroyed.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onDestroy(): void--><!--Device-UIServiceExtensionAbility-onDestroy(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Examples

```TypeScript
import { UIServiceExtensionAbility } from '@kit.AbilityKit';

class ServiceExt extends UIServiceExtensionAbility {
  onDestroy() {
    console.info('onDestroy');
  }
}
```

## onDisconnect

```TypeScript
onDisconnect(want: Want, proxy: UIServiceHostProxy): void
```

Called when the connection to a [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)) is interrupted.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onDisconnect(want: Want, proxy: UIServiceHostProxy): void--><!--Device-UIServiceExtensionAbility-onDisconnect(want: Want, proxy: UIServiceHostProxy): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | [Want](arkts-ability-app-ability-want-want-c.md#Want) information about the [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)), including the ability name and bundle name. |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | Yes | Proxy that sends data to the sender. |

## Examples

```TypeScript
import { UIServiceExtensionAbility, Want, common } from '@kit.AbilityKit';

class UIServiceExt extends UIServiceExtensionAbility {
  onDisconnect(want: Want, proxy: common.UIServiceHostProxy) {
    console.info('onDisconnect, want: ${want.abilityName}');
  }
}
```

## onRequest

```TypeScript
onRequest(want: Want, startId: int): void
```

Called to request to start a [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)). If the UIServiceExtensionAbility is started by calling [startAbility](arkts-ability-uiabilitycontext-c.md#startAbility) or [startUIServiceExtensionAbility](arkts-ability-uiabilitycontext-c.md#startUIServiceExtensionAbility) , this callback will be invoked after [onCreate](#onCreate). The value of **startId** is incremented for each UIServiceExtensionAbility that is started.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onRequest(want: Want, startId: int): void--><!--Device-UIServiceExtensionAbility-onRequest(want: Want, startId: int): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | [Want](arkts-ability-app-ability-want-want-c.md#Want) information about the [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)), including the ability name and bundle name. |
| startId | int | Yes | Number of times the instance has been started. The initial value is **1** for the first start, and it increments automatically for subsequent starts. |

## Examples

```TypeScript
import { UIServiceExtensionAbility, Want} from '@kit.AbilityKit';

class UIServiceExt extends UIServiceExtensionAbility {
  onRequest(want: Want, startId: number) {
    console.info('onRequest, want:' + want.abilityName + ', startId:' + startId);
  }
}
```

## onWindowDidCreate

```TypeScript
onWindowDidCreate(window: window.Window): void
```

Called when a window is created for the [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)). Through this callback, the [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)) passes the created window object to the foreground application.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onWindowDidCreate(window: window.Window): void--><!--Device-UIServiceExtensionAbility-onWindowDidCreate(window: window.Window): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| window | window.Window | Yes | Window object created. |

## Examples

```TypeScript
import { UIServiceExtensionAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class ServiceExt extends UIServiceExtensionAbility {
  onWindowDidCreate(window : window.Window){
    console.info('onWindowDidCreate');
  }
}
```

## onWindowWillCreate

```TypeScript
onWindowWillCreate(config: window.ExtensionWindowConfig): void
```

Called when a window will be created for the [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)). Through **window.ExtensionWindowConfig** in the callback, the foreground application sends the parameters for creating the window to the [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onWindowWillCreate(config: window.ExtensionWindowConfig): void--><!--Device-UIServiceExtensionAbility-onWindowWillCreate(config: window.ExtensionWindowConfig): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | window.ExtensionWindowConfig | Yes | Window configuration information. |

## Examples

```TypeScript
import { UIServiceExtensionAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class UIServiceExt extends UIServiceExtensionAbility {
  onWindowWillCreate(config : window.ExtensionWindowConfig){
    console.info('onWindowWillCreate');
  }
}
```

## context

```TypeScript
context: UIServiceExtensionContext
```

Context environment for a [UIServiceExtensionAbility](#UIServiceExtensionAbility-(System-API)). This context inherits from [ExtensionContext](arkts-ability-extensioncontext-c.md#ExtensionContext).

**Type:** [UIServiceExtensionContext](arkts-ability-uiserviceextensioncontext-c-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-context: UIServiceExtensionContext--><!--Device-UIServiceExtensionAbility-context: UIServiceExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

