# IMAInputStartCallback

```TypeScript
export type IMAInputStartCallback = (kbController: KeyboardController, inputClient: InputClient) => void
```

输入法绑定成功事件的回调函数类型，用于定义inputStart事件触发时执行的回调函数格式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethodEngine-export type IMAInputStartCallback = (kbController: KeyboardController, inputClient: InputClient) => void--><!--Device-inputMethodEngine-export type IMAInputStartCallback = (kbController: KeyboardController, inputClient: InputClient) => void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| kbController | [KeyboardController](../../apis-input-kit/arkts-apis/arkts-input-inputeventclient-keyboardcontroller-i.md) | Yes | 回调函数，返回输入法操作相关实例。 |
| inputClient | [InputClient](arkts-ime-inputmethodengine-inputclient-i.md) | Yes | 输入法操作相关实例。 |

