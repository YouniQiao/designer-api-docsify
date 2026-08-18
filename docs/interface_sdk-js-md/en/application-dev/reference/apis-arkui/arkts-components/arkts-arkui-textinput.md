# TextInput

The **TextInput** component provides single-line text input. > **NOTE** > > This component supports plain text only. For rich text, use the RichEditor component.

## Child Components Not supported

## TextInput

```TypeScript
TextInput(value?: TextInputOptions)
```

Defines the constructor of TextInput.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputInterface-(value?: TextInputOptions): TextInputAttribute--><!--Device-TextInputInterface-(value?: TextInputOptions): TextInputAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TextInputOptions](arkts-arkui-textinputoptions-i.md) | No | Parameters of the **TextInput** component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [PasswordIcon](arkts-arkui-passwordicon-i.md) | PasswordIcon object. |
| [SubmitEvent](arkts-arkui-submitevent-i.md) | Defines the user submission event. |
| [TextInputOptions](arkts-arkui-textinputoptions-i.md) | **TextInput** initialization parameters. |
| [UnderlineColor](arkts-arkui-underlinecolor-i.md) | Defines the underline color width property. |

### Types

| Name | Description |
| --- | --- |
| [OnContentScrollCallback](arkts-arkui-oncontentscrollcallback-t.md) | Defines the callback for text content scrolling. |
| [OnPasteCallback](arkts-arkui-onpastecallback-t.md) | Defines the callback used to return the pasted text content. |
| [OnSubmitCallback](arkts-arkui-onsubmitcallback-t.md) | Defines the callback for submission. |
| [OnTextSelectionChangeCallback](arkts-arkui-ontextselectionchangecallback-t.md) | Defines the callback for text selection changes or caret position changes. |

### Enums

| Name | Description |
| --- | --- |
| [ContentType](arkts-arkui-contenttype-e.md) | Enumerates the content types for autofill. |
| [EnterKeyType](arkts-arkui-enterkeytype-e.md) | Type of the Enter key. |
| [InputType](arkts-arkui-inputtype-e.md) | Sets the single-line text box type. |
| [TextInputStyle](arkts-arkui-textinputstyle-e.md) | Text input style. |

