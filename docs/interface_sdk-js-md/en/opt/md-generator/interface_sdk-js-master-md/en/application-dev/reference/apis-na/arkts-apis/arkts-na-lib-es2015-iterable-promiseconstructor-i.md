# PromiseConstructor

**Since:** -1

**Deprecated since:** -1

<!--Device-unnamed-interface PromiseConstructor--><!--Device-unnamed-interface PromiseConstructor-End-->

## all

```TypeScript
all<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>[]>
```

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve, or rejected when any Promise is rejected.

**Since:** -1

**Deprecated since:** -1

<!--Device-PromiseConstructor-all<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>[]>--><!--Device-PromiseConstructor-all<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>[]>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | Iterable & lt;T \ | [PromiseLike](arkts-na-lib-es5-promiselike-i.md)&lt;T&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;T&gt;[]&gt; |

## race

```TypeScript
race<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>
```

Creates a Promise that is resolved or rejected when any of the provided Promises are resolved or rejected.

**Since:** -1

**Deprecated since:** -1

<!--Device-PromiseConstructor-race<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>--><!--Device-PromiseConstructor-race<T>(values: Iterable<T | PromiseLike<T>>): Promise<Awaited<T>>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | Iterable & lt;T \ | [PromiseLike](arkts-na-lib-es5-promiselike-i.md)&lt;T&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Awaited](arkts-na-awaited-t.md)&lt;T&gt;&gt; |
