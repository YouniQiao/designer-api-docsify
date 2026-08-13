# AsyncIterator

**Since:** -1

**Deprecated since:** -1

<!--Device-unnamed-interface AsyncIterator--><!--Device-unnamed-interface AsyncIterator-End-->

## next

```TypeScript
next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>
```

**Since:** -1

**Deprecated since:** -1

<!--Device-AsyncIterator-next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncIterator-next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>-End-->

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
return?(value?: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>
```

**Since:** -1

**Deprecated since:** -1

<!--Device-AsyncIterator-return?(value?: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncIterator-return?(value?: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | TReturn \| [PromiseLike](arkts-na-lib-es5-promiselike-i.md)&lt;TReturn&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt;&gt; |

## throw

```TypeScript
throw?(e?: any): Promise<IteratorResult<T, TReturn>>
```

**Since:** -1

**Deprecated since:** -1

<!--Device-AsyncIterator-throw?(e?: any): Promise<IteratorResult<T, TReturn>>--><!--Device-AsyncIterator-throw?(e?: any): Promise<IteratorResult<T, TReturn>>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| e | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt;&gt; |
