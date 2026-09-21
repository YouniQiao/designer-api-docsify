# SelectionContainer

Defines SelectionContainer component.

## SelectionContainer

```TypeScript
SelectionContainer(value?: SelectionContainerOptions)
```

Defines the constructor of SelectionContainer.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SelectionContainerOptions](arkts-arkui-selectioncontainer-comp-selectioncontaineroptions-i.md) | No | Initialization options of the component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [SelectionContainerEditMenuOptions](arkts-arkui-selectioncontainer-comp-selectioncontainereditmenuoptions-i.md) | Defines custom edit menu options for SelectionContainer. |
| [SelectionContainerMenuOptions](arkts-arkui-selectioncontainer-comp-selectioncontainermenuoptions-i.md) | Defines selection menu options for SelectionContainer. |
| [SelectionContainerOptions](arkts-arkui-selectioncontainer-comp-selectioncontaineroptions-i.md) | Describes the initialization options of the SelectionContainer component. |

### Types

| Name | Description |
| --- | --- |
| [OnMenuItemClickWithTextCallback](arkts-arkui-selectioncontainer-comp-onmenuitemclickwithtextcallback-t.md) | Invoke upon clicking an item, capable of intercepting the default system menu execution behavior. |

### Enums

| Name | Description |
| --- | --- |
| [SelectionContainerTextJoinStyle](arkts-arkui-selectioncontainer-comp-selectioncontainertextjoinstyle-e.md) | Defines text join style for SelectionContainer. |

## Examples

```TypeScript
### Example 1: Selecting Text Across Nodes and Copying the Text

This example demonstrates how to select text across multiple Text components, concatenate the selected text, and handle copy callbacks by using [SelectionContainer](#interfaces), [copyOption](#copyoption), [textJoinStyle](arkts-arkui-selectioncontainer-comp-attribute.md#textjoinstyle), [onTextSelectionChange](#ontextselectionchange), [onWillCopy](#onwillcopy), and [onCopy](#oncopy).

Since API version 26.0.0, the SelectionContainer component and APIs such as copyOption are added.


```

```TypeScript
### Example 2: Binding a Custom Selection Menu

This example demonstrates how to bind a custom menu when selecting text across nodes through [bindSelectionMenu](#bindselectionmenu).

Since API version 26.0.0, the bindSelectionMenu attribute is added.


```

```TypeScript
### Example 3: Extending Menu Options

This example uses [editMenuOptions](#editmenuoptions) to remove the translation and search menu items from the system menu and add five custom menu items. It also demonstrates, in the [onMenuItemClick](arkts-arkui-selectioncontainer-comp-onmenuitemclickwithtextcallback-t.md) callback, the difference between intercepting the system copy operation (returning true) and not intercepting the select-all operation (returning false).

The editMenuOptions attribute is added since API version 26.0.0.


```

```TypeScript
### Example 4: Closing the Selection Menu and Clearing Text Selection Through the Controllers

This example demonstrates how to close the selection menu and clear the text selection by passing [SelectionContainerController](arkts-arkui-selectioncontainer-comp-selectioncontainercontroller-c.md) through [SelectionContainer](#interfaces) and calling [closeSelectionMenu](#closeselectionmenu) and [clearTextSelection](arkts-arkui-selectioncontainer-comp-selectioncontainercontroller-c.md#cleartextselection).

Since API version 26.0.0, the [SelectionContainerController](arkts-arkui-selectioncontainer-comp-selectioncontainercontroller-c.md) and [SelectionContainerOptions](arkts-arkui-selectioncontainer-comp-selectioncontaineroptions-i.md) APIs are added.
```
