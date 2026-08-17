# AsyncGenerator

**Inheritance/Implementation:** AsyncGenerator extends AsyncIterator<T, TReturn, TNext>

**Since:** -1

<!--Device-unnamed-interface AsyncGenerator--><!--Device-unnamed-interface AsyncGenerator-End-->

## [Symbol.asyncIterator]

```TypeScript
[Symbol.asyncIterator](): AsyncGenerator<T, TReturn, TNext>
```

**Since:** -1

<!--Device-AsyncGenerator-[Symbol.asyncIterator](): AsyncGenerator<T, TReturn, TNext>--><!--Device-AsyncGenerator-[Symbol.asyncIterator](): AsyncGenerator<T, TReturn, TNext>-End-->

**Return value:**

| Type | Description |
| --- | --- |
| [AsyncGenerator](arkts-na-lib-es2018-asyncgenerator-asyncgenerator-i.md)&lt;T, TReturn, TNext&gt; |  |

## next

```TypeScript
next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>
```

**Since:** -1

<!--Device-AsyncGenerator-next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncGenerator-next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| args | [] \| [TNext] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;IteratorResult&lt;T, TReturn&gt;&gt; |  |

## return

```TypeScript
return(value: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>
```

**Since:** -1

<!--Device-AsyncGenerator-return(value: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncGenerator-return(value: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | TReturn \| PromiseLike&lt;TReturn&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;IteratorResult&lt;T, TReturn&gt;&gt; |  |

## throw

```TypeScript
throw(e: any): Promise<IteratorResult<T, TReturn>>
```

**Since:** -1

<!--Device-AsyncGenerator-throw(e: any): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncGenerator-throw(e: any): Promise<IteratorResult<T, TReturn>>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| e | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;IteratorResult&lt;T, TReturn&gt;&gt; |  |

