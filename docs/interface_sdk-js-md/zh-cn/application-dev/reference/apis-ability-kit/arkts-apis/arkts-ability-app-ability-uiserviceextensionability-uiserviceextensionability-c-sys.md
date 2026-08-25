# UIServiceExtensionAbility（系统接口）

UIServiceExtensionAbility提供浮窗组件相关扩展能力，继承自[ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md). 主要用于向三方应用提供带界面的服务。

**继承/实现关系：** UIServiceExtensionAbility extends ExtensionAbility

**起始版本：** 14

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { UIServiceExtensionAbility } from 'kits/@kit.AbilityKit';
```

## onConnect

```TypeScript
onConnect(want: Want, proxy: UIServiceHostProxy): void
```

UIServiceExtension生命周期回调。如果是 [connectUIServiceExtensionAbility()](arkts-ability-uiextensioncontext-c.md#connectuiserviceextensionability) 拉起的服务，会在[onCreate()](#oncreate)之后回调。接收一个 [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md)对象，用于客户端和服务端进行通信。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | 是 |

## onCreate

```TypeScript
onCreate(want: Want): void
```

[UIServiceExtensionContext](../../apis-default/arkts-apis/arkts-uiserviceextensioncontext-c-sys.md)生命周期创建接口，执行初始化 业务逻辑操作。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

## onData

```TypeScript
onData(proxy: UIServiceHostProxy, data: Record<string, Object>): void
```

接收到数据的回调。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | 是 |
| data | Record & lt;string, Object & gt; | 是 |

## onDestroy

```TypeScript
onDestroy(): void
```

UIServiceExtension销毁时回调，执行资源清理等操作。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

## onDisconnect

```TypeScript
onDisconnect(want: Want, proxy: UIServiceHostProxy): void
```

断开与UIServiceExtension的连接。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| proxy | [UIServiceHostProxy](arkts-ability-uiservicehostproxy-i-sys.md) | 是 |

## onRequest

```TypeScript
onRequest(want: Want, startId: number): void
```

请求拉起UIServiceExtension服务处理。如果是 [startAbility](arkts-ability-uiabilitycontext-c.md#startability) 或者 [startUIServiceExtensionAbility](arkts-ability-uiabilitycontext-c.md#startuiserviceextensionability) 拉起的服务，会在[onCreate](#oncreate)之后回调。每次拉起服务都会回调，startId会递增。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| startId | number | 是 |

## onWindowDidCreate

```TypeScript
onWindowDidCreate(window: window.Window): void
```

UIServiceExtension创建后回调。UIServiceExtension服务创建窗口成功后，通过onWindowDidCreate接口把创建的窗口对象传递给前台应用。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [window](../../apis-arkui/arkts-apis/arkts-arkui-window-n.md) | window.Window | 是 |

## onWindowWillCreate

```TypeScript
onWindowWillCreate(config: window.ExtensionWindowConfig): void
```

UIServiceExtension窗体创建前的回调。前台应用把要创建windows的参数通过window.ExtensionWindowConfig传回给UIServiceExtension服务。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | window.ExtensionWindowConfig | 是 |

## context

```TypeScript
context: UIServiceExtensionContext
```

UIServiceExtension的上下文环境，继承自[ExtensionContext](arkts-ability-app-ability-extensionability-extensionability-c.md)。

**类型：** [UIServiceExtensionContext](../../apis-default/arkts-apis/arkts-uiserviceextensioncontext-c-sys.md)

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。
