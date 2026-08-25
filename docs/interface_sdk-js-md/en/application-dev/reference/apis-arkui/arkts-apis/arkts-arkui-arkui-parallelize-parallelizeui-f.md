# ParallelizeUI

## Modules to Import

```TypeScript
```

## ParallelizeUI

```TypeScript
export declare function ParallelizeUI(
  options: ParallelOption | undefined,
  content_: CustomBuilder,
): void
```

Define the constructor of ParallelizeUI.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ParallelOption](arkts-arkui-arkui-parallelize-paralleloption-i.md) \| undefined | Yes |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |


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

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ParallelOption](arkts-arkui-arkui-parallelize-paralleloption-i.md) \| undefined | Yes |
| param | () = & gt; T | Yes |
| content_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;T&gt; | Yes |


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

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ParallelOption](arkts-arkui-arkui-parallelize-paralleloption-i.md) \| undefined | Yes |
| arr | Array & lt;V & gt; | Yes |
| param | (item: V, index: int) = & gt; T | Yes |
| content_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;T&gt; | Yes |
