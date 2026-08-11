# PromiseConstructor

Represents the completion of an asynchronous operation

<!--Device-unnamed-interface PromiseConstructor--><!--Device-unnamed-interface PromiseConstructor-End-->

## any

```TypeScript
any<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>
```

The any function returns a promise that is fulfilled by the first given promise to be fulfilled, or rejected with an AggregateError containing an array of rejection reasons if all of the given promises are rejected. It resolves all elements of the passed iterable to promises as it runs this algorithm.

<!--Device-PromiseConstructor-any<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>--><!--Device-PromiseConstructor-any<T extends readonly unknown[] | []>(values: T): Promise<Awaited<T[number]>>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Awaited&lt;T[number]&gt;&gt; |

## any

```TypeScript
any<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>
```

The any function returns a promise that is fulfilled by the first given promise to be fulfilled, or rejected with an AggregateError containing an array of rejection reasons if all of the given promises are rejected. It resolves all elements of the passed iterable to promises as it runs this algorithm.

<!--Device-PromiseConstructor-any<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>--><!--Device-PromiseConstructor-any<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | Iterable&lt;T \| [PromiseLike&lt;T&gt;&gt;](../../apis-arkts/arkts-apis/arkts-arkts-promise-promiselike-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Awaited&lt;T&gt;&gt; |
