# LazyVWaterFlowLayoutAttribute

定义懒加载垂直瀑布流布局属性。

**Inheritance/Implementation:** LazyVWaterFlowLayoutAttribute extends [LazyWaterFlowLayoutAttribute<LazyVWaterFlowLayoutAttribute>](LazyWaterFlowLayoutAttribute<LazyVWaterFlowLayoutAttribute>)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-export declare class LazyVWaterFlowLayoutAttribute extends LazyWaterFlowLayoutAttribute<LazyVWaterFlowLayoutAttribute>--><!--Device-unnamed-export declare class LazyVWaterFlowLayoutAttribute extends LazyWaterFlowLayoutAttribute<LazyVWaterFlowLayoutAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LazyVWaterFlowLayout, LazyWaterFlowLayoutAttribute, LazyVWaterFlowLayoutAttribute } from 'kits/@kit.ArkUI';
```

## columnsTemplate

```TypeScript
columnsTemplate(value: string | ItemFillPolicy | undefined): LazyVWaterFlowLayoutAttribute
```

该参数用于指定当前瀑布流布局中的列数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyVWaterFlowLayoutAttribute-columnsTemplate(value: string | ItemFillPolicy | undefined): LazyVWaterFlowLayoutAttribute--><!--Device-LazyVWaterFlowLayoutAttribute-columnsTemplate(value: string | ItemFillPolicy | undefined): LazyVWaterFlowLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| ItemFillPolicy \| undefined | Yes | 布局中的列数。 &lt;br&gt;默认值：'1fr' |

**Return value:**

| Type | Description |
| --- | --- |
| [LazyVWaterFlowLayoutAttribute](arkts-arkui-arkui-components-arklazywaterflowlayout-lazyvwaterflowlayoutattribute-i.md) |  |

