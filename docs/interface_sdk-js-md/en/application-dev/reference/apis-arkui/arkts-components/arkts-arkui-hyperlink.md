# Hyperlink

超链接组件，支持文本和图片两种展示形式，在组件宽高范围内点击可实现跳转到指定网页。适用于应用内打开外部网页链接的场景，该组件仅支持与系统浏览器配合使用。

> **说明：**
>
> - 该组件仅支持与系统浏览器配合使用。

## 需要权限

跳转到目标网页需要使用网络时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](docroot://security/AccessToken/declare-permissions.md)。

## 子组件

可以包含[Image]{@link ./image}子组件。

## Hyperlink

```TypeScript
Hyperlink(address: string | Resource, content?: string | Resource)
```

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HyperlinkInterface-(address: string | Resource, content?: string | Resource): HyperlinkAttribute--><!--Device-HyperlinkInterface-(address: string | Resource, content?: string | Resource): HyperlinkAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| address | string \| Resource | Yes | Hyperlink组件跳转的网页地址。 |
| content | string \| Resource | No | Hyperlink组件中超链接显示文本。 <br>默认值：''。若不传该参数且组件内无子组件时，默认显示address参数值。 <br>**说明：** <br>组件内有子组件时，不显示超链接文本。 |

## Summary

