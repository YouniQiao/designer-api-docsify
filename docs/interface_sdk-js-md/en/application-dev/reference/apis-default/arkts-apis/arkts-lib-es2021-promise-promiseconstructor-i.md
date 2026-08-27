# PromiseConstructor

Represents the completion of an asynchronous operation

## Modules to Import

```TypeScript
```

## any

```TypeScript
any<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>
```

The any function returns a promise that is fulfilled by the first given promise to be fulfilled, or rejected with an AggregateError containing an array of rejection reasons if all of the given promises are rejected. It resolves all elements of the passed iterable to promises as it runs this algorithm.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## any

```TypeScript
any<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>
```

The any function returns a promise that is fulfilled by the first given promise to be fulfilled, or rejected with an AggregateError containing an array of rejection reasons if all of the given promises are rejected. It resolves all elements of the passed iterable to promises as it runs this algorithm.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| values | Iterable&lt;T \| PromiseLike&lt;T&gt;&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
