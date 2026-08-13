# Iterator

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-interface Iterator--><!--Device-unnamed-interface Iterator-End-->

## next

```TypeScript
next(...args: [] | [TNext]): IteratorResult<T, TReturn>
```

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-Iterator-next(...args: [] | [TNext]): IteratorResult<T, TReturn>--><!--Device-Iterator-next(...args: [] | [TNext]): IteratorResult<T, TReturn>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| args | [] \| [TNext] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt; |  |

## return

```TypeScript
return?(value?: TReturn): IteratorResult<T, TReturn>
```

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-Iterator-return?(value?: TReturn): IteratorResult<T, TReturn>--><!--Device-Iterator-return?(value?: TReturn): IteratorResult<T, TReturn>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | TReturn | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt; |  |

## throw

```TypeScript
throw?(e?: any): IteratorResult<T, TReturn>
```

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-Iterator-throw?(e?: any): IteratorResult<T, TReturn>--><!--Device-Iterator-throw?(e?: any): IteratorResult<T, TReturn>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| e | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt; |  |

