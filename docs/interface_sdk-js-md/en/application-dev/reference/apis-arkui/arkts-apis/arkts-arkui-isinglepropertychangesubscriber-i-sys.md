# ISinglePropertyChangeSubscriber (System API)

Inherits from [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md#IPropertySubscriber-(System-API)). Represents a subscriber that subscribes to changes in a property value.

**Inheritance/Implementation:** ISinglePropertyChangeSubscriber extends [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md#IPropertySubscriber-(System-API))

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

<!--Device-unnamed-interface ISinglePropertyChangeSubscriber--><!--Device-unnamed-interface ISinglePropertyChangeSubscriber-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## hasChanged

```TypeScript
hasChanged(newValue: T): void
```

Notifies subscribers that the property value has changed.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

<!--Device-ISinglePropertyChangeSubscriber-hasChanged(newValue: T): void--><!--Device-ISinglePropertyChangeSubscriber-hasChanged(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | Instance of the T type. |

