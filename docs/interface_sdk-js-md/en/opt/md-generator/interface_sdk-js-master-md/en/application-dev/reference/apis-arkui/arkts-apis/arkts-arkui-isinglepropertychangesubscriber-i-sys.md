# ISinglePropertyChangeSubscriber (System API)

Inherits from [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md). Represents a subscriber that subscribes to changes in a property value.

**Inheritance/Implementation:** ISinglePropertyChangeSubscriber extends [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md)

**Since:** 7

<!--Device-unnamed-interface ISinglePropertyChangeSubscriber<T> extends IPropertySubscriber--><!--Device-unnamed-interface ISinglePropertyChangeSubscriber<T> extends IPropertySubscriber-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

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
