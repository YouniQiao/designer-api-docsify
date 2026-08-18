# Generator

**Inheritance/Implementation:** Generator extends Iterator<T, TReturn, TNext>

**Since:** -1

<!--Device-unnamed-interface Generator--><!--Device-unnamed-interface Generator-End-->

## Modules to Import

```TypeScript
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): Generator<T, TReturn, TNext>
```

**Since:** -1

<!--Device-Generator-[Symbol.iterator](): Generator<T, TReturn, TNext>--><!--Device-Generator-[Symbol.iterator](): Generator<T, TReturn, TNext>-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Generator & lt;T, TReturn, TNext & gt; |

## next

```TypeScript
next(...args: [] | [TNext]): IteratorResult<T, TReturn>
```

**Since:** -1

<!--Device-Generator-next(...args: [] | [TNext]): IteratorResult<T, TReturn>--><!--Device-Generator-next(...args: [] | [TNext]): IteratorResult<T, TReturn>-End-->

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
return(value: TReturn): IteratorResult<T, TReturn>
```

**Since:** -1

<!--Device-Generator-return(value: TReturn): IteratorResult<T, TReturn>--><!--Device-Generator-return(value: TReturn): IteratorResult<T, TReturn>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | TReturn | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt; |

## throw

```TypeScript
throw(e: any): IteratorResult<T, TReturn>
```

**Since:** -1

<!--Device-Generator-throw(e: any): IteratorResult<T, TReturn>--><!--Device-Generator-throw(e: any): IteratorResult<T, TReturn>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| e | any | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IteratorResult](arkts-na-iteratorresult-t.md)&lt;T, TReturn&gt; |
