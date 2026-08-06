# ParallelizeUI

## ParallelizeUI

```TypeScript
export declare function ParallelizeUI(
  options: ParallelOption | undefined,
  content_: CustomBuilder,
): void
```

Define the constructor of ParallelizeUI.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ParallelizeUI(  options: ParallelOption | undefined,  content_: CustomBuilder,): void--><!--Device-unnamed-export declare function ParallelizeUI(  options: ParallelOption | undefined,  content_: CustomBuilder,): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | ParallelizeUI Option |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parallel creation of content |


## ParallelizeUI

```TypeScript
export declare function ParallelizeUI<T>(
  options: ParallelOption | undefined,
  param: () => T,
  content_: CustomBuilderT<T>,
): void
```

Define the constructor of ParallelizeUI.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ParallelizeUI<T>(  options: ParallelOption | undefined,  param: () => T,  content_: CustomBuilderT<T>,): void--><!--Device-unnamed-export declare function ParallelizeUI<T>(  options: ParallelOption | undefined,  param: () => T,  content_: CustomBuilderT<T>,): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | ParallelizeUI Option |
| param | () =&gt; T | Yes | ParallelizeUI parameter |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes | Parallel creation of content |


## ParallelizeUI

```TypeScript
export declare function ParallelizeUI<V, T>(
  options: ParallelOption | undefined,
  arr: Array<V>,
  param: (item: V, index: int) => T,
  content_: CustomBuilderT<T>
): void
```

On-demand parallel item creation for List and Grid.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ParallelizeUI<V, T>(  options: ParallelOption | undefined,  arr: Array<V>,  param: (item: V, index: int) => T,  content_: CustomBuilderT<T>): void--><!--Device-unnamed-export declare function ParallelizeUI<V, T>(  options: ParallelOption | undefined,  arr: Array<V>,  param: (item: V, index: int) => T,  content_: CustomBuilderT<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | ParallelizeUI Option |
| arr | Array&lt;V&gt; | Yes | The array collection to be used in UI |
| param | (item: V, index: int) =&gt; T | Yes | Define item generator function |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes | Parallel creation of content |

