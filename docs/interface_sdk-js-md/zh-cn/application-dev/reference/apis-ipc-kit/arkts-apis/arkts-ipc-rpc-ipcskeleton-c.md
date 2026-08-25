# IPCSkeleton

用于获取IPC上下文信息，包括获取UID和PID、获取本端和对端设备ID、检查接口调用是否在同一设备上。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

## 导入模块

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## flushCmdBuffer

```TypeScript
static flushCmdBuffer(object: IRemoteObject): void
```

静态方法，将所有挂起的命令从指定的RemoteProxy刷新到相应的RemoteObject。建议在任何时间执行敏感操作之前调用此方法。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| object | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## flushCommands

```TypeScript
static flushCommands(object: IRemoteObject): number
```

静态方法，将所有挂起的命令从指定的RemoteProxy刷新到相应的RemoteObject。建议在任何时间执行敏感操作之前调用此方法。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** static

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| object | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getCallingDeviceID

```TypeScript
static getCallingDeviceID(): string
```

静态方法，获取调用者进程所在的设备ID。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

## getCallingPid

```TypeScript
static getCallingPid(): number
```

静态方法，获取调用者的PID。此方法由[RemoteObject](arkts-ipc-rpc-remoteobject-c.md)对象在IPC上下文环境（ [onRemoteMessageRequest](arkts-ipc-rpc-remoteobject-c.md#onremotemessagerequest)）中调用，不在则返回本进程的PID。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getCallingTokenId

```TypeScript
static getCallingTokenId(): number
```

静态方法，获取调用者的TokenId，用于被调用方对调用方的身份校验。

**起始版本：** 8

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getCallingUid

```TypeScript
static getCallingUid(): number
```

静态方法，获取调用者的UID。此方法由[RemoteObject](arkts-ipc-rpc-remoteobject-c.md)对象在IPC上下文环境（ [onRemoteMessageRequest](arkts-ipc-rpc-remoteobject-c.md#onremotemessagerequest)）中调用，不在则返回本进程的UID。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getContextObject

```TypeScript
static getContextObject(): IRemoteObject
```

静态方法，获取系统服务管理器（SAMGR）对象。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) |

## getLocalDeviceID

```TypeScript
static getLocalDeviceID(): string
```

静态方法，获取本端设备ID。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

## isLocalCalling

```TypeScript
static isLocalCalling(): boolean
```

静态方法，检查当前通信对端是否是本设备的进程。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## resetCallingIdentity

```TypeScript
static resetCallingIdentity(): string
```

静态方法，将远程用户的UID和PID替换为本地用户的UID和PID。它可以用于身份验证等场景。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| string |

## restoreCallingIdentity

```TypeScript
static restoreCallingIdentity(identity: string): void
```

静态方法，将UID和PID恢复为远程用户的UID和PID。它通常在使用resetCallingIdentity后调用，需要resetCallingIdentity返回的远程用户的UID和PID。该接口仅支持在IPC上下文（ [onRemoteMessageRequest](arkts-ipc-rpc-remoteobject-c.md#onremotemessagerequest)）中使用，否则直接返回。

**起始版本：** 9

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| identity | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setCallingIdentity

```TypeScript
static setCallingIdentity(identity: string): boolean
```

静态方法，将UID和PID恢复为远程用户的UID和PID。它通常在使用resetCallingIdentity后调用，需要resetCallingIdentity返回的远程用户的UID和PID。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** static

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| identity | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
