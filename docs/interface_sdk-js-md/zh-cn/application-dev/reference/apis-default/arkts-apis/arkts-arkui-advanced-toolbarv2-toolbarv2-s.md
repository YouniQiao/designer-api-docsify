# ToolBarV2

工具栏用于展示针对当前界面内容的操作选项，在界面底部显示，适用于需要为用户提供快速操作入口的场景。底部最多显示5个入口，超过则收纳入“更多”子项中，在最右侧显示。适用于需要对当前页面内容进行快捷操作的场景，可帮助用户快速访问常用功能， 提升操作效率。

该组件基于[状态管理（V2）](../../../ui/state-management/arkts-state-management-overview.md#状态管理v2)实现，相较于 [状态管理（V1）](../../../ui/state-management/arkts-state-management-overview.md#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组 件层级。借助状态管理（V2），开发者可以通过该组件更灵活地控制工具栏的数据和状态，实现更高效的用户界面刷新。

> **说明：**
> 
> - 该组件仅可在Stage模型下使用。
> 
> - 如果ToolBarV2设置通用属性和通用事件，编译工具链会 &gt; 额外生成节点__Common__，并将通用属性或通用事件挂载在__Common__上，而不是直接应用到ToolBarV2本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议ToolBarV2设置通用属性和 &gt; 通用事件。
> 
> - 当系统切换深浅色模式时，工具栏背景色不会自动跟随切换。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare struct ToolBarV2--><!--Device-unnamed-export declare struct ToolBarV2-End-->

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

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2-@Builder  build(): void--><!--Device-ToolBarV2-@Builder  build(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## activatedIndex

```TypeScript
@Param
  activatedIndex?: int
```

Define toolbarV2 activate item index, default is -1.

**类型：** int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2-@Param  activatedIndex?: int--><!--Device-ToolBarV2-@Param  activatedIndex?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dividerModifier

```TypeScript
@Param
  dividerModifier?: DividerModifier
```

Define divider Modifier.

**类型：** DividerModifier

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2-@Param  dividerModifier?: DividerModifier--><!--Device-ToolBarV2-@Param  dividerModifier?: DividerModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## toolBarList

```TypeScript
@Require
  @Param
  toolBarList: ToolBarV2Item[]
```

Define toolbarV2 item list.

**类型：** [ToolBarV2Item](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbarv2-toolbarv2item-c.md)[]

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2-@Require  @Param  toolBarList: ToolBarV2Item[]--><!--Device-ToolBarV2-@Require  @Param  toolBarList: ToolBarV2Item[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## toolBarModifier

```TypeScript
@Param
  toolBarModifier?: ToolBarV2Modifier
```

Define toolbarV2 modifier.

**类型：** [ToolBarV2Modifier](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbarv2-toolbarv2modifier-c.md)

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolBarV2-@Param  toolBarModifier?: ToolBarV2Modifier--><!--Device-ToolBarV2-@Param  toolBarModifier?: ToolBarV2Modifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

