# AgentExtensionAbility

AgentExtensionAbility继承自[ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md)，提供智能体扩展能力，包括智能体 服务的创建、销毁、连接、断开的生命周期回调接口，以及接收客户端所发送数据和安全认证的回调接口。本文将AgentExtensionAbility组件提供方称为服务端，将AgentExtensionAbility组件使用方称为客户端。

> **说明：**&gt;
> 本模块接口不支持在[har](../../../quick-start/har-package.md)包中使用。
@extends ExtensionAbility

**继承/实现关系：** AgentExtensionAbility extends ExtensionAbility

**起始版本：** 24

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

## 导入模块

```TypeScript
import { AgentExtensionAbility } from 'kits/@kit.AbilityKit';
```

## onAuth

```TypeScript
onAuth(proxy: AgentHostProxy, handshakeData: string): void
```

当AgentExtensionAbility接收到客户端发送的安全认证请求时，系统会触发该回调。服务端可以在此回调中处理接收到的安全认证请求，并通过 [AgentHostProxy.authorize](arkts-ability-agenthostproxy-i.md#authorize)向客户端发送安全认证请求。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| proxy | [AgentHostProxy](arkts-ability-agenthostproxy-i.md) | 是 |
| handshakeData | string | 是 |

## onConnect

```TypeScript
onConnect(want: Want, proxy: AgentHostProxy): void
```

当客户端连接AgentExtensionAbility成功后，系统会触发该回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| proxy | [AgentHostProxy](arkts-ability-agenthostproxy-i.md) | 是 |

## onCreate

```TypeScript
onCreate(want: Want): void
```

当AgentExtensionAbility实例创建完成时，系统会触发该回调，开发者可在该回调中执行初始化逻辑（如定义变量、加载资源等）。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

## onData

```TypeScript
onData(proxy: AgentHostProxy, data: string): void
```

当AgentExtensionAbility接收到客户端发送的数据时，系统会触发该回调。服务端可以在此回调中通过 [AgentHostProxy.sendData](arkts-ability-agenthostproxy-i.md#senddata)向客户端发送数据。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| proxy | [AgentHostProxy](arkts-ability-agenthostproxy-i.md) | 是 |
| data | string | 是 |

## onDestroy

```TypeScript
onDestroy(): void
```

当AgentExtensionAbility被销毁时，系统会触发该回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

## onDisconnect

```TypeScript
onDisconnect(want: Want, proxy: AgentHostProxy): void
```

当客户端与AgentExtensionAbility断开连接时，系统会触发该回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| proxy | [AgentHostProxy](arkts-ability-agenthostproxy-i.md) | 是 |

## context

```TypeScript
context: AgentExtensionContext
```

AgentExtensionAbility的上下文环境，继承自[ExtensionContext](arkts-ability-extensioncontext-c.md)。

**类型：** [AgentExtensionContext](arkts-ability-agentextensioncontext-c.md)

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AgentRuntime.Core
