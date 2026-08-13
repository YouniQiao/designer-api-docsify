# Hyperlink

超链接组件，支持文本和图片两种展示形式，在组件宽高范围内点击可实现跳转到指定网页。适用于应用内打开外部网页链接的场景，该组件仅支持与系统浏览器配合使用。 > **说明：** > > - 该组件仅支持与系统浏览器配合使用。

## 需要权限 跳转到目标网页需要使用网络时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](../../../security/AccessToken/declare-permissions.md)。 ###### 子组件 可以包含Image子组件。

## Hyperlink

```TypeScript
Hyperlink(address: string | Resource, content?: string | Resource)
```

**起始版本：** 7

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-HyperlinkInterface-(address: string | Resource, content?: string | Resource): HyperlinkAttribute--><!--Device-HyperlinkInterface-(address: string | Resource, content?: string | Resource): HyperlinkAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| address | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
| content | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 否 |

## 汇总
