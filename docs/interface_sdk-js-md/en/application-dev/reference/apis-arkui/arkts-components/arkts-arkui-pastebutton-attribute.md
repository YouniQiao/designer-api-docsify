# PasteButton properties/events

This component can only inherit the universal attributes of security components.

Only the following events are supported.

**Inheritance/Implementation:** PasteButtonAttribute extends SecurityComponentMethod<PasteButtonAttribute>

**Since:** 10

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## onClick

```TypeScript
onClick(event: PasteButtonCallback)
```

Triggered when the paste button is clicked, returning the authorization result. Upon successful authorization, the application obtains temporary permission to read clipboard content.

> **NOTE：**
> - You may want to learn the
> [restrictions on security component styles](../../../security/AccessToken/security-component-overview.md#constraints)
> to avoid authorization failures caused by incompliant styles.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [PasteButtonCallback](arkts-arkui-pastebuttoncallback-t.md) | Yes |
