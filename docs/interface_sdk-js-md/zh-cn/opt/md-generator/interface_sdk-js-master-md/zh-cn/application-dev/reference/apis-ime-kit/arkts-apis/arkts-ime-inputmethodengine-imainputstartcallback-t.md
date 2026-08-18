# IMAInputStartCallback

```TypeScript
export type IMAInputStartCallback = (kbController: KeyboardController, inputClient: InputClient) => void
```

输入法绑定成功事件的回调函数类型，用于定义inputStart事件触发时执行的回调函数格式。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputMethodEngine-export type IMAInputStartCallback = (kbController: KeyboardController, inputClient: InputClient) => void--><!--Device-inputMethodEngine-export type IMAInputStartCallback = (kbController: KeyboardController, inputClient: InputClient) => void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| kbController | [KeyboardController](../../apis-input-kit/arkts-apis/arkts-input-inputeventclient-keyboardcontroller-i.md) | 是 |
| inputClient | [InputClient](arkts-ime-inputmethodengine-inputclient-i.md) | 是 |
