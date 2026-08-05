# AsyncGenerator

**Inheritance/Implementation:** AsyncGenerator extends [AsyncIterator<T, TReturn, TNext>](AsyncIterator<T, TReturn, TNext>)

**ArkTS mode:** ArkTS-Dyn only

<!--Device-unnamed-interface AsyncGenerator<T = unknown, TReturn = any, TNext = unknown> extends AsyncIterator<T, TReturn, TNext>--><!--Device-unnamed-interface AsyncGenerator<T = unknown, TReturn = any, TNext = unknown> extends AsyncIterator<T, TReturn, TNext>-End-->

## [Symbol.asyncIterator]

```TypeScript
[Symbol.asyncIterator](): AsyncGenerator<T, TReturn, TNext>
```

**ArkTS mode:** ArkTS-Dyn only

<!--Device-AsyncGenerator-[Symbol.asyncIterator](): AsyncGenerator<T, TReturn, TNext>--><!--Device-AsyncGenerator-[Symbol.asyncIterator](): AsyncGenerator<T, TReturn, TNext>-End-->

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T, TReturn, TNext&gt; |  |

## next

```TypeScript
next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>
```

**ArkTS mode:** ArkTS-Dyn only

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

**ArkTS mode:** ArkTS-Dyn only

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

**ArkTS mode:** ArkTS-Dyn only

<!--Device-AsyncGenerator-throw(e: any): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncGenerator-throw(e: any): Promise<IteratorResult<T, TReturn>>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| e | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;IteratorResult&lt;T, TReturn&gt;&gt; |  |

