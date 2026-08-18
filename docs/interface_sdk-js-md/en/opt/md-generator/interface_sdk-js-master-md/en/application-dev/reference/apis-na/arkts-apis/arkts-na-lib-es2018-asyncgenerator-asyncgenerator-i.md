# AsyncGenerator

**Inheritance/Implementation:** AsyncGenerator extends AsyncIterator<T, TReturn, TNext>

**Since:** -1

<!--Device-unnamed-interface AsyncGenerator--><!--Device-unnamed-interface AsyncGenerator-End-->

## Modules to Import

```TypeScript
```

## [Symbol.asyncIterator]

```TypeScript
[Symbol.asyncIterator](): AsyncGenerator<T, TReturn, TNext>
```

**Since:** -1

<!--Device-AsyncGenerator-[Symbol.asyncIterator](): AsyncGenerator<T, TReturn, TNext>--><!--Device-AsyncGenerator-[Symbol.asyncIterator](): AsyncGenerator<T, TReturn, TNext>-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AsyncGenerator](arkts-na-lib-es2018-asyncgenerator-asyncgenerator-i.md)&lt;T, TReturn, TNext&gt; |

## next

```TypeScript
next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>
```

**Since:** -1

<!--Device-AsyncGenerator-next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncGenerator-next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [] \| [TNext] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt;&gt; |

## return

```TypeScript
return(value: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>
```

**Since:** -1

<!--Device-AsyncGenerator-return(value: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncGenerator-return(value: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | TReturn \| [PromiseLike](arkts-na-lib-es5-promiselike-i.md)&lt;TReturn&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt;&gt; |

## throw

```TypeScript
throw(e: any): Promise<IteratorResult<T, TReturn>>
```

**Since:** -1

<!--Device-AsyncGenerator-throw(e: any): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncGenerator-throw(e: any): Promise<IteratorResult<T, TReturn>>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| e | any | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt;&gt; |
