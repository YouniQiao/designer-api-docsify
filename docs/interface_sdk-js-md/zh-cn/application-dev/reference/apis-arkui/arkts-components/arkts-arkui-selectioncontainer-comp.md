# SelectionContainer

SelectionContainer组件用于为多个文本节点提供跨节点文本选中、复制及菜单扩展能力，支持统一配置选中文本的手柄颜色和底板颜色，支持灵活的文本拼接策略，支持自定义选择菜单和扩展菜单选项。适用于需要跨多个Text组件实现文本连续选中、统一复制、样式自定义及菜单扩展的场景，解决了多Text组件场景下文本选择体验割裂的问题，提升了用户在复杂文本布局中的交互体验。

> **说明：** > > - 本组件中选中文本相关回调返回的文本内容，按照[Text](arkts-arkui-text-comp.md#text)组件的从上到下显示顺序进行拼接。 > > - 本组件默认布局走[Stack](arkts-arkui-stack-comp.md#stack)，如有其他容器布局需求请在SelectionContainer内放置一个容器组件。 > > - SelectionContainer内跨节点选中文本时不显示放大镜，也不支持[getMagnifier](../arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md#getmagnifier)主动设置放大镜。 > > - 仅Text组件中的文本内容参与跨节点选中与文本拼接。

## 子组件

可以包含子组件。

## SelectionContainer

```TypeScript
SelectionContainer(value?: SelectionContainerOptions)
```

定义SelectionContainer的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SelectionContainerOptions](arkts-arkui-selectioncontainer-comp-selectioncontaineroptions-i.md) | 否 | 组件的初始化选项。 |

## 汇总

### 接口

| 名称 | 说明 |
| --- | --- |
| [SelectionContainerEditMenuOptions](arkts-arkui-selectioncontainer-comp-selectioncontainereditmenuoptions-i.md) | SelectionContainer自定义编辑菜单选项。 |
| [SelectionContainerMenuOptions](arkts-arkui-selectioncontainer-comp-selectioncontainermenuoptions-i.md) | 配置选择菜单中的选项。 |
| [SelectionContainerOptions](arkts-arkui-selectioncontainer-comp-selectioncontaineroptions-i.md) | 组件初始化配置项。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [OnMenuItemClickWithTextCallback](arkts-arkui-selectioncontainer-comp-onmenuitemclickwithtextcallback-t.md) | 点击菜单项时触发，可拦截系统默认菜单项（如复制、粘贴菜单项）的执行行为。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [SelectionContainerTextJoinStyle](arkts-arkui-selectioncontainer-comp-selectioncontainertextjoinstyle-e.md) | 文本聚合拼接方式。 |

## 示例

```TypeScript
### 示例1（跨节点选中文本并复制）

该示例通过[SelectionContainer](#接口)、[copyOption](#copyoption)、[textJoinStyle](arkts-arkui-selectioncontainer-comp-attribute.md#textjoinstyle)、[onTextSelectionChange](#ontextselectionchange)、[onWillCopy](#onwillcopy)、[onCopy](#oncopy)接口展示跨多个Text组件选中文本、拼接选中文本并处理复制回调的能力。

从API版本26.0.0开始，新增SelectionContainer组件和copyOption等接口。


```

```TypeScript
### 示例2（绑定自定义选择菜单）

该示例通过[bindSelectionMenu](#bindselectionmenu)接口实现了跨节点选中文本时绑定自定义菜单的功能。

从API版本26.0.0开始，新增bindSelectionMenu属性。


```

```TypeScript
### 示例3（扩展菜单选项）

该示例通过[editMenuOptions](#editmenuoptions)接口实现了去除系统菜单中的翻译和搜索菜单项，并添加5个自定义菜单项的功能。同时在[onMenuItemClick](arkts-arkui-selectioncontainer-comp-onmenuitemclickwithtextcallback-t.md)回调中展示拦截系统复制操作（return true）和不拦截全选操作（return false）的差异。

从API版本26.0.0开始，新增editMenuOptions属性。


```

```TypeScript
### 示例4（通过控制器关闭选择菜单与清除文本选中）

该示例通过[SelectionContainer](#接口)传入[SelectionContainerController](arkts-arkui-selectioncontainer-comp-selectioncontainercontroller-c.md)，调用[closeSelectionMenu](#closeselectionmenu)和[clearTextSelection](arkts-arkui-selectioncontainer-comp-selectioncontainercontroller-c.md#cleartextselection)接口展示关闭选择菜单和清除选中文本的能力。

从API版本26.0.0开始，新增[SelectionContainerController](arkts-arkui-selectioncontainer-comp-selectioncontainercontroller-c.md)和[SelectionContainerOptions](arkts-arkui-selectioncontainer-comp-selectioncontaineroptions-i.md)接口。
```
