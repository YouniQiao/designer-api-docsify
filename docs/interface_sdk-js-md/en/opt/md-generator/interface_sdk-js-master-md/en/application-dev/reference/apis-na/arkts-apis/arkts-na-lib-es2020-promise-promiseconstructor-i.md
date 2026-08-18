# PromiseConstructor

**Since:** -1

<!--Device-unnamed-interface PromiseConstructor--><!--Device-unnamed-interface PromiseConstructor-End-->

## Modules to Import

```TypeScript
```

## allSettled

```TypeScript
allSettled<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: PromiseSettledResult<Awaited<T[P]>> }>
```

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve or reject.

**Since:** -1

<!--Device-PromiseConstructor-allSettled<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: PromiseSettledResult<Awaited<T[P]>> }>--><!--Device-PromiseConstructor-allSettled<T extends readonly unknown[] | []>(values: T): Promise<{ -readonly [P in keyof T]: PromiseSettledResult<Awaited<T[P]>> }>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | T | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;{ -readonly [P in keyof T]: PromiseSettledResult&lt;[Awaited](arkts-na-awaited-t.md)&lt;T[P]&gt;&gt; }&gt; |

## allSettled

```TypeScript
allSettled<T>(values: Iterable<T | PromiseLike<T>>): Promise<PromiseSettledResult<Awaited<T>>[]>
```

Creates a Promise that is resolved with an array of results when all of the provided Promises resolve or reject.

**Since:** -1

<!--Device-PromiseConstructor-allSettled<T>(values: Iterable<T | PromiseLike<T>>): Promise<PromiseSettledResult<Awaited<T>>[]>--><!--Device-PromiseConstructor-allSettled<T>(values: Iterable<T | PromiseLike<T>>): Promise<PromiseSettledResult<Awaited<T>>[]>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| values | Iterable & lt;T \ | [PromiseLike](arkts-na-lib-es5-promiselike-i.md)&lt;T&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PromiseSettledResult](arkts-na-promisesettledresult-t.md)&lt;[Awaited](arkts-na-awaited-t.md)&lt;T&gt;&gt;[]&gt; |
