# PromiseConstructor

**Since:** -1

<!--Device-unnamed-interface PromiseConstructor--><!--Device-unnamed-interface PromiseConstructor-End-->

## Modules to Import

```TypeScript
```

## all

```TypeScript
all<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>[]>
```

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve, or rejected when any Promise is rejected.

**Since:** -1

<!--Device-PromiseConstructor-all<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>[]>--><!--Device-PromiseConstructor-all<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>[]>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | Iterable&lt;T \| PromiseLike&lt;T&gt;&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## race

```TypeScript
race<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>
```

Creates a Promise that is resolved or rejected when any of the provided Promises are resolved or rejected.

**Since:** -1

<!--Device-PromiseConstructor-race<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>--><!--Device-PromiseConstructor-race<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | Iterable&lt;T \| PromiseLike&lt;T&gt;&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
