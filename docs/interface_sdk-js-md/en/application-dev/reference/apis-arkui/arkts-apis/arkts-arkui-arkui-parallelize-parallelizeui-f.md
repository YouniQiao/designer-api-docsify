# ParallelizeUI

## Modules to Import

```TypeScript
```

## ParallelizeUI

```TypeScript
@Builder
export declare function ParallelizeUI(
  options: ParallelOption | undefined,
  content_: CustomBuilder,
): void
```

Define the constructor of ParallelizeUI.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ParallelizeUI(  options: ParallelOption | undefined,  content_: CustomBuilder,): void--><!--Device-unnamed-@Builderexport declare function ParallelizeUI(  options: ParallelOption | undefined,  content_: CustomBuilder,): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ParallelOption](arkts-arkui-arkuiparallelize-paralleloption-i.md) \| undefined | Yes | ParallelizeUI Option |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | Yes | Parallel creation of content |


## ParallelizeUI

```TypeScript
@Builder
export declare function ParallelizeUI<T>(
  options: ParallelOption | undefined,
  param: () => T,
  content_: CustomBuilderT<T>,
): void
```

Define the constructor of ParallelizeUI.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ParallelizeUI<T>(  options: ParallelOption | undefined,  param: () => T,  content_: CustomBuilderT<T>,): void--><!--Device-unnamed-@Builderexport declare function ParallelizeUI<T>(  options: ParallelOption | undefined,  param: () => T,  content_: CustomBuilderT<T>,): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ParallelOption](arkts-arkui-arkuiparallelize-paralleloption-i.md) \| undefined | Yes | ParallelizeUI Option |
| param | () =&gt; T | Yes | ParallelizeUI parameter |
| content_ | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | Yes | Parallel creation of content |


## ParallelizeUI

```TypeScript
@Builder
export declare function ParallelizeUI<V, T>(
  options: ParallelOption | undefined,
  arr: Array<V>,
  param: (item: V, index: int) => T,
  content_: CustomBuilderT<T>
): void
```

On-demand parallel item creation for List and Grid.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ParallelizeUI<V, T>(  options: ParallelOption | undefined,  arr: Array<V>,  param: (item: V, index: int) => T,  content_: CustomBuilderT<T>): void--><!--Device-unnamed-@Builderexport declare function ParallelizeUI<V, T>(  options: ParallelOption | undefined,  arr: Array<V>,  param: (item: V, index: int) => T,  content_: CustomBuilderT<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ParallelOption](arkts-arkui-arkuiparallelize-paralleloption-i.md) \| undefined | Yes | ParallelizeUI Option |
| arr | Array&lt;V&gt; | Yes | The array collection to be used in UI |
| param | (item: V, index: int) =&gt; T | Yes | Define item generator function |
| content_ | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;T&gt; | Yes | Parallel creation of content |

