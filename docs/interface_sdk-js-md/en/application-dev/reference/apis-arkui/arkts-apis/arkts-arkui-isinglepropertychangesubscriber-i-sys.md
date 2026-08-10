# ISinglePropertyChangeSubscriber (System API)

继承自[IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md)。用于订阅单个属性值的变化，当被订阅的属性发生变化时接收通知。

**Inheritance/Implementation:** ISinglePropertyChangeSubscriber extends [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-interface ISinglePropertyChangeSubscriber<T> extends IPropertySubscriber--><!--Device-unnamed-interface ISinglePropertyChangeSubscriber<T> extends IPropertySubscriber-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## hasChanged

```TypeScript
hasChanged(newValue: T): void
```

变化时调用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ISinglePropertyChangeSubscriber-hasChanged(newValue: T): void--><!--Device-ISinglePropertyChangeSubscriber-hasChanged(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | 更改后的新值。 |

