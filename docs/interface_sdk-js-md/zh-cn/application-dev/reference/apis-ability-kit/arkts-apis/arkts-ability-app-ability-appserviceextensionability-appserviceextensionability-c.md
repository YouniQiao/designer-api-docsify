# AppServiceExtensionAbility

AppServiceExtensionAbility模块提供后台服务相关扩展能力，包括后台服务的创建、销毁、连接、断开等生命周期回调。

**继承/实现关系：** AppServiceExtensionAbility extends ExtensionAbility

**起始版本：** 20

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { AppServiceExtensionAbility } from 'kits/@kit.AbilityKit';
```

## onConnect

```TypeScript
onConnect(want: Want): rpc.RemoteObject
```

调用方使用 [connectAppServiceExtensionAbility()](arkts-ability-uiabilitycontext-c.md#connectappserviceextensionability) 连接AppServiceExtensionAbility实例时，系统会触发该回调。应用需要在该接口中返回一个RemoteObject对象，用于客户端和服务端进行通信。当AppServiceExtensionAbility实例处于连接状态时，如果调用方发起新的连接，系统会返回缓存的RemoteObject对象， 而不会重复回调onConnect()接口。  
**设备行为差异**：该接口仅在PC/2in1设备中可正常执行回调，在其他设备上不执行回调。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| rpc.RemoteObject |

## onCreate

```TypeScript
onCreate(want: Want): void
```

在AppServiceExtensionAbility实例创建时，系统会触发该回调。应用可以在该接口中执行自己的业务逻辑初始化操作，例如注册公共事件监听等。

> **说明：**&gt;
> 如果AppServiceExtensionAbility实例已创建，再次启动或连接该实例时不会触发onCreate()回调。
**设备行为差异**：该接口仅在PC/2in1设备中可正常执行回调，在其他设备上不执行回调。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

## onDestroy

```TypeScript
onDestroy(): void
```

在AppServiceExtensionAbility实例销毁时，系统会触发该回调。应用可以在该接口中执行资源清理等操作，如注销监听等。  
**设备行为差异**：该接口仅在PC/2in1设备中可正常执行回调，在其他设备上不执行回调。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onDisconnect

```TypeScript
onDisconnect(want: Want): void
```

当所有连接方断开与AppServiceExtensionAbility实例的连接时，系统会触发该回调。  
**设备行为差异**：该接口仅在PC/2in1设备中可正常执行回调，在其他设备上不执行回调。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

## onRequest

```TypeScript
onRequest(want: Want, startId: number): void
```

调用方每次使用 [startAppServiceExtensionAbility()](arkts-ability-uiabilitycontext-c.md#startappserviceextensionability) 拉起AppServiceExtensionAbility实例时，系统都会触发该回调。  
**设备行为差异**：该接口仅在PC/2in1设备中可正常执行回调，在其他设备上不执行回调。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| startId | number | 是 |

## context

```TypeScript
context: AppServiceExtensionContext
```

AppServiceExtensionAbility的上下文环境，继承自[ExtensionContext](arkts-ability-extensioncontext-c.md)。

**类型：** [AppServiceExtensionContext](../../apis-default/arkts-apis/arkts-appserviceextensioncontext-c.md)

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
