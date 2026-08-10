# PromiseLike

**ArkTS模式：** 仅支持ArkTS-Dyn

## then

```TypeScript
then<TResult1 = T, TResult2 = never>(onfulfilled?: ((value: T) => TResult1 | PromiseLike<TResult1>) | undefined | null, onrejected?: ((reason: any) => TResult2 | PromiseLike<TResult2>) | undefined | null): PromiseLike<TResult1 | TResult2>
```

Attaches callbacks for the resolution and/or rejection of the Promise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-PromiseLike-then<TResult1 = T, TResult2 = never>(onfulfilled?: ((value: T) => TResult1 | PromiseLike<TResult1>) | undefined | null, onrejected?: ((reason: any) => TResult2 | PromiseLike<TResult2>) | undefined | null): PromiseLike<TResult1 | TResult2>--><!--Device-PromiseLike-then<TResult1 = T, TResult2 = never>(onfulfilled?: ((value: T) => TResult1 | PromiseLike<TResult1>) | undefined | null, onrejected?: ((reason: any) => TResult2 | PromiseLike<TResult2>) | undefined | null): PromiseLike<TResult1 | TResult2>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onfulfilled | ((value: T) =&gt; TResult1 \| PromiseLike&lt;TResult1&gt;) \| undefined \| null | 否 |  |
| onrejected | ((reason: any) =&gt; TResult2 \| PromiseLike&lt;TResult2&gt;) \| undefined \| null | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PromiseLike](../../apis-arkts/arkts-apis/arkts-arkts-promise-promiselike-i.md)&lt;TResult1 \| TResult2&gt; |  |

