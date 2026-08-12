# Iterator

**ArkTS mode:** ArkTS-Dyn only

## next

```TypeScript
next(...args: [] | [TNext]): IteratorResult<T, TReturn>
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| args | [] \| [TNext] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [IteratorResult](arkts-iteratorresult-t.md)&lt;T, TReturn&gt; |  |

## return

```TypeScript
return?(value?: TReturn): IteratorResult<T, TReturn>
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | TReturn | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [IteratorResult](arkts-iteratorresult-t.md)&lt;T, TReturn&gt; |  |

## throw

```TypeScript
throw?(e?: any): IteratorResult<T, TReturn>
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| e | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [IteratorResult](arkts-iteratorresult-t.md)&lt;T, TReturn&gt; |  |

