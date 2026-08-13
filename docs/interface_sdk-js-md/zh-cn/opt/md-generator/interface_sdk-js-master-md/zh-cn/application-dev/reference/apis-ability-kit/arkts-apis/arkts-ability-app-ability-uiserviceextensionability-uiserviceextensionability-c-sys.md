# UIServiceExtensionAbility（系统接口）

UIServiceExtensionAbility提供浮窗组件相关扩展能力，继承自[ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md#ExtensionAbility). 主要用于向三方应用提供带界面的服务。

**继承/实现关系：** UIServiceExtensionAbility extends ExtensionAbility

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare class UIServiceExtensionAbility--><!--Device-unnamed-declare class UIServiceExtensionAbility-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

## onConnect

```TypeScript
onConnect(want: Want, proxy: UIServiceHostProxy): void
```

UIServiceExtension生命周期回调。如果是 [connectUIServiceExtensionAbility()](arkts-ability-uiextensioncontext-c.md#connectUIServiceExtensionAbility) 拉起的服务，会在[onCreate()](#onCreate)之后回调。接收一个 [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md#UIServiceHostProxy（系统接口）)对象，用于客户端和服务端进行通信。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIServiceExtensionAbility-onConnect(want: Want, proxy: UIServiceHostProxy): void--><!--Device-UIServiceExtensionAbility-onConnect(want: Want, proxy: UIServiceHostProxy): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| [proxy](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-config-i.md) | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | 是 |

## 示例

```TypeScript
import { UIServiceExtensionAbility, Want, common} from '@kit.AbilityKit';

class UIServiceExt extends UIServiceExtensionAbility {
  onConnect(want: Want, proxy: common.UIServiceHostProxy){
    console.info(`onConnect, want: ${want.abilityName}`);
  }
}
```

## onCreate

```TypeScript
onCreate(want: Want): void
```

[UIServiceExtensionContext](../../apis-na/arkts-apis/arkts-na-uiserviceextensioncontext-c-sys.md#UIServiceExtensionContext（系统接口）)生命周期创建接口，执行初始化 业务逻辑操作。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIServiceExtensionAbility-onCreate(want: Want): void--><!--Device-UIServiceExtensionAbility-onCreate(want: Want): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

## 示例

```TypeScript
import { UIServiceExtensionAbility, Want } from '@kit.AbilityKit';

class UIServiceExt extends UIServiceExtensionAbility {
  // 创建UIServiceExtensionAbility
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

**起始版本：** 14

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, Object>): void--><!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, Object>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [proxy](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-config-i.md) | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | 是 |
| data | Record & lt;string, Object & gt; | 是 |

## 示例

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

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, RecordData>): void--><!--Device-UIServiceExtensionAbility-onData(proxy: UIServiceHostProxy, data: Record<string, RecordData>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [proxy](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-config-i.md) | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | 是 |
| data | Record&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt; | 是 |

## onDestroy

```TypeScript
onDestroy(): void
```

UIServiceExtension销毁时回调，执行资源清理等操作。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIServiceExtensionAbility-onDestroy(): void--><!--Device-UIServiceExtensionAbility-onDestroy(): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

## 示例

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

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIServiceExtensionAbility-onDisconnect(want: Want, proxy: UIServiceHostProxy): void--><!--Device-UIServiceExtensionAbility-onDisconnect(want: Want, proxy: UIServiceHostProxy): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| [proxy](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-config-i.md) | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | 是 |

## 示例

```TypeScript
import { UIServiceExtensionAbility, Want, common } from '@kit.AbilityKit';

class UIServiceExt extends UIServiceExtensionAbility {
  onDisconnect(want: Want, proxy: common.UIServiceHostProxy) {
    console.info(`onDisconnect, want: ${want.abilityName}`);
  }
}
```

## onRequest

```TypeScript
onRequest(want: Want, startId: number): void
```

请求拉起UIServiceExtension服务处理。如果是 [startAbility](arkts-ability-uiabilitycontext-c.md#startAbility) 或者 [startUIServiceExtensionAbility](arkts-ability-uiabilitycontext-c.md#startUIServiceExtensionAbility) 拉起的服务，会在[onCreate](#onCreate)之后回调。每次拉起服务都会回调，startId会递增。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIServiceExtensionAbility-onRequest(want: Want, startId: int): void--><!--Device-UIServiceExtensionAbility-onRequest(want: Want, startId: int): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| startId | number | 是 |

## 示例

```TypeScript
import { UIServiceExtensionAbility, Want} from '@kit.AbilityKit';

class UIServiceExt extends UIServiceExtensionAbility {
  onRequest(want: Want, startId: number) {
    console.info(`onRequest, want: ${want.abilityName}, startId: ${startId}`);
  }
}
```

## onWindowDidCreate

```TypeScript
onWindowDidCreate(window: window.Window): void
```

UIServiceExtension创建后回调。UIServiceExtension服务创建窗口成功后，通过onWindowDidCreate接口把创建的窗口对象传递给前台应用。

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIServiceExtensionAbility-onWindowDidCreate(window: window.Window): void--><!--Device-UIServiceExtensionAbility-onWindowDidCreate(window: window.Window): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [window](../../apis-arkui/arkts-apis/arkts-arkui-window-n.md) | window.Window | 是 |

## 示例

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

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIServiceExtensionAbility-onWindowWillCreate(config: window.ExtensionWindowConfig): void--><!--Device-UIServiceExtensionAbility-onWindowWillCreate(config: window.ExtensionWindowConfig): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | window.ExtensionWindowConfig | 是 |

## 示例

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

UIServiceExtension的上下文环境，继承自[ExtensionContext](arkts-ability-app-ability-extensionability-extensionability-c.md#ExtensionAbility)。

**类型：** [UIServiceExtensionContext](../../apis-na/arkts-apis/arkts-na-uiserviceextensioncontext-c-sys.md)

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIServiceExtensionAbility-context: UIServiceExtensionContext--><!--Device-UIServiceExtensionAbility-context: UIServiceExtensionContext-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。
