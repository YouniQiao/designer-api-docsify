# Promise

Represents the completion of an asynchronous operation

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-unnamed-interface Promise<T>--><!--Device-unnamed-interface Promise<T>-End-->

## catch

```TypeScript
catch<TResult = never>(onrejected?: ((reason: any) => TResult | PromiseLike<TResult>) | undefined | null): Promise<T | TResult>
```

Attaches a callback for only the rejection of the Promise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Promise-catch<TResult = never>(onrejected?: ((reason: any) => TResult | PromiseLike<TResult>) | undefined | null): Promise<T | TResult>--><!--Device-Promise-catch<TResult = never>(onrejected?: ((reason: any) => TResult | PromiseLike<TResult>) | undefined | null): Promise<T | TResult>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onrejected | ((reason: any) =&gt; TResult \| PromiseLike&lt;TResult&gt;) \| undefined \| null | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;T \| TResult&gt; |  |

## then

```TypeScript
then<TResult1 = T, TResult2 = never>(onfulfilled?: ((value: T) => TResult1 | PromiseLike<TResult1>) | undefined | null, onrejected?: ((reason: any) => TResult2 | PromiseLike<TResult2>) | undefined | null): Promise<TResult1 | TResult2>
```

Attaches callbacks for the resolution and/or rejection of the Promise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Promise-then<TResult1 = T, TResult2 = never>(onfulfilled?: ((value: T) => TResult1 | PromiseLike<TResult1>) | undefined | null, onrejected?: ((reason: any) => TResult2 | PromiseLike<TResult2>) | undefined | null): Promise<TResult1 | TResult2>--><!--Device-Promise-then<TResult1 = T, TResult2 = never>(onfulfilled?: ((value: T) => TResult1 | PromiseLike<TResult1>) | undefined | null, onrejected?: ((reason: any) => TResult2 | PromiseLike<TResult2>) | undefined | null): Promise<TResult1 | TResult2>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onfulfilled | ((value: T) =&gt; TResult1 \| PromiseLike&lt;TResult1&gt;) \| undefined \| null | 否 |  |
| onrejected | ((reason: any) =&gt; TResult2 \| PromiseLike&lt;TResult2&gt;) \| undefined \| null | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;TResult1 \| TResult2&gt; |  |

