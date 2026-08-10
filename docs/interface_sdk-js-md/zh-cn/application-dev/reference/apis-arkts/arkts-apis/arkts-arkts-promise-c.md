# Promise

Represents the eventual completion or failure of an asynchronous operation.

**继承/实现关系：** Promise implements [PromiseLike<T>](PromiseLike<T>)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class Promise<out T> implements PromiseLike<T>--><!--Device-unnamed-export class Promise<out T> implements PromiseLike<T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## all

```TypeScript
static all<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Array<Awaited<U>>>
```

Waits for all promises to resolve from a FixedArray.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-static all<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Array<Awaited<U>>>--><!--Device-Promise-static all<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Array<Awaited<U>>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| promises | FixedArray&lt;PromiseLike&lt;U&gt; \| U \| undefined&gt; | 是 | The promises to wait for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;Awaited&lt;U&gt;&gt;&gt; | Promise used to return Array&lt;Awaited<U>&gt;&lt;U&gt;>. |

## all

```TypeScript
static all<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Array<Awaited<U>>>
```

Waits for all promises to resolve from an Iterable.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-static all<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Array<Awaited<U>>>--><!--Device-Promise-static all<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Array<Awaited<U>>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| promises | Iterable&lt;PromiseLike&lt;U&gt; \| U&gt; | 是 | The promises to wait for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;Awaited&lt;U&gt;&gt;&gt; | Promise used to return Array&lt;Awaited<U>&gt;&lt;U&gt;>. |

## allSettled

```TypeScript
static allSettled<U>(promises: FixedArray<PromiseLike<U> | U | undefined>):
        Promise<PromiseSettledResult<Awaited<U>>[]>
```

Waits for all promises to settle from a FixedArray.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-static allSettled<U>(promises: FixedArray<PromiseLike<U> | U | undefined>):        Promise<PromiseSettledResult<Awaited<U>>[]>--><!--Device-Promise-static allSettled<U>(promises: FixedArray<PromiseLike<U> | U | undefined>):        Promise<PromiseSettledResult<Awaited<U>>[]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| promises | FixedArray&lt;PromiseLike&lt;U&gt; \| U \| undefined&gt; | 是 | The promises to wait for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;PromiseSettledResult&lt;Awaited&lt;U&gt;&gt;[]&gt; | Promise used to return PromiseSettledResult&lt;Awaited<U>&gt;&lt;U&gt;>[]. |

## allSettled

```TypeScript
static allSettled<U>(promises: Iterable<PromiseLike<U> | U>): Promise<PromiseSettledResult<Awaited<U>>[]>
```

Waits for all promises to settle from an Iterable.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-static allSettled<U>(promises: Iterable<PromiseLike<U> | U>): Promise<PromiseSettledResult<Awaited<U>>[]>--><!--Device-Promise-static allSettled<U>(promises: Iterable<PromiseLike<U> | U>): Promise<PromiseSettledResult<Awaited<U>>[]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| promises | Iterable&lt;PromiseLike&lt;U&gt; \| U&gt; | 是 | The promises to wait for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;PromiseSettledResult&lt;Awaited&lt;U&gt;&gt;[]&gt; | Promise used to return PromiseSettledResult&lt;Awaited<U>&gt;&lt;U&gt;>[]. |

## any

```TypeScript
static any<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>
```

Waits for any promise to resolve from a FixedArray.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-static any<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>--><!--Device-Promise-static any<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| promises | FixedArray&lt;PromiseLike&lt;U&gt; \| U \| undefined&gt; | 是 | The promises to wait for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## any

```TypeScript
static any<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>
```

Waits for any promise to resolve from an Iterable.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-static any<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>--><!--Device-Promise-static any<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| promises | Iterable&lt;PromiseLike&lt;U&gt; \| U&gt; | 是 | The promises to wait for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## catch

```TypeScript
catch<U = never>(onRejected: () => PromiseLike<U> | U): Promise<Awaited<T | U>>
```

Attaches a callback for the rejection of the Promise with no error parameter.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-catch<U = never>(onRejected: () => PromiseLike<U> | U): Promise<Awaited<T | U>>--><!--Device-Promise-catch<U = never>(onRejected: () => PromiseLike<U> | U): Promise<Awaited<T | U>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onRejected | () =&gt; PromiseLike&lt;U&gt; \| U | 是 | The callback to execute when the Promise is rejected. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;T \| U&gt;&gt; | Promise used to return Awaited&lt;T \| U&gt;. |

## catch

```TypeScript
catch<U = never>(onRejected?: (error: Error) => PromiseLike<U> | U): Promise<Awaited<T | U>>
```

Attaches a callback for the rejection of the Promise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-catch<U = never>(onRejected?: (error: Error) => PromiseLike<U> | U): Promise<Awaited<T | U>>--><!--Device-Promise-catch<U = never>(onRejected?: (error: Error) => PromiseLike<U> | U): Promise<Awaited<T | U>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onRejected | (error: Error) =&gt; PromiseLike&lt;U&gt; \| U | 否 | The callback to execute when the Promise is rejected. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;T \| U&gt;&gt; | Promise used to return Awaited&lt;T \| U&gt;. |

## constructor

```TypeScript
constructor(callback: (resolve: (value: PromiseLike<T> | T) => void,
        reject: (error: Error) => void) => void)
```

Constructs a new Promise with the given callback.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-constructor(callback: (resolve: (value: PromiseLike<T> | T) => void,        reject: (error: Error) => void) => void)--><!--Device-Promise-constructor(callback: (resolve: (value: PromiseLike<T> | T) => void,        reject: (error: Error) => void) => void)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (resolve: (value: PromiseLike&lt;T&gt; \| T) =&gt; void,         reject: (error: Error) =&gt; void) =&gt; void | 是 | The callback to execute. |

## finally

```TypeScript
finally<U = T>(onFinally?: () => PromiseLike<U> | U): Promise<Awaited<T>>
```

Attaches a callback that is invoked when the Promise is settled.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-finally<U = T>(onFinally?: () => PromiseLike<U> | U): Promise<Awaited<T>>--><!--Device-Promise-finally<U = T>(onFinally?: () => PromiseLike<U> | U): Promise<Awaited<T>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onFinally | () =&gt; PromiseLike&lt;U&gt; \| U | 否 | The callback to execute when the Promise is settled. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;T&gt;&gt; | Promise used to return Awaited&lt;T&gt;. |

## race

```TypeScript
static race<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>
```

Waits for the first promise to settle from a FixedArray.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-static race<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>--><!--Device-Promise-static race<U>(promises: FixedArray<PromiseLike<U> | U | undefined>): Promise<Awaited<U>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| promises | FixedArray&lt;PromiseLike&lt;U&gt; \| U \| undefined&gt; | 是 | The promises to wait for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## race

```TypeScript
static race<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>
```

Waits for the first promise to settle from an Iterable.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-static race<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>--><!--Device-Promise-static race<U>(promises: Iterable<PromiseLike<U> | U>): Promise<Awaited<U>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| promises | Iterable&lt;PromiseLike&lt;U&gt; \| U&gt; | 是 | The promises to wait for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## reject

```TypeScript
static reject(): Promise<void>
```

Creates a rejected Promise with no value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-static reject(): Promise<void>--><!--Device-Promise-static reject(): Promise<void>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## reject

```TypeScript
static reject<U = never>(error: Error): Promise<Awaited<U>>
```

Creates a rejected Promise with the given error.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-static reject<U = never>(error: Error): Promise<Awaited<U>>--><!--Device-Promise-static reject<U = never>(error: Error): Promise<Awaited<U>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | Error | 是 | The error to reject with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## resolve

```TypeScript
static resolve(): Promise<void>
```

Creates a resolved Promise with no value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-static resolve(): Promise<void>--><!--Device-Promise-static resolve(): Promise<void>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## resolve

```TypeScript
static resolve<U>(value: PromiseLike<U> | U): Promise<Awaited<U>>
```

Creates a resolved Promise with the given value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-static resolve<U>(value: PromiseLike<U> | U): Promise<Awaited<U>>--><!--Device-Promise-static resolve<U>(value: PromiseLike<U> | U): Promise<Awaited<U>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PromiseLike](arkts-arkts-promise-promiselike-i.md)&lt;U&gt; \| U | 是 | The value to resolve with. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## then

```TypeScript
then<U = T>(onFulfilled: () => PromiseLike<U> | U): Promise<Awaited<U>>
```

Attaches a callback for the resolution of the Promise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-then<U = T>(onFulfilled: () => PromiseLike<U> | U): Promise<Awaited<U>>--><!--Device-Promise-then<U = T>(onFulfilled: () => PromiseLike<U> | U): Promise<Awaited<U>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onFulfilled | () =&gt; PromiseLike&lt;U&gt; \| U | 是 | The callback to execute when the Promise is resolved. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;U&gt;&gt; | Promise used to return Awaited&lt;U&gt;. |

## then

```TypeScript
then(_onFulfilled?: undefined): Promise<Awaited<T>>
```

Attaches no callback for the resolution of the Promise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-then(_onFulfilled?: undefined): Promise<Awaited<T>>--><!--Device-Promise-then(_onFulfilled?: undefined): Promise<Awaited<T>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| _onFulfilled | undefined | 否 | Undefined to skip fulfillment handling. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;T&gt;&gt; | Promise used to return Awaited&lt;T&gt;. |

## then

```TypeScript
then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,
        onRejected?: (error: Error) => PromiseLike<E> | E): Promise<Awaited<U | E>>
```

Attaches callbacks for the resolution and/or rejection of the Promise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Promise-then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,        onRejected?: (error: Error) => PromiseLike<E> | E): Promise<Awaited<U | E>>--><!--Device-Promise-then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,        onRejected?: (error: Error) => PromiseLike<E> | E): Promise<Awaited<U | E>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onFulfilled | (value: T) =&gt; PromiseLike&lt;U&gt; \| U | 是 | The callback to execute when the Promise is resolved. |
| onRejected | (error: Error) =&gt; PromiseLike&lt;E&gt; \| E | 否 | The callback to execute when the Promise is rejected. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;U \| E&gt;&gt; | Promise used to return Awaited&lt;U \| E&gt;. |

