# SubscribedAbstractProperty

Represents a synchronized property from [AppStorage](../../../ui/state-management/arkts-appstorage.md) or  
[LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare abstract class SubscribedAbstractProperty<T>--><!--Device-unnamed-declare abstract class SubscribedAbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## aboutToBeDeleted

```TypeScript
abstract aboutToBeDeleted(): void
```

Cancels the synchronization relationship between the [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)instance and [AppStorage](../../../ui/state-management/arkts-appstorage.md) or  
[LocalStorage](../../../ui/state-management/arkts-localstorage.md), whether it is a one-way or two-way binding.After **aboutToBeDeleted** is called, the **SubscribedAbstractProperty** instance is invalidated, meaning it can no longer be used to call the [set](arkts-arkui-localstorage-c.md#set) or [get](arkts-arkui-localstorage-c.md#get) API.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

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

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SubscribedAbstractProperty-constructor(    /**     * Subscriber IPropertySubscriber.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @systemapi     * @since 7     *      */    subscribeMe?: IPropertySubscriber,    /**     * Subscriber info.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @systemapi     * @since 7     *      */    info?: string,  )--><!--Device-SubscribedAbstractProperty-constructor(    /**     * Subscriber IPropertySubscriber.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @systemapi     * @since 7     *      */    subscribeMe?: IPropertySubscriber,    /**     * Subscriber info.     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @systemapi     * @since 7     *      */    info?: string,  )-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No | Variable properties. |
| info | string | No | Variable information. |

## createOneWaySync

```TypeScript
createOneWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyOneWay<T>
```

Creates one-way synchronization.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SubscribedAbstractProperty-createOneWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyOneWay<T>--><!--Device-SubscribedAbstractProperty-createOneWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyOneWay<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No | Variable properties. |
| info | string | No | Variable information. |

**Return value:**

| Type | Description |
| --- | --- |
| [SyncedPropertyOneWay](arkts-arkui-syncedpropertyoneway-c-sys.md)&lt;T&gt; | One-way synchronized property. |

## createTwoWaySync

```TypeScript
createTwoWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyTwoWay<T>
```

Creates two-way synchronization.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SubscribedAbstractProperty-createTwoWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyTwoWay<T>--><!--Device-SubscribedAbstractProperty-createTwoWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyTwoWay<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No | Variable properties. |
| info | string | No | Variable information. |

**Return value:**

| Type | Description |
| --- | --- |
| [SyncedPropertyTwoWay](arkts-arkui-syncedpropertytwoway-c-sys.md)&lt;T&gt; | Two-way synchronized property. |

## get

```TypeScript
abstract get(): T
```

Reads the data of the synchronized property from [AppStorage](../../../ui/state-management/arkts-appstorage.md) or  
[LocalStorage](../../../ui/state-management/arkts-localstorage.md).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-SubscribedAbstractProperty-abstract get(): T--><!--Device-SubscribedAbstractProperty-abstract get(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| T | Data of the synchronized property in AppStorage or LocalStorage. |

## id

```TypeScript
id(): number
```

Called when the subscriber ID is entered.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SubscribedAbstractProperty-id(): number--><!--Device-SubscribedAbstractProperty-id(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## info

```TypeScript
info(): string
```

Property name.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SubscribedAbstractProperty-info(): string--><!--Device-SubscribedAbstractProperty-info(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | Property name. |

## notifyHasChanged

```TypeScript
protected notifyHasChanged(newValue: T): void
```

Notifies subscribers that the value has changed.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SubscribedAbstractProperty-protected notifyHasChanged(newValue: T): void--><!--Device-SubscribedAbstractProperty-protected notifyHasChanged(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | New value after the change. |

## notifyPropertyRead

```TypeScript
protected notifyPropertyRead(): void
```

Notifies subscribers that the property has been read.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SubscribedAbstractProperty-protected notifyPropertyRead(): void--><!--Device-SubscribedAbstractProperty-protected notifyPropertyRead(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## numberOfSubscrbers

```TypeScript
numberOfSubscrbers(): number
```

Obtains the number of subscribers.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SubscribedAbstractProperty-numberOfSubscrbers(): number--><!--Device-SubscribedAbstractProperty-numberOfSubscrbers(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | Number of subscribers. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-SubscribedAbstractProperty-abstract set(newValue: T): void--><!--Device-SubscribedAbstractProperty-abstract set(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | Data to set. Since API version 12, the value can be **null** or **undefined**. |

## unlinkSuscriber

```TypeScript
unlinkSuscriber(subscriberId: number): void
```

Removes a subscriber.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SubscribedAbstractProperty-unlinkSuscriber(subscriberId: number): void--><!--Device-SubscribedAbstractProperty-unlinkSuscriber(subscriberId: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subscriberId | number | Yes | ID of the subscriber to remove. |

## id_

```TypeScript
private id_
```

Private member variable ID.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SubscribedAbstractProperty-private id_--><!--Device-SubscribedAbstractProperty-private id_-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## info_

```TypeScript
private info_?
```

Variable information.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SubscribedAbstractProperty-private info_?--><!--Device-SubscribedAbstractProperty-private info_?-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subscribers_

```TypeScript
protected subscribers_: Set<number>
```

A set of subscribers.

**Type:** Set&lt;number&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SubscribedAbstractProperty-protected subscribers_: Set<number>--><!--Device-SubscribedAbstractProperty-protected subscribers_: Set<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

