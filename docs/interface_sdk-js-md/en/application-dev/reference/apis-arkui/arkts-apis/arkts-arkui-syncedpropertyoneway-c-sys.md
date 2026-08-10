# SyncedPropertyOneWay (System API)

继承自[SubscribedAbstractProperty\&lt;T\&gt;](arkts-arkui-subscribedabstractproperty-c.md)。用于接收父组件状态值的单向同步，当父组件状态变化时更新自身值。

**Inheritance/Implementation:** SyncedPropertyOneWay extends [SubscribedAbstractProperty<T>](SubscribedAbstractProperty<T>) and implements [ISinglePropertyChangeSubscriber<T>](ISinglePropertyChangeSubscriber<T>)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare class SyncedPropertyOneWay<T> extends SubscribedAbstractProperty<T>  implements ISinglePropertyChangeSubscriber<T>--><!--Device-unnamed-declare class SyncedPropertyOneWay<T> extends SubscribedAbstractProperty<T>  implements ISinglePropertyChangeSubscriber<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## aboutToBeDeleted

```TypeScript
aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void
```

销毁时调用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SyncedPropertyOneWay-aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void--><!--Device-SyncedPropertyOneWay-aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| unsubscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No | 被取消的订阅者，需为已订阅的订阅者；不传入则取消所有订阅者。 |

## constructor

```TypeScript
constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)
```

构造函数。订阅关系不再需要时，应调用[unlinkSuscriber()](arkts-arkui-subscribedabstractproperty-c.md#unlinksuscriber)解除订阅（订阅者ID通过[IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md).[id()](arkts-arkui-ipropertysubscriber-i-sys.md#id)获取），或调用本对象的[aboutToBeDeleted()](arkts-arkui-syncedpropertyoneway-c-sys.md#abouttobedeleted)方法处理取消订阅。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SyncedPropertyOneWay-constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)--><!--Device-SyncedPropertyOneWay-constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [SubscribedAbstractProperty](arkts-arkui-storageproperty-subscribedabstractproperty-i.md)&lt;T&gt; | Yes | 单向同步属性的数据源。 |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | No | 订阅者，用于接收属性变化通知；不传入则不建立订阅关系。 |
| info | string | No | 变量信息，用于标识该订阅关系；不传入时默认为undefined。 |

## get

```TypeScript
get(): T
```

获取数据时调用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SyncedPropertyOneWay-get(): T--><!--Device-SyncedPropertyOneWay-get(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回单向同步属性当前的数据值。 |

## hasChanged

```TypeScript
hasChanged(newValue: T): void
```

变化时调用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SyncedPropertyOneWay-hasChanged(newValue: T): void--><!--Device-SyncedPropertyOneWay-hasChanged(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | 更改后的新值。 |

## set

```TypeScript
set(newValue: T): void
```

赋值时调用。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SyncedPropertyOneWay-set(newValue: T): void--><!--Device-SyncedPropertyOneWay-set(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | 要设置的新值。 |

## source_

```TypeScript
private source_
```

单向同步属性的数据源。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SyncedPropertyOneWay-private source_--><!--Device-SyncedPropertyOneWay-private source_-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## wrappedValue_

```TypeScript
private wrappedValue_
```

单向绑定时的值。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-SyncedPropertyOneWay-private wrappedValue_--><!--Device-SyncedPropertyOneWay-private wrappedValue_-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

