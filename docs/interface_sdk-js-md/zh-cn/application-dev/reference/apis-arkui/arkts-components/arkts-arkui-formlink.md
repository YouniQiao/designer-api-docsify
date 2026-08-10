# FormLink

The **FormLink** component is provided for interactions between static widgets and widget providers. It supports 
three types of events: router, message, and call.

> **NOTE**
>
> - This component is supported since API version 10. Updates will be marked with a superscript to indicate their 
> earliest API version.
>
> - This component can be used only in static widgets.
>
> - This document covers static widget development only. For comprehensive widget development guidance, see the 
> [widget development guide](docroot://form/formkit-overview.md).

## FormLink

```TypeScript
FormLink(options: FormLinkOptions)
```

Init FormLink component with options.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-FormLinkInterface-(options: FormLinkOptions): FormLinkAttribute--><!--Device-FormLinkInterface-(options: FormLinkOptions): FormLinkAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [FormLinkOptions](arkts-arkui-formlinkoptions-i.md) | 是 | Widget information. |

## 汇总

- [FormLinkOptions](arkts-arkui-formlink-formlinkoptions-i.md)
