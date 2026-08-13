# Iterator

**Since:** -1

**Deprecated since:** -1

<!--Device-unnamed-interface Iterator--><!--Device-unnamed-interface Iterator-End-->

## next

```TypeScript
next(...args: [] | [TNext]): IteratorResult<T, TReturn>
```

**Since:** -1

**Deprecated since:** -1

<!--Device-Iterator-next(...args: [] | [TNext]): IteratorResult<T, TReturn>--><!--Device-Iterator-next(...args: [] | [TNext]): IteratorResult<T, TReturn>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [] \| [TNext] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt; |

## return

```TypeScript
return?(value?: TReturn): IteratorResult<T, TReturn>
```

**Since:** -1

**Deprecated since:** -1

<!--Device-Iterator-return?(value?: TReturn): IteratorResult<T, TReturn>--><!--Device-Iterator-return?(value?: TReturn): IteratorResult<T, TReturn>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | TReturn | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt; |

## throw

```TypeScript
throw?(e?: any): IteratorResult<T, TReturn>
```

**Since:** -1

**Deprecated since:** -1

<!--Device-Iterator-throw?(e?: any): IteratorResult<T, TReturn>--><!--Device-Iterator-throw?(e?: any): IteratorResult<T, TReturn>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| e | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt; |
