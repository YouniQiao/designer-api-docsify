# AsyncIterator

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-interface AsyncIterator--><!--Device-unnamed-interface AsyncIterator-End-->

## next

```TypeScript
next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>
```

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-AsyncIterator-next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncIterator-next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>-End-->

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
return?(value?: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>
```

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-AsyncIterator-return?(value?: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncIterator-return?(value?: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | TReturn \| PromiseLike&lt;TReturn&gt; | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;IteratorResult&lt;T, TReturn&gt;&gt; |  |

## throw

```TypeScript
throw?(e?: any): Promise<IteratorResult<T, TReturn>>
```

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-AsyncIterator-throw?(e?: any): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncIterator-throw?(e?: any): Promise<IteratorResult<T, TReturn>>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| e | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;IteratorResult&lt;T, TReturn&gt;&gt; |  |

