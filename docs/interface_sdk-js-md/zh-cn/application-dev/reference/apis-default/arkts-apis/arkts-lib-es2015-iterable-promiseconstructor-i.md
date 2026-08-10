# PromiseConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## all

```TypeScript
all<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>[]>
```

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve, or rejected when any Promise is rejected.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-all<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>[]>--><!--Device-PromiseConstructor-all<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>[]>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | Iterable&lt;T \| PromiseLike&lt;T&gt;&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;T&gt;[]&gt; |  |

## race

```TypeScript
race<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>
```

Creates a Promise that is resolved or rejected when any of the provided Promises are resolved or rejected.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-race<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>--><!--Device-PromiseConstructor-race<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | Iterable&lt;T \| PromiseLike&lt;T&gt;&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Awaited&lt;T&gt;&gt; |  |

