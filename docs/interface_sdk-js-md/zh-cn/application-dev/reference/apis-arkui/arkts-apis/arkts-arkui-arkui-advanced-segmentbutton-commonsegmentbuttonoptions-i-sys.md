# CommonSegmentButtonOptions

定义分段按钮组件的可自定义的属性。

**起始版本：** 11

<!--Device-unnamed-interface CommonSegmentButtonOptions--><!--Device-unnamed-interface CommonSegmentButtonOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { SegmentButton, SegmentButtonOptions, SegmentButtonItemOptionsArray, TabSegmentButtonOptions, TabSegmentButtonConstructionOptions, CapsuleSegmentButtonOptions, CapsuleSegmentButtonConstructionOptions, SegmentButtonTextItem, SegmentButtonIconItem, SegmentButtonIconTextItem, DimensionNoPercentage, CommonSegmentButtonOptions, ItemRestriction, SegmentButtonItemTuple, SegmentButtonItemArray, SegmentButtonItemOptionsConstructorOptions, SegmentButtonItemOptions, BorderRadiusMode } from '@kit.ArkUI';
```

## backgroundSystemMaterial

```TypeScript
backgroundSystemMaterial?: uiMaterial.Material
```

分段按钮组件的背景板的系统材质。不同系统材质具有不同的属性，产生不同的效果。传入材质后，SegmentButton的动效发生改变。对于胶囊类多选分段按钮（即type为"capsule"且multiply为true），该属性不生效。默认值：无材质效果。从API版本26.0.0开始，除胶囊类多选分段按钮（即type为"capsule"且multiply为true）外，backgroundSystemMaterial设置自动反色的系统材质时，fontColor和 selectedFontColor使用支持反色的特殊系统资源，颜色自动适配到材质背景色的反色。

**类型：** uiMaterial.Material

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-CommonSegmentButtonOptions-backgroundSystemMaterial?: uiMaterial.Material--><!--Device-CommonSegmentButtonOptions-backgroundSystemMaterial?: uiMaterial.Material-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

