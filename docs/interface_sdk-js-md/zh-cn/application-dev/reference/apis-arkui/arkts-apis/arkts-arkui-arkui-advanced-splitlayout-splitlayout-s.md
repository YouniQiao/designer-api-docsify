# SplitLayout

SplitLayout组件提供了常用的页面布局样式，主要用于展示图片、标题和内容容器的组合布局，适用于需要自适应不同屏幕尺寸的分栏展示场景（如详情页、设置页等）。支持自适应不同屏幕宽度（小于等于600vp、大于600vp且小于等于84 0vp、大于840vp三种布局），解决了在不同尺寸设备上需要展示不同布局样式的需求，提升页面适配性和用户体验。

> **说明：**
> 
> - 该组件从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> 
> - 该组件仅可在Stage模型下使用。
> 
> - SplitLayout不支持设置通用属性和通用事件。如果设
> 置，编译工具链会额外生成__Common__节点，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到SplitLayout本身，导致设置的属性或事件不生效。

**起始版本：** 10

<!--Device-unnamed-export declare struct SplitLayout--><!--Device-unnamed-export declare struct SplitLayout-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { SplitLayout } from '@kit.ArkUI';
```

## container

```TypeScript
@BuilderParam
  container: () => void
```

容器内组件，用于在布局下方区域承载自定义组件内容，无返回值。

**类型：** () =&gt; void

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SplitLayout-@BuilderParam  container: () => void--><!--Device-SplitLayout-@BuilderParam  container: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## mainImage

```TypeScript
@State
  mainImage: ResourceStr
```

主图片资源，显示在布局上方区域，支持png、jpg、svg等常见图片格式。

**类型：** ResourceStr

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SplitLayout-@State  mainImage: ResourceStr--><!--Device-SplitLayout-@State  mainImage: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## primaryText

```TypeScript
@Prop
  primaryText: ResourceStr
```

主标题内容，无长度限制。显示在布局的标题区域。

**类型：** ResourceStr

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SplitLayout-@Prop  primaryText: ResourceStr--><!--Device-SplitLayout-@Prop  primaryText: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## secondaryText

```TypeScript
@Prop
  secondaryText?: ResourceStr
```

副标题内容，无长度限制。当需要在标题下方显示副标题时传入，不传入时不显示副标题。

**类型：** ResourceStr

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SplitLayout-@Prop  secondaryText?: ResourceStr--><!--Device-SplitLayout-@Prop  secondaryText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## tertiaryText

```TypeScript
@Prop
  tertiaryText?: ResourceStr
```

辅助文本，无长度限制。显示在副标题下方区域，当需要显示辅助文本时传入，不传入时不显示辅助文本。

**类型：** ResourceStr

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SplitLayout-@Prop  tertiaryText?: ResourceStr--><!--Device-SplitLayout-@Prop  tertiaryText?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

