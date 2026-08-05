# UIServiceExtensionAbility (System API)

UIServiceExtensionAbility provides extended capabilities related to the floating window component. It inherits from [ExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. It is mainly used to provide services with UIs for third-party applications. > **NOTE** > > The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

**Inheritance/Implementation:** UIServiceExtensionAbility extends [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class UIServiceExtensionAbility extends ExtensionAbility--><!--Device-unnamed-declare class UIServiceExtensionAbility extends ExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## onConnect

```TypeScript
onConnect(want: Want, proxy: UIServiceHostProxy): void
```

Called when the connection to a [UIServiceExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is established. If the UIServiceExtensionAbility is started by calling [connectUIServiceExtensionAbility()]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ , this callback will be invoked after [onCreate()]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_. This callback receives a [UIServiceHostProxy]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ object for communication between the client and server.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onConnect(want: Want, proxy: UIServiceHostProxy): void--><!--Device-UIServiceExtensionAbility-onConnect(want: Want, proxy: UIServiceHostProxy): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | [Want]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ information about the [UIServiceExtensionAbility]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, including the ability name and bundle name. |
| proxy | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | [UIServiceHostProxy]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_object, used for communication between the client and server. |

**Example**

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

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onCreate(want: Want): void--><!--Device-UIServiceExtensionAbility-onCreate(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | [Want]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ information about the [UIServiceExtensionAbility]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, including the ability name and bundle name. |

**Example**

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

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, Object>): void--><!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, Object>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| proxy | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Proxy that sends data to the client. |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, Object&gt; | Yes | Data received. |

**Example**

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, RecordData>): void--><!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, RecordData>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| proxy | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the UI service host proxy. |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, RecordData&gt; | Yes | Indicates the received data. |

## onDestroy

```TypeScript
onDestroy(): void
```

Called to clear resources when this [UIServiceExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is destroyed.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onDestroy(): void--><!--Device-UIServiceExtensionAbility-onDestroy(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Example**

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

Called when the connection to a [UIServiceExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is interrupted.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onDisconnect(want: Want, proxy: UIServiceHostProxy): void--><!--Device-UIServiceExtensionAbility-onDisconnect(want: Want, proxy: UIServiceHostProxy): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | [Want]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ information about the [UIServiceExtensionAbility]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, including the ability name and bundle name. |
| proxy | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Proxy that sends data to the sender. |

**Example**

```TypeScript
import { UIServiceExtensionAbility, Want, common } from '@kit.AbilityKit';

class UIServiceExt extends UIServiceExtensionAbility {
  onDisconnect(want: Want, proxy: common.UIServiceHostProxy) {
    console.info('onDisconnect, want: ${want.abilityName}');
  }
}
```

## onRequest

ArkTS-Dyn:
```TypeScript
onRequest(want: Want, startId: number): void
```

ArkTS-Sta:
```TypeScript
onRequest(want: Want, startId: int): void
```

Called to request to start a [UIServiceExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. If the UIServiceExtensionAbility is started by calling [startAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ or [startUIServiceExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ , this callback will be invoked after [onCreate]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_. The value of **startId** is incremented for each UIServiceExtensionAbility that is started.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onRequest(want: Want, startId: int): void--><!--Device-UIServiceExtensionAbility-onRequest(want: Want, startId: int): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | [Want]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ information about the [UIServiceExtensionAbility]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, including the ability name and bundle name. |
| startId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Number of times the instance has been started. The initial value is **1** for the first start,and it increments automatically for subsequent starts. |

**Example**

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

Called when a window is created for the [UIServiceExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. Through this callback, the [UIServiceExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ passes the created window object to the foreground application.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onWindowDidCreate(window: window.Window): void--><!--Device-UIServiceExtensionAbility-onWindowDidCreate(window: window.Window): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| window | window.Window | Yes | Window object created. |

**Example**

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

Called when a window will be created for the [UIServiceExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. Through **window.ExtensionWindowConfig** in the callback, the foreground application sends the parameters for creating the window to the [UIServiceExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onWindowWillCreate(config: window.ExtensionWindowConfig): void--><!--Device-UIServiceExtensionAbility-onWindowWillCreate(config: window.ExtensionWindowConfig): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | window.ExtensionWindowConfig | Yes | Window configuration information. |

**Example**

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

Context environment for a [UIServiceExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. This context inherits from [ExtensionContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Type:** UIServiceExtensionContext

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-context: UIServiceExtensionContext--><!--Device-UIServiceExtensionAbility-context: UIServiceExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

