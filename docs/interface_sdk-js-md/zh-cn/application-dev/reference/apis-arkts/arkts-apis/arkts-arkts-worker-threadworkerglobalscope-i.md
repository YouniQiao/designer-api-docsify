# ThreadWorkerGlobalScope

Worker线程用于与宿主线程通信的类。其中postMessage接口用于向宿主线程发送消息，close接口用于销毁Worker线程。 ThreadWorkerGlobalScope类继承GlobalScope9+。

**继承/实现关系：** ThreadWorkerGlobalScope extends [GlobalScope](arkts-arkts-worker-globalscope-i.md)

**起始版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { worker, DedicatedWorkerGlobalScope, ErrorEvent, Event, EventListener, EventTarget, MessageEvent, MessageEvents, PostMessageOptions, ThreadWorkerGlobalScope, WorkerEventListener, WorkerEventTarget, WorkerOptions, ThreadWorkerPriority, Priority } from 'kits/@kit.ArkTS';
```

## callGlobalCallObjectMethod

```TypeScript
callGlobalCallObjectMethod(instanceName: string, methodName: string, timeout: number, ...args: Object[]): Object
```

Worker线程调用宿主线程上注册的对象的指定方法，此调用对Worker线程同步，对宿主线程异步， 返回值通过数据拷贝传递。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [instanceName](../../apis-ability-kit/arkts-apis/arkts-ability-errormanager-globalerror-i.md) | string | 是 |
| methodName | string | 是 |
| timeout | number | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | 是 |

**返回值：**

| 类型 |
| --- |
| Object |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |
| [10200019](../errorcode-utils.md#10200019-调用未注册对象的方法错误) |
| [10200020](../errorcode-utils.md#10200020-调用注册对象上的方法类型错误) |
| [10200021](../errorcode-utils.md#10200021-全局调用等待超时错误) |

## close

```TypeScript
close(): void
```

销毁Worker线程，终止Worker接收消息。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |

## onmessage

```TypeScript
onmessage?: (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void
```

回调函数。表示Worker线程收到来自其宿主线程通过postMessage或postMessageWithSharedSendable接口发送的消息时被调用的事件处理程序，处理程序在Worker线程中执行。 其中this指调用者对象本身ThreadWorkerGlobalScope，ev类型为MessageEvents，表示收到的宿主线程发送的消息数据。默认值为undefined。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| this | [ThreadWorkerGlobalScope](arkts-arkts-worker-threadworkerglobalscope-i.md) | 是 |
| ev | [MessageEvents](arkts-arkts-worker-messageevents-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200005](../errorcode-utils.md#10200005-worker不支持某api) |

## onmessageerror

```TypeScript
onmessageerror?: (this: ThreadWorkerGlobalScope, ev: MessageEvents) => void
```

回调函数。表示当Worker线程的Worker对象接收到一条无法被反序列化的消息时被调用的事件处理程序，处理程序在Worker线程中执行。其中this指调用者对象本身ThreadWorkerGlobalScope， ev类型为MessageEvents，表示收到的消息数据。默认值为undefined。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| this | [ThreadWorkerGlobalScope](arkts-arkts-worker-threadworkerglobalscope-i.md) | 是 |
| ev | [MessageEvents](arkts-arkts-worker-messageevents-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200005](../errorcode-utils.md#10200005-worker不支持某api) |

## postMessage

```TypeScript
postMessage(messageObject: Object, transfer: ArrayBuffer[]): void
```

Worker线程通过转移对象所有权的方式向宿主线程发送消息。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| messageObject | Object | 是 |
| [transfer](arkts-arkts-worker-postmessageoptions-i.md) | ArrayBuffer[] | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |

## postMessage

```TypeScript
postMessage(messageObject: Object, options?: PostMessageOptions): void
```

Worker线程通过转移对象所有权或拷贝数据的方式向宿主线程发送消息。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| messageObject | Object | 是 |
| options | [PostMessageOptions](arkts-arkts-worker-postmessageoptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |

## postMessageAtFront

```TypeScript
postMessageAtFront?(message: Object, priority: Priority, transfer?: ArrayBuffer[]): void
```

Worker线程通过转移对象所有权的方式向宿主线程发送插队消息，并插入到对应优先级队列的队头。 除Worker线程向主线程发送的场景外，该接口与postMessage功能一致。

> **说明：**&gt;
> - 如果是Worker线程向宿主线程发送插队的消息，消息能够插队并且按优先级进行发送。&gt;
> - 如果是Worker线程之间发送插队的消息，消息只能插队，没有优先级。&gt;
> - postMessage和postMessageWithSharedSendable接口向宿主线程发送消息，默认是HIGH优先级，无插队效果。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | Object | 是 |
| priority | [Priority](arkts-arkts-worker-priority-e.md) | 是 |
| [transfer](arkts-arkts-worker-postmessageoptions-i.md) | ArrayBuffer[] | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200004](../errorcode-utils.md#10200004-worker处于非运行状态) |
| [10200006](../errorcode-utils.md#10200006-worker传输信息序列化异常) |

## postMessageWithSharedSendable

```TypeScript
postMessageWithSharedSendable(message: Object, transfer?: ArrayBuffer[]): void
```

Worker线程向宿主线程发送消息，消息中的Sendable对象通过引用传递， 非Sendable对象通过拷贝数据的方式传递。

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
