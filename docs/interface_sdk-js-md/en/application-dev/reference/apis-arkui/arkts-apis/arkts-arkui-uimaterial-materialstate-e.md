# MaterialState

材质使能状态枚举，表示应用级沉浸式系统材质配置的状态。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-uiMaterial-export enum MaterialState--><!--Device-uiMaterial-export enum MaterialState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 0
```

默认模式。[弹出框Dialog](../../../ui/arkts-base-dialog-overview.md)、[即时反馈（Toast）](../../../ui/arkts-create-toast.md)、  
[AlphabetIndexer](alphabet_indexer)在组件本身未设置背景颜色、模糊参数和阴影参数时默认开启沉浸式系统材质；[Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md)设置  
[copyOption](arkts-arkui-text-textattribute-i.md#copyoption)后长按或双击触发的文本菜单默认开启沉浸式系统材质；其他组件由应用主动设置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialState-DEFAULT = 0--><!--Device-MaterialState-DEFAULT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ENABLE

```TypeScript
ENABLE = 1
```

使能模式。[弹出框Dialog](../../../ui/arkts-base-dialog-overview.md)、[即时反馈（Toast）](../../../ui/arkts-create-toast.md)、  
[AlphabetIndexer](alphabet_indexer)、[ChipGroup](arkts-arkui-advanced-chipgroup.md)、  
[Chip](arkts-arkui-advanced-chip.md)、[Select](arkts-arkui-select-select-f.md#select)、[菜单控制](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)、[Toggle](arkts-arkui-toggle-toggle-f.md#toggle)、  
[SegmentButton](arkts-arkui-advanced-segmentbutton.md)、  
[SegmentButtonV2](arkts-arkui-advanced-segmentbuttonv2.md)、[Slider](arkts-arkui-slider-slider-f.md#slider)、  
[bindSheet](arkts-arkui-common-commonmethod-i.md#bindsheet)、[SelectionMenu](arkts-arkui-advanced-selectionmenu.md)组件默认开启沉浸式系统材质；  
[Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md)设置[copyOption](arkts-arkui-text-textattribute-i.md#copyoption)后长按或双击触发的文本菜单默认开启沉浸式系统材质。此模式下，沉浸式系统材质样式生效的优先级高于组件本身设置的背景色、模糊、阴影和边框样式。其他组件需开发者主动设置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialState-ENABLE = 1--><!--Device-MaterialState-ENABLE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DISABLE

```TypeScript
DISABLE = 2
```

禁用模式。所有组件禁止开启沉浸式系统材质，即使主动为组件设置沉浸式系统材质参数也不会生效。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaterialState-DISABLE = 2--><!--Device-MaterialState-DISABLE = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

