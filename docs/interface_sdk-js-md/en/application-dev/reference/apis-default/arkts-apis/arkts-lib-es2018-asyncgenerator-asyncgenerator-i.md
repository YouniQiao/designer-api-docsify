# AsyncGenerator

## Modules to Import

```TypeScript
```

## [Symbol.asyncIterator]

```TypeScript
[Symbol.asyncIterator](): AsyncGenerator<T, TReturn, TNext>
```

**Return value:**

| Type | Description |
| --- | --- |
## next

```TypeScript
next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>
```

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

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | TReturn \| PromiseLike & lt;TReturn & gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## throw

```TypeScript
throw(e: any): Promise<IteratorResult<T, TReturn>>
```

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| e | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
