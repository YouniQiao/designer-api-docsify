# PromiseConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## allSettled

```TypeScript
allSettled<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: PromiseSettledResult<Awaited<T[P]>> }>
```

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve or reject.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-allSettled<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: PromiseSettledResult<Awaited<T[P]>> }>--><!--Device-PromiseConstructor-allSettled<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: PromiseSettledResult<Awaited<T[P]>> }>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;{ -readonly [P in keyof T]: PromiseSettledResult&lt;Awaited&lt;T[P]&gt;&gt; }&gt; |  |

## allSettled

```TypeScript
allSettled<T>(values: Iterable<T | PromiseLike<T>>): Promise<PromiseSettledResult<Awaited<T>>[]>
```

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve or reject.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseConstructor-allSettled<T>(values: Iterable<T | PromiseLike<T>>): Promise<PromiseSettledResult<Awaited<T>>[]>--><!--Device-PromiseConstructor-allSettled<T>(values: Iterable<T | PromiseLike<T>>): Promise<PromiseSettledResult<Awaited<T>>[]>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | Iterable&lt;T \| PromiseLike&lt;T&gt;&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;PromiseSettledResult&lt;Awaited&lt;T&gt;&gt;[]&gt; |  |

