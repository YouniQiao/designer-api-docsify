# PromiseConstructor

Represents the completion of an asynchronous operation

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-interface PromiseConstructor--><!--Device-unnamed-interface PromiseConstructor-End-->

## any

```TypeScript
any<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>
```

The any function returns a promise that is fulfilled by the first given promise to be fulfilled, or rejected with an AggregateError containing an array of rejection reasons if all of the given promises are rejected. It resolves all elements of the passed iterable to promises as it runs this algorithm.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-any<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>--><!--Device-PromiseConstructor-any<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;T[number]&gt;&gt; |  |

## any

```TypeScript
any<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>
```

The any function returns a promise that is fulfilled by the first given promise to be fulfilled, or rejected with an AggregateError containing an array of rejection reasons if all of the given promises are rejected. It resolves all elements of the passed iterable to promises as it runs this algorithm.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-any<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>--><!--Device-PromiseConstructor-any<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | Iterable&lt;T \| PromiseLike&lt;T&gt;&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;T&gt;&gt; |  |

