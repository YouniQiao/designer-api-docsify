# Generator

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): Generator<T, TReturn, TNext>
```

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Generator&lt;T, TReturn, TNext&gt; |

## next

```TypeScript
next(...args: [] | [TNext]): IteratorResult<T, TReturn>
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| args | [] \| [TNext] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IteratorResult&lt;T, TReturn&gt;](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iteratorresult-c.md) |

## return

```TypeScript
return(value: TReturn): IteratorResult<T, TReturn>
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | TReturn | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IteratorResult&lt;T, TReturn&gt;](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iteratorresult-c.md) |

## throw

```TypeScript
throw(e: any): IteratorResult<T, TReturn>
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| e | any | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IteratorResult&lt;T, TReturn&gt;](../../apis-arkts/arkts-apis/arkts-arkts-iterator-iteratorresult-c.md) |
