# SyncedPropertyTwoWay (System API)

Inherits from [SubscribedAbstractProperty&lt;T&gt;](arkts-arkui-subscribedabstractproperty-c.md#SubscribedAbstractProperty-(System-API)). Represents a property with two-way synchronization.

**Inheritance/Implementation:** SyncedPropertyTwoWay extends SubscribedAbstractProperty<T> and implements ISinglePropertyChangeSubscriber<T>

**Since:** 7

**Deprecated since:** -1

<!--Device-unnamed-declare class SyncedPropertyTwoWay--><!--Device-unnamed-declare class SyncedPropertyTwoWay-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## aboutToBeDeleted

```TypeScript
aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void
```

Called when the object is about to be destroyed.

**Since:** 7

**Deprecated since:** -1

<!--Device-SyncedPropertyTwoWay-aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void--><!--Device-SyncedPropertyTwoWay-aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| unsubscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No |

## constructor

```TypeScript
constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)
```

Constructor.

**Since:** 7

**Deprecated since:** -1

<!--Device-SyncedPropertyTwoWay-constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)--><!--Device-SyncedPropertyTwoWay-constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; | Yes |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No |
| info | string | No |

## get

```TypeScript
get(): T
```

Obtains the current value of the property.

**Since:** 7

**Deprecated since:** -1

<!--Device-SyncedPropertyTwoWay-get(): T--><!--Device-SyncedPropertyTwoWay-get(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## hasChanged

```TypeScript
hasChanged(newValue: T): void
```

Notifies subscribers that the property value has changed.

**Since:** 7

**Deprecated since:** -1

<!--Device-SyncedPropertyTwoWay-hasChanged(newValue: T): void--><!--Device-SyncedPropertyTwoWay-hasChanged(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newValue | T | Yes |

## set

```TypeScript
set(newValue: T): void
```

Sets a new value for the property.

**Since:** 7

**Deprecated since:** -1

<!--Device-SyncedPropertyTwoWay-set(newValue: T): void--><!--Device-SyncedPropertyTwoWay-set(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newValue | T | Yes |

## source_

```TypeScript
private source_
```

Data source for the two-way synchronized property.

**Since:** 7

**Deprecated since:** -1

<!--Device-SyncedPropertyTwoWay-private source_--><!--Device-SyncedPropertyTwoWay-private source_-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.
