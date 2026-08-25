# IMAInputStartCallback

```TypeScript
export type IMAInputStartCallback = (kbController: KeyboardController, inputClient: InputClient) => void
```

The callback of 'inputStart' event.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| kbController | [KeyboardController](../../apis-input-kit/arkts-apis/arkts-input-inputeventclient-keyboardcontroller-i.md) | Yes |
| inputClient | [InputClient](arkts-ime-inputmethodengine-inputclient-i.md) | Yes |
