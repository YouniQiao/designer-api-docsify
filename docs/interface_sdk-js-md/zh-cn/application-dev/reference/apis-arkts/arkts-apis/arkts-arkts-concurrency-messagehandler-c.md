# MessageHandler

处理消息并提供消息调度能力。不同消息可由不同的MessageHandler处理。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(handler: (message: concurrency.Message) => void, worker: EAWorker | undefined = EAWorker.current())
```

构造一个MessageHandler实例，需要传入消息处理函数，可选传入EAWorker实例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | (message: concurrency.Message) = & gt; void | 是 |
| worker | [EAWorker](arkts-arkts-eaworker-c.md) \| undefined | 是 |

## getWorker

```TypeScript
getWorker(): EAWorker
```

返回与该处理器关联的Worker。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [EAWorker](arkts-arkts-eaworker-c.md) |

## hasCallbacks

```TypeScript
hasCallbacks(callback: () => void): boolean
```

检查处理器中是否有指定的回调函数在等待执行。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | () = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## hasMessages

```TypeScript
hasMessages(what: int): boolean
```

检查处理器中是否有指定标识符的消息。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| what | int | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## hasMessages

```TypeScript
hasMessages(what: int, obj: Any): boolean
```

检查处理器中是否有指定标识符和数据对象的消息。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| what | int | 是 |
| obj | Any | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## post

```TypeScript
post(callback: () => void): boolean
```

构造消息并添加到消息队列中执行。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | () = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## removeCallbacks

```TypeScript
removeCallbacks(callback: () => void): boolean
```

从消息队列中移除匹配指定回调函数的待执行回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | () = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## removeMessages

```TypeScript
removeMessages(what: int): boolean
```

从消息队列中移除指定标识符的待执行消息。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| what | int | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## removeMessages

```TypeScript
removeMessages(what: int, obj: Any): boolean
```

从消息队列中移除指定标识符和数据对象的待执行消息。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| what | int | 是 |
| obj | Any | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## sendEmptyMessage

```TypeScript
sendEmptyMessage(what: int): boolean
```

发送指定标识符的空消息。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| what | int | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## sendMessage

```TypeScript
sendMessage(message: concurrency.Message): boolean
```

将消息添加到消息队列。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | concurrency.Message | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
