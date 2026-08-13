# PromiseLike

**Since:** -1

**Deprecated since:** -1

<!--Device-unnamed-interface PromiseLike--><!--Device-unnamed-interface PromiseLike-End-->

## then

```TypeScript
then<TResult1 = T, TResult2 = never>(onfulfilled?: ((value: T) => TResult1 | PromiseLike<TResult1>) | undefined | null, onrejected?: ((reason: any) => TResult2 | PromiseLike<TResult2>) | undefined | null): PromiseLike<TResult1 | TResult2>
```

Attaches callbacks for the resolution and/or rejection of the Promise.

**Since:** -1

**Deprecated since:** -1

<!--Device-PromiseLike-then<TResult1 = T, TResult2 = never>(onfulfilled?: ((value: T) => TResult1 | PromiseLike<TResult1>) | undefined | null, onrejected?: ((reason: any) => TResult2 | PromiseLike<TResult2>) | undefined | null): PromiseLike<TResult1 | TResult2>--><!--Device-PromiseLike-then<TResult1 = T, TResult2 = never>(onfulfilled?: ((value: T) => TResult1 | PromiseLike<TResult1>) | undefined | null, onrejected?: ((reason: any) => TResult2 | PromiseLike<TResult2>) | undefined | null): PromiseLike<TResult1 | TResult2>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| onfulfilled | ((value: T) = & gt; TResult1 \ | [PromiseLike](arkts-na-lib-es5-promiselike-i.md) & lt;TResult1 & gt;) \ | undefined \| null | No |
| onrejected | ((reason: any) = & gt; TResult2 \ | [PromiseLike](arkts-na-lib-es5-promiselike-i.md) & lt;TResult2 & gt;) \ | undefined \| null | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PromiseLike](arkts-na-lib-es5-promiselike-i.md)&lt;TResult1 \| TResult2 & gt; |
