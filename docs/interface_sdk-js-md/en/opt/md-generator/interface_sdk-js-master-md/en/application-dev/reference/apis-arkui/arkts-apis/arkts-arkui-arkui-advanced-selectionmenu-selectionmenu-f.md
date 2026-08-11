# SelectionMenu

## Modules to Import

```TypeScript
import { EditorMenuOptions, SelectionMenuOptions, EditorEventInfo, SelectionMenu, ExpandedMenuOptions } from 'kits/@kit.ArkUI';
```

## SelectionMenu

```TypeScript
export declare function SelectionMenu(options: SelectionMenuOptions): void
```

Defines a **SelectionMenu** component. When the input parameter is empty, both the component and its content area have a zero size, making the component invisible. For example, when a **SelectionMenu** component activated via right  
-click is bound to a [RichEditor](../../apis-arkui/arkts-components/arkts-arkui-rich_editor-i) component using  
[bindSelectionMenu](RichEditorAttribute#bindSelectionMenu), it will not be displayed when the **RichEditor**component receives a right-click event.

**Since:** 11

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-export declare function SelectionMenu(options: SelectionMenuOptions): void--><!--Device-unnamed-export declare function SelectionMenu(options: SelectionMenuOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SelectionMenuOptions](arkts-arkui-arkui-advanced-selectionmenu-selectionmenuoptions-i.md) | Yes |
