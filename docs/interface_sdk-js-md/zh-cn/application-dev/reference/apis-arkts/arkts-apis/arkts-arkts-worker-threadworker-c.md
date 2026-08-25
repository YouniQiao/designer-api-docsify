# ThreadWorker

使用以下方法前，需先构造ThreadWorker实例。ThreadWorker类继承WorkerEventTarget。使用Worker模块时，API version 18及之后的版本建议在宿主线程中注册onAllErrors回调，以捕获Worker线程生命周期内的各种异常。API version 18之前的版本应注册onerror回调。 如果未注册onAllErrors或onerror回调，当Worker线程出现异常时会发生崩溃问题。 注意，onerror接口仅能捕获onmessage回调中的同步异常，捕获异常后，Worker线程将进入销毁流程，无法继续使用。onAllErrors接口与onerror接口之间的行为差异如下：
1. 异常捕获范围
onAllErrors接口可以捕获Worker线程的onmessage回调、timer回调以及文件执行等流程中产生的全局异常。onerror接口仅能捕获Worker线程的onmessage回调中同步方法产生的异常，无法捕获多线程回调和模块化相关异常。
2. 异常捕获后的线程状态
onAllErrors接口捕获异常后，Worker线程仍然存活并可以继续使用。这使开发者可以在捕获异常后执行其他操作，无需担心线程终止。onerror接口捕获异常后，Worker线程会进入销毁流程，无法继续使用。这意味着在onerror触发后，Worker线程将被终止，后续操作将无法进行。
3. 适用场景
onAllErrors接口适用于捕获Worker线程中所有类型异常的场景，特别是确保异常发生后Worker线程仍能继续运行的复杂场景。onerror接口适用于只需要捕获onmessage回调中同步异常的简单场景。由于捕获异常后线程会被销毁，适用于不需要继续使用Worker线程的情况。推荐使用onAllErrors接口，因为它提供了更全面的异常捕获能力，并且不会导致线程终止。

**继承/实现关系：** ThreadWorker implements [WorkerEventTarget](arkts-arkts-worker-workereventtarget-i.md)

**起始版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from 'kits/@kit.ArkTS';
```

## addEventListener

```TypeScript
addEventListener(type: string, listener: WorkerEventListener): void
```

向宿主线程的Worker实例对象添加一个事件监听，该接口与on9+接口功能一致。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| listener | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200005](../errorcode-utils.md#10200005-worker不支持某api) |

## constructor

```TypeScript
constructor(scriptURL: string, options?: WorkerOptions)
```

ThreadWorker构造函数。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scriptURL | string | 是 |
| options | [WorkerOptions](arkts-arkts-worker-workeroptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200003](../errorcode-utils.md#10200003-worker初始化失败) |
| [10200007](../errorcode-utils.md#10200007-worker文件路径异常) |

## dispatchEvent

```TypeScript
dispatchEvent(event: Event): boolean
```

分发定义在Worker线程的事件。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Event](arkts-arkts-worker-event-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |

## off

```TypeScript
off(type: string, listener?: WorkerEventListener): void
```

移除宿主线程的Worker实例对象中类型为type的事件监听，该接口与removeEventListener9+接口功能一致。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| listener | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200005](../errorcode-utils.md#10200005-worker不支持某api) |

## on

```TypeScript
on(type: string, listener: WorkerEventListener): void
```

向宿主线程的Worker实例对象添加一个事件监听，该接口与addEventListener9+接口功能一致。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| listener | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200005](../errorcode-utils.md#10200005-worker不支持某api) |

## onAllErrors

```TypeScript
onAllErrors?: ErrorCallback
```

回调函数。表示Worker线程生命周期内发生异常被调用的事件处理程序，处理程序在宿主线程中执行。默认值为undefined。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200005](../errorcode-utils.md#10200005-worker不支持某api) |

## once

```TypeScript
once(type: string, listener: WorkerEventListener): void
```

向宿主线程的Worker实例对象添加一个事件监听，该事件监听只执行一次，执行完后会自动删除。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| listener | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200005](../errorcode-utils.md#10200005-worker不支持某api) |

## onerror

```TypeScript
onerror?: (err: ErrorEvent) => void
```

回调函数，用于处理onmessage回调函数中同步代码产生的异常，处理程序在宿主线程中执行。 回调函数的err类型为ErrorEvent，表示收到的异常数据。默认值为undefined。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| err | [ErrorEvent](arkts-arkts-worker-errorevent-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200005](../errorcode-utils.md#10200005-worker不支持某api) |

## onexit

```TypeScript
onexit?: (code: number) => void
```

回调函数。表示Worker线程销毁时被调用的事件处理程序，该处理程序在宿主线程中执行。回调函数的code参数类型为number， 异常退出时code为1，正常退出时code为0。默认值为undefined。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200005](../errorcode-utils.md#10200005-worker不支持某api) |

## onmessage

```TypeScript
onmessage?: (event: MessageEvents) => void
```

回调函数。表示宿主线程接收到来自其创建的Worker通过workerPort.postMessage或workerPort.postMessageWithSharedSendable接口发送的消息时 被调用的事件处理程序，处理程序在宿主线程中执行。其中回调函数中event类型为MessageEvents， 表示收到的Worker线程发送的消息数据。默认值为undefined。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [MessageEvents](arkts-arkts-worker-messageevents-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200005](../errorcode-utils.md#10200005-worker不支持某api) |

## onmessageerror

```TypeScript
onmessageerror?: (event: MessageEvents) => void
```

回调函数。用于处理Worker对象接收到的无法被序列化的消息。该处理程序在宿主线程中执行， event类型为MessageEvents，表示收到的Worker消息数据。默认值为undefined。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [MessageEvents](arkts-arkts-worker-messageevents-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200005](../errorcode-utils.md#10200005-worker不支持某api) |

## postMessage

```TypeScript
postMessage(message: Object, transfer: ArrayBuffer[]): void
```

宿主线程通过转移对象所有权的方式向Worker线程发送消息。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | Object | 是 |
| [transfer](arkts-arkts-worker-postmessageoptions-i.md) | ArrayBuffer[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |

## postMessage

```TypeScript
postMessage(message: Object, options?: PostMessageOptions): void
```

宿主线程可以通过转移对象所有权或拷贝数据的方式向Worker线程发送消息。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | Object | 是 |
| options | [PostMessageOptions](arkts-arkts-worker-postmessageoptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |

## postMessageWithSharedSendable

```TypeScript
postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void
```

宿主线程向Worker线程发送消息，消息中的Sendable对象通过引用传递， 非Sendable对象通过拷贝数据的方式传递。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | Object | 是 |
| [transfer](arkts-arkts-worker-postmessageoptions-i.md) | ArrayBuffer[] | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |

## registerGlobalCallObject

```TypeScript
registerGlobalCallObject(instanceName: string, globalCallObject: Object): void
```

在宿主线程的ThreadWorker实例上注册一个对象，该对象的方法可在Worker线程中通过 callGlobalCallObjectMethod调用。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [instanceName](../../apis-ability-kit/arkts-apis/arkts-ability-errormanager-globalerror-i.md) | string | 是 |
| globalCallObject | Object | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |

## removeAllListener

```TypeScript
removeAllListener(): void
```

移除宿主线程中Worker实例对象的所有事件监听。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |

## removeEventListener

```TypeScript
removeEventListener(type: string, callback?: WorkerEventListener): void
```

移除宿主线程的Worker实例对象中类型为type的事件监听，该接口与off9+接口功能一致。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| callback | [WorkerEventListener](arkts-arkts-worker-workereventlistener-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |

## terminate

```TypeScript
terminate(): void
```

由宿主线程主动销毁Worker线程并停止Worker线程接收消息。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |

## unregisterGlobalCallObject

```TypeScript
unregisterGlobalCallObject(instanceName?: string): void
```

取消在宿主线程ThreadWorker实例上注册的对象，该方法会释放ThreadWorker实例与目标对象之间的强引用。 如果无匹配对象，该方法不会报错。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [instanceName](../../apis-ability-kit/arkts-apis/arkts-ability-errormanager-globalerror-i.md) | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
