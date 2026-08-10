# @ohos.arkui.components.SelectionContainer

## Modules to Import

```TypeScript
import { SelectionContainerInstance, SelectionContainer, OnMenuItemClickWithTextCallback, SelectionContainerOptions, SelectionContainerAttribute, SelectionContainerEditMenuOptions, SelectionContainerTextJoinStyle, SelectionContainerController, SelectionContainerMenuOptions } from 'kits/@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [SelectionContainer](arkts-arkui-arkui-components-selectioncontainer-selectioncontainer-f.md#selectioncontainer) | 创建一个SelectionContainer组件。需要在组件属性设置开始时调用setSelectionContainerOptions，并在组件属性设置结束时调用applyAttributesFinish。 |

### Interfaces

| Name | Description |
| --- | --- |
| [SelectionContainerAttribute](arkts-arkui-arkui-components-selectioncontainer-selectioncontainerattribute-i.md) | 支持[通用属性](../../../reference/apis-arkui/arkui-ts/ts-component-general-attributes.md)。 |
| [SelectionContainerEditMenuOptions](arkts-arkui-arkui-components-selectioncontainer-selectioncontainereditmenuoptions-i.md) | SelectionContainer自定义编辑菜单选项。 |
| [SelectionContainerMenuOptions](arkts-arkui-arkui-components-selectioncontainer-selectioncontainermenuoptions-i.md) | 配置选择菜单中的选项。 |

### Enums

| Name | Description |
| --- | --- |
| [SelectionContainerTextJoinStyle](arkts-arkui-arkui-components-selectioncontainer-selectioncontainertextjoinstyle-e.md) | 文本聚合拼接方式。  \| 名称 \| 值 \| 说明 \|  \| ---- \| -- \| ---- \|  \| NEWLINE \| 0 \| 不同文本节点之间使用换行符`\n`拼接。 \|  \| DIRECT \| 1 \| 不同文本节点之间直接拼接，不添加分隔符。 \| |

### Types

| Name | Description |
| --- | --- |
| [OnMenuItemClickWithTextCallback](arkts-arkui-onmenuitemclickwithtextcallback-t.md) | 点击菜单项时触发，可拦截系统默认菜单项（如复制、粘贴菜单项）的执行行为。 |

