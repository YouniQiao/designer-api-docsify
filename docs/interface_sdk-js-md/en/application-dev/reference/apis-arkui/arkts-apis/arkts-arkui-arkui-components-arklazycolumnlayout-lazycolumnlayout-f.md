# LazyColumnLayout

## Modules to Import

```TypeScript
import { LazyColumnLayoutAttribute, LazyColumnLayout } from 'kits/@kit.ArkUI';
```

## LazyColumnLayout

```TypeScript
export declare function LazyColumnLayout(
    content_?: CustomBuilder,
): LazyColumnLayoutAttribute
```

Defines LazyColumnLayout Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function LazyColumnLayout(    content_?: CustomBuilder,): LazyColumnLayoutAttribute--><!--Device-unnamed-export declare function LazyColumnLayout(    content_?: CustomBuilder,): LazyColumnLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | content |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyColumnLayoutAttribute](arkts-arkui-arkui-components-arklazycolumnlayout-lazycolumnlayoutattribute-i.md) | The attribute of the LazyColumnLayout. |


## LazyColumnLayout

```TypeScript
export declare function LazyColumnLayout(
    style_: CustomBuilderT<LazyColumnLayoutAttribute>,
    content_?: CustomBuilder
): LazyColumnLayoutAttribute
```

Defines LazyColumnLayout Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function LazyColumnLayout(    style_: CustomBuilderT<LazyColumnLayoutAttribute>,    content_?: CustomBuilder): LazyColumnLayoutAttribute--><!--Device-unnamed-export declare function LazyColumnLayout(    style_: CustomBuilderT<LazyColumnLayoutAttribute>,    content_?: CustomBuilder): LazyColumnLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;LazyColumnLayoutAttribute&gt; | Yes | The style to create a LazyColumnLayout. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | content |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyColumnLayoutAttribute](arkts-arkui-arkui-components-arklazycolumnlayout-lazycolumnlayoutattribute-i.md) | The attribute of the LazyColumnLayout. |

