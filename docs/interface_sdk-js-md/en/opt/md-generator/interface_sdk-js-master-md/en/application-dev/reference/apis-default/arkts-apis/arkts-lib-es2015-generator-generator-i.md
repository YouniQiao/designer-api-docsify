# Generator

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): Generator<T, TReturn, TNext>
```

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Generator & lt;T, TReturn, TNext & gt; |

## next

```TypeScript
next(...args: [] | [TNext]): IteratorResult<T, TReturn>
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [] \| [TNext] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IteratorResult](arkts-iteratorresult-t.md)&lt;T, TReturn&gt; |

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
| [IteratorResult](arkts-iteratorresult-t.md)&lt;T, TReturn&gt; |

## throw

```TypeScript
throw(e: any): IteratorResult<T, TReturn>
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [e](../../apis-arkts/arkts-apis/arkts-arkts-math-decimal-decimal-c.md) | any | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IteratorResult](arkts-iteratorresult-t.md)&lt;T, TReturn&gt; |
