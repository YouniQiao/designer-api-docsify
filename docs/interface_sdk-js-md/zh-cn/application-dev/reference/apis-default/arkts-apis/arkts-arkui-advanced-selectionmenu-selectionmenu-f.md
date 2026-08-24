# SelectionMenu

## 导入模块

```TypeScript
```

## SelectionMenu

```TypeScript
@Builder
export declare function SelectionMenu(options: SelectionMenuOptions): void
```

入参为空时，文本选择菜单组件SelectionMenu内容区大小及组件大小为零。表现例如，富文本组件 RichEditor使用 bindSelectionMenu接口绑定一 个SelectionMenu的右键菜单，则右键富文本组件区域时无任何菜单弹出。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-@Builderexport declare function SelectionMenu(options: SelectionMenuOptions): void--><!--Device-unnamed-@Builderexport declare function SelectionMenu(options: SelectionMenuOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SelectionMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-selectionmenu-selectionmenuoptions-i.md) | 是 | 文本选择菜单可选项。 |

