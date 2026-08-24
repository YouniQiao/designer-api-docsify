# CapsuleSegmentButtonV2

分段按钮组件用于创建页签型、单选或多选的胶囊型分段按钮，支持文本、图标、Symbol等多种选项类型及图文混合配置，可自定义字体、颜色、圆角等样式。页签型分段按钮适用于页签切换场景，单选胶囊型分段按钮适用于单选切换场景，多选胶囊型分段按 钮适用于多选筛选场景。

**起始版本：** 18

**装饰器类型：** @ComponentV2

<!--Device-unnamed-export declare struct CapsuleSegmentButtonV2--><!--Device-unnamed-export declare struct CapsuleSegmentButtonV2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { SegmentButtonV2ItemOptions, OnSelectedIndexChange, OnSelectedIndexesChange, SegmentButtonV2Item, SegmentButtonV2Items, TabSegmentButtonV2, CapsuleSegmentButtonV2, MultiCapsuleSegmentButtonV2 } from '@kit.ArkUI';
```

## backgroundSystemMaterial

```TypeScript
readonly backgroundSystemMaterial?: uiMaterial.Material
```

分段按钮组件的背景板的系统材质。不同系统材质包含不同的属性影响效果。传入材质后，SegmentButtonV2的动效发生改变。默认值：无材质效果。该成员只读，不支持更改。

**类型：** uiMaterial.Material

**起始版本：** 23

**装饰器类型：** @Param

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-CapsuleSegmentButtonV2-@Param  readonly backgroundSystemMaterial?: uiMaterial.Material--><!--Device-CapsuleSegmentButtonV2-@Param  readonly backgroundSystemMaterial?: uiMaterial.Material-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

