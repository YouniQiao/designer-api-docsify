# Generator

**Inheritance/Implementation:** Generator extends [Iterator<T, TReturn, TNext>](Iterator<T, TReturn, TNext>)

**ArkTS mode:** ArkTS-Dyn only

<!--Device-unnamed-interface Generator<T = unknown, TReturn = any, TNext = unknown> extends Iterator<T, TReturn, TNext>--><!--Device-unnamed-interface Generator<T = unknown, TReturn = any, TNext = unknown> extends Iterator<T, TReturn, TNext>-End-->

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): Generator<T, TReturn, TNext>
```

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Generator-[Symbol.iterator](): Generator<T, TReturn, TNext>--><!--Device-Generator-[Symbol.iterator](): Generator<T, TReturn, TNext>-End-->

**Return value:**

| Type | Description |
| --- | --- |
| Generator&lt;T, TReturn, TNext&gt; |  |

## next

```TypeScript
next(...args: [] | [TNext]): IteratorResult<T, TReturn>
```

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Generator-next(...args: [] | [TNext]): IteratorResult<T, TReturn>--><!--Device-Generator-next(...args: [] | [TNext]): IteratorResult<T, TReturn>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| args | [] \| [TNext] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T, TReturn&gt; |  |

## return

```TypeScript
return(value: TReturn): IteratorResult<T, TReturn>
```

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Generator-return(value: TReturn): IteratorResult<T, TReturn>--><!--Device-Generator-return(value: TReturn): IteratorResult<T, TReturn>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | TReturn | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T, TReturn&gt; |  |

## throw

```TypeScript
throw(e: any): IteratorResult<T, TReturn>
```

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Generator-throw(e: any): IteratorResult<T, TReturn>--><!--Device-Generator-throw(e: any): IteratorResult<T, TReturn>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| e | any | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T, TReturn&gt; |  |

