# DistributedExtensionContext

用于分布式扩展功能的实现。

**继承/实现关系：** DistributedExtensionContext extends ExtensionContext

**起始版本：** 20

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

## 导入模块

```TypeScript
import { DistributedExtensionContext } from 'kits/@kit.DistributedServiceKit';
```

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

将当前DistributedExtensionAbility连接到远端（其他设备上的）ServiceExtensionAbility，建立连接后 通过onConnect回调返回的[rpc.IRemoteObject](../../apis-ipc-kit/arkts-apis/arkts-ipc-rpc-iremoteobject-c.md)代理与远端 ServiceExtensionAbility进行跨设备IPC通信，以使用其对外提供的能力。适用于多设备限定协同场景， 例如在当前设备上调用其他设备的后台服务能力。使用时，开发者首先通过Want中的deviceId指定目标设备、 bundleName和abilityName指定目标ServiceExtensionAbility，并构造 [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-connectoptions-connectoptions-i.md)实现onConnect、 onDisconnect、onFailed三个回调分别处理连接成功、连接断开和连接失败状态；随后调用 connectServiceExtensionAbility发起连接并获取返回的连接ID，连接成功后在onConnect回调中拿到 IRemoteObject代理对象，基于该代理与远端ServiceExtensionAbility进行IPC通信； 使用完毕后需调用[disconnectServiceExtensionAbility](#disconnectserviceextensionability) 断开连接并释放资源。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-connectoptions-connectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000053](../../apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

断开与远端ServiceExtensionAbility的连接，与[connectServiceExtensionAbility](#connectserviceextensionability) 配对使用。调用connectServiceExtensionAbility后，必须在使用完毕后调用此方法释放连接资源， 需要使用connectServiceExtensionAbility返回的连接ID调用此方法。断开连接之后开发者需要将连接成功时 onConnect回调中返回的remote对象置空，以避免后续误用已失效的代理对象。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [connection](../../apis-network-kit/arkts-apis/arkts-net-connection.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000003](../../apis-ability-kit/errorcode-ability.md#16000003-指定的id不存在) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
