# DriverExtensionAbility

DriverExtensionAbility模块提供驱动相关扩展能力，提供驱动创建、销毁、连接、断开等生命周期回调。

**起始版本：** 10

**系统能力：** SystemCapability.Driver.ExternalDevice

## 导入模块

```TypeScript
import { DriverExtensionAbility, DriverExtensionContext } from 'kits/@kit.DriverDevelopmentKit';
```

## onConnect

```TypeScript
onConnect(want: Want): rpc.RemoteObject | Promise<rpc.RemoteObject>
```

Extension生命周期回调，会在[onCreate](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-abilitystage-abilitystage-c.md#oncreate)之后回调。返回一个 [RemoteObject](../../apis-ipc-kit/arkts-apis/arkts-ipc-rpc-remoteobject-c.md)对象，用于客户端和服务端进行通信。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| rpc.RemoteObject \| Promise & lt;rpc.RemoteObject & gt; |

## onDisconnect

```TypeScript
onDisconnect(want: Want): void | Promise<void>
```

Extension的生命周期回调，客户端执行断开连接服务时回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

## onDump

```TypeScript
onDump(params: Array<string>): Array<string>
```

转储客户端信息时调用，建议不要转储敏感信息。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

## onInit

```TypeScript
onInit(want: Want): void
```

Extension生命周期回调，在创建时回调，执行初始化业务逻辑操作。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

## onRelease

```TypeScript
onRelease(): void
```

Extension生命周期回调，在销毁时回调，执行资源清理等操作。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Driver.ExternalDevice

## context

```TypeScript
context: DriverExtensionContext
```

DriverExtension的上下文环境，继承自ExtensionContext。

**类型：** [DriverExtensionContext](arkts-driverdevelopment-driverextensioncontext-t.md)

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Driver.ExternalDevice
