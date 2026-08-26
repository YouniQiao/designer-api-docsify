# Generator

## Modules to Import

```TypeScript
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): Generator<T, TReturn, TNext>
```

**Return value:**

| Type | Description |
| --- | --- |
## next

```TypeScript
next(...args: [] | [TNext]): IteratorResult<T, TReturn>
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
return(value: TReturn): IteratorResult<T, TReturn>
```

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | TReturn | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## throw

```TypeScript
throw(e: any): IteratorResult<T, TReturn>
```

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| e | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
