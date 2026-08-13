# SyncedPropertyTwoWay（系统接口）

继承自[SubscribedAbstractProperty\&lt;T\&gt;](arkts-arkui-subscribedabstractproperty-c.md#SubscribedAbstractProperty（系统接口）)。用于实现父子组件之间的双向状态数据同步。

**继承/实现关系：** SyncedPropertyTwoWay extends SubscribedAbstractProperty<T> implements ISinglePropertyChangeSubscriber<T>

**起始版本：** 7

**废弃版本：** -1

<!--Device-unnamed-declare class SyncedPropertyTwoWay--><!--Device-unnamed-declare class SyncedPropertyTwoWay-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## aboutToBeDeleted

```TypeScript
aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void
```

销毁时调用。

**起始版本：** 7

**废弃版本：** -1

<!--Device-SyncedPropertyTwoWay-aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void--><!--Device-SyncedPropertyTwoWay-aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| unsubscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | 否 |

## constructor

```TypeScript
constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)
```

构造函数。订阅关系不再需要时，应调用[unlinkSuscriber()](arkts-arkui-subscribedabstractproperty-c-sys.md#unlinkSuscriber)解除 订阅（订阅者ID通过[IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md#IPropertySubscriber（系统接口）).[id()](arkts-arkui-ipropertysubscriber-i-sys.md#id)获取）， 或调用本对象的[aboutToBeDeleted()](#aboutToBeDeleted)方法处理取消订阅。

**起始版本：** 7

**废弃版本：** -1

<!--Device-SyncedPropertyTwoWay-constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)--><!--Device-SyncedPropertyTwoWay-constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; | 是 |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | 否 |
| info | string | 否 |

## get

```TypeScript
get(): T
```

获取数据时调用。

**起始版本：** 7

**废弃版本：** -1

<!--Device-SyncedPropertyTwoWay-get(): T--><!--Device-SyncedPropertyTwoWay-get(): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| T |

## hasChanged

```TypeScript
hasChanged(newValue: T): void
```

变化时调用。

**起始版本：** 7

**废弃版本：** -1

<!--Device-SyncedPropertyTwoWay-hasChanged(newValue: T): void--><!--Device-SyncedPropertyTwoWay-hasChanged(newValue: T): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newValue | T | 是 |

## set

```TypeScript
set(newValue: T): void
```

赋值时调用。

**起始版本：** 7

**废弃版本：** -1

<!--Device-SyncedPropertyTwoWay-set(newValue: T): void--><!--Device-SyncedPropertyTwoWay-set(newValue: T): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newValue | T | 是 |

## source_

```TypeScript
private source_
```

双向同步属性的数据源。

**起始版本：** 7

**废弃版本：** -1

<!--Device-SyncedPropertyTwoWay-private source_--><!--Device-SyncedPropertyTwoWay-private source_-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。
