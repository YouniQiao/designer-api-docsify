# SubscribedAbstractProperty

Represents a synchronized property from [AppStorage](../../../ui/state-management/arkts-appstorage.md) or  
[LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 9

<!--Device-unnamed-declare abstract class SubscribedAbstractProperty<T>--><!--Device-unnamed-declare abstract class SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToBeDeleted

```TypeScript
abstract aboutToBeDeleted(): void
```

Cancels the synchronization relationship between the [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)instance and [AppStorage](../../../ui/state-management/arkts-appstorage.md) or  
[LocalStorage](../../../ui/state-management/arkts-localstorage.md), whether it is a one-way or two-way binding.After **aboutToBeDeleted** is called, the **SubscribedAbstractProperty** instance is invalidated, meaning it can no longer be used to call the [set](arkts-arkui-localstorage-c.md#set) or [get](arkts-arkui-localstorage-c.md#get) API.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SubscribedAbstractProperty-abstract aboutToBeDeleted(): void--><!--Device-SubscribedAbstractProperty-abstract aboutToBeDeleted(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(
    /**
     * Subscriber IPropertySubscriber.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @systemapi
     * @since 7
     * 
     */
    subscribeMe?: IPropertySubscriber,
    /**
     * Subscriber info.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @systemapi
     * @since 7
     * 
     */
    info?: string,
  )
```

Constructor.

**Since:** 7

<!--Device-SubscribedAbstractProperty-constructor(    /**     * Subscriber IPropertySubscriber.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @systemapi     * @since 7     *      */    subscribeMe?: IPropertySubscriber,    /**     * Subscriber info.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @systemapi     * @since 7     *      */    info?: string,  )--><!--Device-SubscribedAbstractProperty-constructor(    /**     * Subscriber IPropertySubscriber.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @systemapi     * @since 7     *      */    subscribeMe?: IPropertySubscriber,    /**     * Subscriber info.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @systemapi     * @since 7     *      */    info?: string,  )-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No |
| [info](#info) | string | No |

## createOneWaySync

```TypeScript
createOneWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyOneWay<T>
```

Creates one-way synchronization.

**Since:** 7

<!--Device-SubscribedAbstractProperty-createOneWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyOneWay<T>--><!--Device-SubscribedAbstractProperty-createOneWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyOneWay<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No |
| [info](#info) | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SyncedPropertyOneWay](arkts-arkui-syncedpropertyoneway-c-sys.md)&lt;T&gt; |

## createTwoWaySync

```TypeScript
createTwoWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyTwoWay<T>
```

Creates two-way synchronization.

**Since:** 7

<!--Device-SubscribedAbstractProperty-createTwoWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyTwoWay<T>--><!--Device-SubscribedAbstractProperty-createTwoWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyTwoWay<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No |
| [info](#info) | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SyncedPropertyTwoWay](arkts-arkui-syncedpropertytwoway-c-sys.md)&lt;T&gt; |

## get

```TypeScript
abstract get(): T
```

Reads the data of the synchronized property from [AppStorage](../../../ui/state-management/arkts-appstorage.md) or  
[LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-SubscribedAbstractProperty-abstract get(): T--><!--Device-SubscribedAbstractProperty-abstract get(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## id

```TypeScript
id(): number
```

Called when the subscriber ID is entered.

**Since:** 7

<!--Device-SubscribedAbstractProperty-id(): number--><!--Device-SubscribedAbstractProperty-id(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## info

```TypeScript
info(): string
```

Property name.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SubscribedAbstractProperty-info(): string--><!--Device-SubscribedAbstractProperty-info(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## notifyHasChanged

```TypeScript
protected notifyHasChanged(newValue: T): void
```

Notifies subscribers that the value has changed.

**Since:** 7

<!--Device-SubscribedAbstractProperty-protected notifyHasChanged(newValue: T): void--><!--Device-SubscribedAbstractProperty-protected notifyHasChanged(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newValue | T | Yes |

## notifyPropertyRead

```TypeScript
protected notifyPropertyRead(): void
```

Notifies subscribers that the property has been read.

**Since:** 7

<!--Device-SubscribedAbstractProperty-protected notifyPropertyRead(): void--><!--Device-SubscribedAbstractProperty-protected notifyPropertyRead(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## numberOfSubscrbers

```TypeScript
numberOfSubscrbers(): number
```

Obtains the number of subscribers.

**Since:** 7

<!--Device-SubscribedAbstractProperty-numberOfSubscrbers(): number--><!--Device-SubscribedAbstractProperty-numberOfSubscrbers(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## set

```TypeScript
abstract set(newValue: T): void
```

Sets the data of the synchronized property in [AppStorage](../../../ui/state-management/arkts-appstorage.md) or  
[LocalStorage](../../../ui/state-management/arkts-localstorage.md). The value of **newValue** must be of the **T**type. Since API version 12, it can be **null** or **undefined**.

> **NOTE：**

> Since API version 12, AppStorage and LocalStorage support the Map, Set, Date types, as well as **null**,
> **undefined**, and union types.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-SubscribedAbstractProperty-abstract set(newValue: T): void--><!--Device-SubscribedAbstractProperty-abstract set(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newValue | T | Yes |

## unlinkSuscriber

```TypeScript
unlinkSuscriber(subscriberId: number): void
```

Removes a subscriber.

**Since:** 7

<!--Device-SubscribedAbstractProperty-unlinkSuscriber(subscriberId: number): void--><!--Device-SubscribedAbstractProperty-unlinkSuscriber(subscriberId: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| subscriberId | number | Yes |

## id_

```TypeScript
private id_
```

Private member variable ID.

**Since:** 7

<!--Device-SubscribedAbstractProperty-private id_--><!--Device-SubscribedAbstractProperty-private id_-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## info_

```TypeScript
private info_?
```

Variable information.

**Since:** 7

<!--Device-SubscribedAbstractProperty-private info_?--><!--Device-SubscribedAbstractProperty-private info_?-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subscribers_

```TypeScript
protected subscribers_: Set<number>
```

A set of subscribers.

**Type:** Set&lt;number&gt;

**Since:** 7

<!--Device-SubscribedAbstractProperty-protected subscribers_: Set<number>--><!--Device-SubscribedAbstractProperty-protected subscribers_: Set<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
