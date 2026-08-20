# PromiseLike

Represents a thenable object.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export interface PromiseLike--><!--Device-unnamed-export interface PromiseLike-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## then

```TypeScript
then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,
        onRejected?: (error: Error) => PromiseLike<E> | E): PromiseLike<Awaited<U | E>>
```

Attaches callbacks for the resolution and/or rejection of the Promise.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PromiseLike-then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,        onRejected?: (error: Error) => PromiseLike<E> | E): PromiseLike<Awaited<U | E>>--><!--Device-PromiseLike-then<U = T, E = never>(onFulfilled: (value: T) => PromiseLike<U> | U,        onRejected?: (error: Error) => PromiseLike<E> | E): PromiseLike<Awaited<U | E>>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onFulfilled | (value: T) =&gt; PromiseLike&lt;U&gt; \| U | Yes | The callback to execute when the Promise is resolved. |
| onRejected | (error: Error) =&gt; PromiseLike&lt;E&gt; \| E | No | The callback to execute when the Promise is rejected. |

**Return value:**

| Type | Description |
| --- | --- |
| [PromiseLike](arkts-arkts-promise-promiselike-i.md)&lt;[Awaited](../../apis-default/arkts-apis/arkts-awaited-t.md)&lt;U \| E&gt;&gt; | A PromiseLike for the result of the callbacks. |

