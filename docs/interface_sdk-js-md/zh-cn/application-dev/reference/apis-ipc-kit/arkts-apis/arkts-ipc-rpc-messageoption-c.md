# MessageOption

公共消息选项，使用指定的标志类型，构造指定的MessageOption对象。

**起始版本：** 7

**系统能力：** SystemCapability.Communication.IPC.Core

## 导入模块

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## constructor

```TypeScript
constructor(syncFlags?: number, waitTime?: number)
```

MessageOption构造函数。

**起始版本：** 7

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| syncFlags | number | 否 |
| waitTime | number | 否 |

## constructor

```TypeScript
constructor(async?: boolean)
```

MessageOption构造函数。

**起始版本：** 9

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| async | boolean | 否 |

## getFlags

```TypeScript
getFlags(): number
```

获取同步调用或异步调用标志。

**起始版本：** 7

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## getWaitTime

```TypeScript
getWaitTime(): number
```

获取rpc调用的最长等待时间。

**起始版本：** 7

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| number |

## isAsync

```TypeScript
isAsync(): boolean
```

获取 [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)调用中确定同步或是异步的标志。

**起始版本：** 9

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## setAsync

```TypeScript
setAsync(isAsync: boolean): void
```

设置 [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)调用中确定同步或是异步的标志。

**起始版本：** 9

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [isAsync](arkts-ipc-rpc-messageoption-c.md) | boolean | 是 |

## setFlags

```TypeScript
setFlags(flags: number): void
```

设置同步调用或异步调用标志。

**起始版本：** 7

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flags | number | 是 |

## setWaitTime

```TypeScript
setWaitTime(waitTime: number): void
```

设置rpc调用最长等待时间。

**起始版本：** 7

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| waitTime | number | 是 |

## TF_ACCEPT_FDS

```TypeScript
static readonly TF_ACCEPT_FDS: number
```

指示 [sendMessageRequest](arkts-ipc-rpc-iremoteobject-c.md#sendmessagerequest)接口可以传递文件描述符。

**类型：** number

**默认值：** 16

**起始版本：** 7

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

## TF_ASYNC

```TypeScript
static readonly TF_ASYNC: number
```

异步调用标识。

**类型：** number

**默认值：** 1

**起始版本：** 7

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

## TF_SYNC

```TypeScript
static readonly TF_SYNC: number
```

同步调用标识。

**类型：** number

**默认值：** 0

**起始版本：** 7

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core

## TF_WAIT_TIME

```TypeScript
static readonly TF_WAIT_TIME: number
```

RPC等待时间（单位：秒），IPC场景下无效。默认等待为8秒（不建议修改等待时间）。

**类型：** number

**默认值：** 4 [since 7 - 10] @default 8 [since 11]

**起始版本：** 7

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.IPC.Core
