# LazyDynamicLayoutAttribute

Defines the LazyDynamicLayout attribute functions.

**Inheritance/Implementation:** LazyDynamicLayoutAttribute extends CommonMethod<LazyDynamicLayoutAttribute>

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare class LazyDynamicLayoutAttribute--><!--Device-unnamed-export declare class LazyDynamicLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LazyDynamicLayoutAttribute, LazyDynamicLayout } from '@kit.ArkUI';
```

## onVisibleIndexesChange

```TypeScript
onVisibleIndexesChange(callback: Callback<int[]> | undefined): LazyDynamicLayoutAttribute
```

Called when visible indexes change.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyDynamicLayoutAttribute-onVisibleIndexesChange(callback: Callback<int[]> | undefined): LazyDynamicLayoutAttribute--><!--Device-LazyDynamicLayoutAttribute-onVisibleIndexesChange(callback: Callback<int[]> | undefined): LazyDynamicLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-na/arkts-apis/arkts-na-callback-t.md)&lt;int[]&gt; \| undefined | Yes | Callback used to return the list of index numbers of visible subcomponents. &lt;br&gt;Passing undefined will unregister the callback. |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyDynamicLayoutAttribute](arkts-arkui-arkui-components-arklazydynamiclayout-lazydynamiclayoutattribute-c.md) |  |

