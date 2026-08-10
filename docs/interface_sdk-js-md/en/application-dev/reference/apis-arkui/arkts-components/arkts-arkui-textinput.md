# TextInput

单行文本输入框组件，用于接收用户的单行文本输入。支持多种输入类型（如文本、密码、邮箱、数字等）、自定义样式（字体、颜色、下划线、装饰线等）、输入过滤、密码输入模式、自动填充等功能，适用于登录注册、搜索、表单填写等多种场景。能够解决文本
输入验证、格式化、安全输入等常见需求，简化开发流程、提升用户体验并增强数据安全性。

> **说明：**
>
> 该组件仅支持单文本样式，若需实现富文本样式，建议使用[RichEditor]{@link ./rich_editor}组件。

## 子组件

无

## TextInput

```TypeScript
TextInput(value?: TextInputOptions)
```

定义单行文本输入组件构造函数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextInputInterface-(value?: TextInputOptions): TextInputAttribute--><!--Device-TextInputInterface-(value?: TextInputOptions): TextInputAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TextInputOptions](arkts-arkui-textinputoptions-i.md) | No | TextInput组件参数。默认值undefined。不设置该参数时，输入框初始化为空。 |

## Summary

- [PasswordIcon](arkts-arkui-textinput-passwordicon-i.md)
- [SubmitEvent](arkts-arkui-textinput-submitevent-i.md)
- [TextInputOptions](arkts-arkui-textinput-textinputoptions-i.md)
- [UnderlineColor](arkts-arkui-textinput-underlinecolor-i.md)
- [OnContentScrollCallback](arkts-arkui-textinput-oncontentscrollcallback-t.md)
- [OnPasteCallback](arkts-arkui-textinput-onpastecallback-t.md)
- [OnSubmitCallback](arkts-arkui-textinput-onsubmitcallback-t.md)
- [OnTextSelectionChangeCallback](arkts-arkui-textinput-ontextselectionchangecallback-t.md)
- [ContentType](arkts-arkui-textinput-contenttype-e.md)
- [EnterKeyType](arkts-arkui-textinput-enterkeytype-e.md)
- [InputType](arkts-arkui-textinput-inputtype-e.md)
- [TextInputStyle](arkts-arkui-textinput-textinputstyle-e.md)
