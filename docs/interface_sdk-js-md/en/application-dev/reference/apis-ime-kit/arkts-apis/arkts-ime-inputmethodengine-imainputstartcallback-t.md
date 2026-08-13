# IMAInputStartCallback

```TypeScript
export type IMAInputStartCallback = (kbController: KeyboardController, inputClient: InputClient) => void
```

The callback of 'inputStart' event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethodEngine-export type IMAInputStartCallback = (kbController: KeyboardController, inputClient: InputClient) => void--><!--Device-inputMethodEngine-export type IMAInputStartCallback = (kbController: KeyboardController, inputClient: InputClient) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| kbController | KeyboardController | Yes | keyboard controller. |
| inputClient | [InputClient](arkts-ime-inputmethodengine-inputclient-i.md) | Yes | input client. |

