# InputElement

The &lt;input&gt; component provides an interactive interface to receive user input, which is displayed in a single line by default.@extends Element @interface InputElement

**Inheritance/Implementation:** InputElement extends [Element](arkts-arkui-viewmodel-element-i.md)

**Since:** 4

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delete

```TypeScript
delete(): void
```

Deletes the previous character at the cursor position.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## focus

```TypeScript
focus(param: { focus: boolean }): void
```

Obtains or loses the focus of a component. When the component type is set to text, email, date, time, number, or password, the input method can be displayed or collapsed.

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | { focus: boolean } | Yes |

## showError

```TypeScript
showError(param: { error: string }): void
```

Displays the error message. This attribute is available when the component type is set to text, email, date, time, number, or password.

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | { error: string } | Yes |
