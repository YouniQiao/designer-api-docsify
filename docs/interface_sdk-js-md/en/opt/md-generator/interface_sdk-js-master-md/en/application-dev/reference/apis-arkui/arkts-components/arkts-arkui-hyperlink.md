# Hyperlink

The **Hyperlink** component implements a link from a location in the component to another location.

> **NOTE**
>
> - This component must be used with the system browser.

## Required Permissions

If Internet access is required, you must apply for the **ohos.permission.INTERNET** permission. For details about how to apply for a permission, see [Declaring Permissions](docroot://security/AccessToken/declare-permissions.md).

## Child Components

This component can contain the [Image]{@link ./image} child component.

## Hyperlink

```TypeScript
Hyperlink(address: string | Resource, content?: string | Resource)
```

Defines the constructor of Hyperlink.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-HyperlinkInterface-(address: string | Resource, content?: string | Resource): HyperlinkAttribute--><!--Device-HyperlinkInterface-(address: string | Resource, content?: string | Resource): HyperlinkAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| address | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |
| content | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | No |

## Summary
