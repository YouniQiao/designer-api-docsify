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

| Type | Description |
| --- | --- |
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
