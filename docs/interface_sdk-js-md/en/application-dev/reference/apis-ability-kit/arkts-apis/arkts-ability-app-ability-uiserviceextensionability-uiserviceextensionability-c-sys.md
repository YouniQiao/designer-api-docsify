# UIServiceExtensionAbility (System API)

UIServiceExtensionAbility提供浮窗组件相关扩展能力，继承自[ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md).主要用于向三方应用提供带界面的服务。

**Inheritance/Implementation:** UIServiceExtensionAbility extends [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class UIServiceExtensionAbility extends ExtensionAbility--><!--Device-unnamed-declare class UIServiceExtensionAbility extends ExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { UIServiceExtensionAbility } from 'kits/@kit.AbilityKit';
```

## onConnect

```TypeScript
onConnect(want: Want, proxy: UIServiceHostProxy): void
```

UIServiceExtension生命周期回调。如果是  
[connectUIServiceExtensionAbility()](arkts-ability-uiextensioncontext-c.md#connectuiserviceextensionability)拉起的服务，会在[onCreate()](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md#oncreate)之后回调。接收一个  
[UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md)对象，用于客户端和服务端进行通信。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onConnect(want: Want, proxy: UIServiceHostProxy): void--><!--Device-UIServiceExtensionAbility-onConnect(want: Want, proxy: UIServiceHostProxy): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 当前 [UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md)相关的 [Want](arkts-ability-app-ability-want-want-c.md)类型信息，包括Ability名称、Bundle名称等。 |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | Yes | 一个[UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) 对象，用于客户端和服务端进行通信。 |

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

[UIServiceExtensionContext](../../apis-default/arkts-apis/arkts-uiserviceextensioncontext-c-sys.md/arkts-uiserviceextensioncontext-c-sys.md)生命周期创建接口，执行初始化业务逻辑操作。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onCreate(want: Want): void--><!--Device-UIServiceExtensionAbility-onCreate(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 当前 [UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md)相关的 [Want](arkts-ability-app-ability-want-want-c.md)类型信息，包括Ability名称、Bundle名称等。 |

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

接收到数据的回调。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, Object>): void--><!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, Object>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | Yes | 往客户端发送数据的Proxy。 |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Yes | 表示接收到的数据。 |

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

接收到数据的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, RecordData>): void--><!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, RecordData>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | Yes | 往客户端发送数据的Proxy。 |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, RecordData&gt; | Yes | 表示接收到的数据。 |

## onDestroy

```TypeScript
onDestroy(): void
```

UIServiceExtension销毁时回调，执行资源清理等操作。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

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

断开与UIServiceExtension的连接。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onDisconnect(want: Want, proxy: UIServiceHostProxy): void--><!--Device-UIServiceExtensionAbility-onDisconnect(want: Want, proxy: UIServiceHostProxy): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 当前 [UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md)相关的 [Want](arkts-ability-app-ability-want-want-c.md)类型信息，包括Ability名称、Bundle名称等。 |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | Yes | 往发起方发送数据的Proxy。 |

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

ArkTS-Dyn:
```TypeScript
onRequest(want: Want, startId: number): void
```

ArkTS-Sta:
```TypeScript
onRequest(want: Want, startId: int): void
```

请求拉起UIServiceExtension服务处理。如果是  
[startAbility](arkts-ability-uiabilitycontext-c.md#startability)或者  
[startUIServiceExtensionAbility](arkts-ability-uiabilitycontext-c.md#startuiserviceextensionability)拉起的服务，会在[onCreate](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md#oncreate)之后回调。每次拉起服务都会回调，startId会递增。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onRequest(want: Want, startId: int): void--><!--Device-UIServiceExtensionAbility-onRequest(want: Want, startId: int): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 当前 [UIServiceExtensionAbility](arkts-ability-app-ability-uiserviceextensionability-uiserviceextensionability-c-sys.md)相关的 [Want](arkts-ability-app-ability-want-want-c.md)类型信息，包括Ability名称、Bundle名称等。 |
| startId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 返回浮窗拉起次数。首次拉起初始值返回1，多次之后自动递增。 |

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

UIServiceExtension创建后回调。UIServiceExtension服务创建窗口成功后，通过onWindowDidCreate接口把创建的窗口对象传递给前台应用。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onWindowDidCreate(window: window.Window): void--><!--Device-UIServiceExtensionAbility-onWindowDidCreate(window: window.Window): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| window | window.Window | Yes | 表示已创建的Window。 |

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

UIServiceExtension窗体创建前的回调。前台应用把要创建windows的参数通过window.ExtensionWindowConfig传回给UIServiceExtension服务。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-onWindowWillCreate(config: window.ExtensionWindowConfig): void--><!--Device-UIServiceExtensionAbility-onWindowWillCreate(config: window.ExtensionWindowConfig): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | window.ExtensionWindowConfig | Yes | UIServiceExtension窗体配置信息。 |

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

UIServiceExtension的上下文环境，继承自[ExtensionContext](arkts-ability-app-ability-extensionability-extensionability-c.md)。

**Type:** [UIServiceExtensionContext](../../apis-default/arkts-apis/arkts-uiserviceextensioncontext-c-sys.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIServiceExtensionAbility-context: UIServiceExtensionContext--><!--Device-UIServiceExtensionAbility-context: UIServiceExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

