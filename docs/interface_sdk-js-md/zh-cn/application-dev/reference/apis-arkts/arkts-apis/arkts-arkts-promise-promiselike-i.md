# PromiseLike

Represents a thenable object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface PromiseLike<out T>--><!--Device-unnamed-export interface PromiseLike<out T>-End-->

**系统能力：** SystemCapability.Utils.Lang

## then

```TypeScript
then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,
        onRejected?: (error: Error) => PromiseLike<E> | E): PromiseLike<Awaited<U | E>>
```

Attaches callbacks for the resolution and/or rejection of the Promise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PromiseLike-then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,        onRejected?: (error: Error) => PromiseLike<E> | E): PromiseLike<Awaited<U | E>>--><!--Device-PromiseLike-then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,        onRejected?: (error: Error) => PromiseLike<E> | E): PromiseLike<Awaited<U | E>>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| onFulfilled | (value: T) =&gt; PromiseLike&lt;U&gt; \| U | 是 | The callback to execute when the Promise is resolved. |
| onRejected | (error: Error) =&gt; PromiseLike&lt;E&gt; \| E | 否 | The callback to execute when the Promise is rejected. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PromiseLike](arkts-arkts-promise-promiselike-i.md)&lt;Awaited&lt;U \| E&gt;&gt; | A PromiseLike for the result of the callbacks. |

