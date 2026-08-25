# Promise

表示异步操作的最终完成或失败。

**继承/实现关系：** Promise implements PromiseLike<T>

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## all

```TypeScript
static all<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Array<Awaited<U>>>
```

等待FixedArray中所有Promise都解析。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| promises | FixedArray & lt;PromiseLike & lt;U & gt; \ | U \| undefined & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;Awaited & lt;U & gt; & gt; & gt; |

## all

```TypeScript
static all<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Array<Awaited<U>>>
```

等待可迭代对象中所有Promise都解析。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| promises | Iterable & lt;PromiseLike & lt;U & gt; \ | U & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;Awaited & lt;U & gt; & gt; & gt; |

## allSettled

```TypeScript
static allSettled<U>(promises: FixedArray<PromiseLike<U> | U | undefined>):
        Promise<PromiseSettledResult<Awaited<U>>[]>
```

等待FixedArray中所有Promise都完成。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| promises | FixedArray & lt;PromiseLike & lt;U & gt; \ | U \| undefined & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PromiseSettledResult](arkts-arkts-promisesettledresult-t.md)&lt;Awaited&lt;U&gt;&gt;[]&gt; |

## allSettled

```TypeScript
static allSettled<U>(promises: Iterable<PromiseLike<U> | U>): Promise<PromiseSettledResult<Awaited<U>>[]>
```

等待可迭代对象中所有Promise都完成。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| promises | Iterable & lt;PromiseLike & lt;U & gt; \ | U & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PromiseSettledResult](arkts-arkts-promisesettledresult-t.md)&lt;Awaited&lt;U&gt;&gt;[]&gt; |

## any

```TypeScript
static any<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>
```

等待FixedArray中任意一个Promise解析。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| promises | FixedArray & lt;PromiseLike & lt;U & gt; \ | U \| undefined & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## any

```TypeScript
static any<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>
```

等待可迭代对象中任意一个Promise解析。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| promises | Iterable & lt;PromiseLike & lt;U & gt; \ | U & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## catch

```TypeScript
catch<U = never>(onRejected: () => PromiseLike<U> | U): Promise<Awaited<T | U>>
```

为Promise的拒绝添加回调函数（无参形式）。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| onRejected | () = & gt; PromiseLike & lt;U & gt; \ | U | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Awaited & lt;T \ | U & gt; & gt; | 用于返回Awaited & lt;T \ |

## catch

```TypeScript
catch<U = never>(onRejected?: (error: Error) => PromiseLike<U> | U): Promise<Awaited<T | U>>
```

为Promise的拒绝添加回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| onRejected | (error: Error) = & gt; PromiseLike & lt;U & gt; \ | U | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Awaited & lt;T \ | U & gt; & gt; | 用于返回Awaited & lt;T \ |

## constructor

```TypeScript
constructor(callback: (resolve: (value: PromiseLike<T> | T) => void,
        reject: (error: Error) => void) => void)
```

使用指定的回调函数构造新的Promise。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (resolve: (value: PromiseLike & lt;T & gt; \ | T) = & gt; void,         reject: (error: Error) = & gt; void) = & gt; void | 是 |

## finally

```TypeScript
finally<U = T>(onFinally?: () => PromiseLike<U> | U): Promise<Awaited<T>>
```

添加在Promise完成（无论解析还是拒绝）时调用的回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| onFinally | () = & gt; PromiseLike & lt;U & gt; \ | U | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Awaited & lt;T & gt; & gt; |

## race

```TypeScript
static race<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>
```

等待FixedArray中第一个Promise完成。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| promises | FixedArray & lt;PromiseLike & lt;U & gt; \ | U \| undefined & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## race

```TypeScript
static race<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>
```

等待可迭代对象中第一个Promise完成。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| promises | Iterable & lt;PromiseLike & lt;U & gt; \ | U & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## reject

```TypeScript
static reject(): Promise<void>
```

创建一个已拒绝的空Promise。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## reject

```TypeScript
static reject<U = never>(error: Error): Promise<Awaited<U>>
```

使用指定Error创建已拒绝的Promise。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| error | Error | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## resolve

```TypeScript
static resolve(): Promise<void>
```

创建一个已解析的空Promise。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## resolve

```TypeScript
static resolve<U>(value: PromiseLike<U> | U): Promise<Awaited<U>>
```

使用指定值创建已解析的Promise。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | PromiseLike & lt;U & gt; \ | U | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## then

```TypeScript
then<U = T>(onFulfilled: () => PromiseLike<U> | U): Promise<Awaited<U>>
```

为Promise的解析添加回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| onFulfilled | () = & gt; PromiseLike & lt;U & gt; \ | U | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Awaited & lt;U & gt; & gt; |

## then

```TypeScript
then(_onFulfilled?: undefined): Promise<Awaited<T>>
```

不为Promise的解析添加回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| _onFulfilled | undefined | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Awaited & lt;T & gt; & gt; |

## then

```TypeScript
then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,
        onRejected?: (error: Error) => PromiseLike<E> | E): Promise<Awaited<U | E>>
```

为Promise的解析和/或拒绝添加回调函数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| onFulfilled | (value: T) = & gt; PromiseLike & lt;U & gt; \ | U | 是 |
| onRejected | (error: Error) = & gt; PromiseLike & lt;E & gt; \ | E | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Awaited & lt;U \ | E & gt; & gt; | 用于返回Awaited & lt;U \ |
