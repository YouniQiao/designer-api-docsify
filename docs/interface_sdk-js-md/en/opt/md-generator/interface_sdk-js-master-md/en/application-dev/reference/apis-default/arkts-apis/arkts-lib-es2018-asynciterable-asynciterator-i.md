# AsyncIterator

## next

```TypeScript
next(...args: [] | [TNext]): Promise<IteratorResult<T, TReturn>>
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| args | [] \| [TNext] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;IteratorResult&lt;T, TReturn&gt;&gt; |

## return

```TypeScript
return?(value?: TReturn | PromiseLike<TReturn>): Promise<IteratorResult<T, TReturn>>
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | TReturn \| [PromiseLike&lt;TReturn&gt;](../../apis-arkts/arkts-apis/arkts-arkts-promise-promiselike-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;IteratorResult&lt;T, TReturn&gt;&gt; |

## throw

```TypeScript
throw?(e?: any): Promise<IteratorResult<T, TReturn>>
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| e | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;IteratorResult&lt;T, TReturn&gt;&gt; |
