# ISinglePropertyChangeSubscriber(System API) (System API)

Inherits from IPropertySubscriber. Represents a subscriber that subscribes to changes in a property value.

**Inheritance/Implementation:** ISinglePropertyChangeSubscriber extends IPropertySubscriber

**Since:** 7

<!--Device-unnamed-interface ISinglePropertyChangeSubscriber--><!--Device-unnamed-interface ISinglePropertyChangeSubscriber-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## hasChanged

```TypeScript
hasChanged(newValue: T): void
```

Notifies subscribers that the property value has changed.

**Since:** 7

<!--Device-ISinglePropertyChangeSubscriber-hasChanged(newValue: T): void--><!--Device-ISinglePropertyChangeSubscriber-hasChanged(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newValue | T | Yes |
