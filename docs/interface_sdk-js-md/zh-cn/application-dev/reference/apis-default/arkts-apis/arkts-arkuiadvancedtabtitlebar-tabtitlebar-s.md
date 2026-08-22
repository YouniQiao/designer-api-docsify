# TabTitleBar

TabTitleBar是页签型标题栏组件，支持页签列表与关联内容的联动切换，并可配置右侧菜单项。适用于需要通过页签切换页面内容的场景，如顶部导航栏等。该组件通过页签和菜单项的灵活配置，可满足不同的交互需求。仅支持一级页面的页签切换。

> **说明：**
> 
> - 该组件仅可在Stage模型下使用。
> 
> - 设置TabTitleBar的通用属性或通用事件时，编译工具
> 链会在__Common__节点上挂载而非直接应用到组件本身，可能导致设置不生效或不符合预期，因此不建议设置。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare struct TabTitleBar--><!--Device-unnamed-export declare struct TabTitleBar-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

The method to build component.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabTitleBar-@Builder  build(): void--><!--Device-TabTitleBar-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## menuItems

```TypeScript
menuItems?: Array<TabTitleBarMenuItem>
```

右侧菜单项目列表。若不传，则不显示右侧菜单项。

**类型：** Array&lt;[TabTitleBarMenuItem](arkts-arkuiadvancedtabtitlebar-tabtitlebarmenuitem-c.md)&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabTitleBar-menuItems?: Array<TabTitleBarMenuItem>--><!--Device-TabTitleBar-menuItems?: Array<TabTitleBarMenuItem>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## swiperContent

```TypeScript
@BuilderParam
  swiperContent: () => void
```

页签列表关联的页面内容构造器。

**类型：** () =&gt; void

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabTitleBar-@BuilderParam  swiperContent: () => void--><!--Device-TabTitleBar-@BuilderParam  swiperContent: () => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## tabItems

```TypeScript
tabItems: Array<TabTitleBarTabItem>
```

左侧页签项目列表。

**类型：** Array&lt;[TabTitleBarTabItem](arkts-arkuiadvancedtabtitlebar-tabtitlebartabitem-c.md)&gt;

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TabTitleBar-tabItems: Array<TabTitleBarTabItem>--><!--Device-TabTitleBar-tabItems: Array<TabTitleBarTabItem>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

