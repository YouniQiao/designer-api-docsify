# PromiseConstructor

## allSettled

```TypeScript
allSettled<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: PromiseSettledResult<Awaited<T[P]>> }>
```

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve or reject.

<!--Device-PromiseConstructor-allSettled<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: PromiseSettledResult<Awaited<T[P]>> }>--><!--Device-PromiseConstructor-allSettled<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: PromiseSettledResult<Awaited<T[P]>> }>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;{ -readonly [P in keyof T]: PromiseSettledResult&lt;Awaited&lt;T[P]&gt;&gt; }&gt; |

## allSettled

```TypeScript
allSettled<T>(values: Iterable<T | PromiseLike<T>>): Promise<PromiseSettledResult<Awaited<T>>[]>
```

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve or reject.

<!--Device-PromiseConstructor-allSettled<T>(values: Iterable<T | PromiseLike<T>>): Promise<PromiseSettledResult<Awaited<T>>[]>--><!--Device-PromiseConstructor-allSettled<T>(values: Iterable<T | PromiseLike<T>>): Promise<PromiseSettledResult<Awaited<T>>[]>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | Iterable&lt;T \| [PromiseLike&lt;T&gt;&gt;](../../apis-arkts/arkts-apis/arkts-arkts-promise-promiselike-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;PromiseSettledResult&lt;Awaited&lt;T&gt;&gt;[]&gt; |
