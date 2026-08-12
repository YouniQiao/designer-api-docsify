# SubscribedAbstractProperty

SubscribedAbstractProperty是[AppStorage](../../../ui/state-management/arkts-appstorage.md)/  
[LocalStorage](../../../ui/state-management/arkts-localstorage.md)中属性的单/双向同步绑定对象，用于与AppStorage/LocalStorage中的属性建立数据同步关系。SubscribedAbstractProperty实例需要通过[aboutToBeDeleted](#aboutToBeDeleted)接口手动释放，以取消同步关系并无效化实例。

> **说明：**
> 
> 从API version 12开始，AppStorage/LocalStorage支持Map、Set、Date类型，支持null、undefined以及联合类型。

**起始版本：** 9

<!--Device-unnamed-declare abstract class SubscribedAbstractProperty<T>--><!--Device-unnamed-declare abstract class SubscribedAbstractProperty<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## aboutToBeDeleted

```TypeScript
abstract aboutToBeDeleted(): void
```

取消[SubscribedAbstractProperty](#SubscribedAbstractProperty)实例对  
[AppStorage](../../../ui/state-management/arkts-appstorage.md)/  
[LocalStorage](../../../ui/state-management/arkts-localstorage.md)的单向或双向同步关系，并无效化SubscribedAbstractProperty实例。即调用aboutToBeDeleted方法之后，不能再使用SubscribedAbstractProperty实例调用[set](arkts-arkui-localstorage-c.md#set)或[get](arkts-arkui-localstorage-c.md#get)方法。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SubscribedAbstractProperty-abstract aboutToBeDeleted(): void--><!--Device-SubscribedAbstractProperty-abstract aboutToBeDeleted(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 示例

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let link = AppStorage.setAndLink('PropB', 49); // PropA -> 47, PropB -> 49
link.aboutToBeDeleted();
```

## constructor

```TypeScript
constructor(
    /**
     * 订阅者，用于接收属性变化通知；不传入则不建立订阅关系。
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @systemapi
     * @since 7
     * 
     */
    subscribeMe?: IPropertySubscriber,
    /**
     * 变量信息，用于标识该订阅关系；不传入时默认为undefined。
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @systemapi
     * @since 7
     * 
     */
    info?: string,
  )
```

构造函数。若传入了subscribeMe参数建立了订阅关系，订阅关系不再需要时，应调用[unlinkSuscriber()](#unlinkSuscriber)解除订阅（订阅者ID通过[IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md#IPropertySubscriber).[id()](arkts-arkui-ipropertysubscriber-i-sys.md#id)获取）。

**起始版本：** 7

<!--Device-SubscribedAbstractProperty-constructor(    /**     * 订阅者，用于接收属性变化通知；不传入则不建立订阅关系。     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @systemapi     * @since 7     *      */    subscribeMe?: IPropertySubscriber,    /**     * 变量信息，用于标识该订阅关系；不传入时默认为undefined。     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @systemapi     * @since 7     *      */    info?: string,  )--><!--Device-SubscribedAbstractProperty-constructor(    /**     * 订阅者，用于接收属性变化通知；不传入则不建立订阅关系。     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @systemapi     * @since 7     *      */    subscribeMe?: IPropertySubscriber,    /**     * 变量信息，用于标识该订阅关系；不传入时默认为undefined。     *     * @syscap SystemCapability.ArkUI.ArkUI.Full     * @systemapi     * @since 7     *      */    info?: string,  )-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | 否 |
| [info](#info) | string | 否 |

## createOneWaySync

```TypeScript
createOneWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyOneWay<T>
```

创建单向同步属性。数据变更仅从数据源向订阅者单向传播。订阅关系不再需要时，应调用[unlinkSuscriber()](#unlinkSuscriber)解除订阅（订阅者ID通过[IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md#IPropertySubscriber).[id()](arkts-arkui-ipropertysubscriber-i-sys.md#id)获取），或由返回的[SyncedPropertyOneWay](arkts-arkui-syncedpropertyoneway-c-sys.md#SyncedPropertyOneWay)对象的[aboutToBeDeleted()](arkts-arkui-syncedpropertyoneway-c-sys.md#aboutToBeDeleted)方法处理取消订阅。

**起始版本：** 7

<!--Device-SubscribedAbstractProperty-createOneWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyOneWay<T>--><!--Device-SubscribedAbstractProperty-createOneWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyOneWay<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | 否 |
| [info](#info) | string | 否 |

**返回值：**

| 类型 |
| --- |
| [SyncedPropertyOneWay](arkts-arkui-syncedpropertyoneway-c-sys.md)&lt;T&gt; |

## createTwoWaySync

```TypeScript
createTwoWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyTwoWay<T>
```

创建双向同步属性。数据变更在数据源与订阅者之间双向传播。与[createOneWaySync](#createOneWaySync)相比，该方法支持数据源与订阅者之间的双向同步，适用于订阅者也需要反向修改数据源的场景；若仅需数据源向订阅者单向同步，请使用[createOneWaySync](#createOneWaySync)。订阅关系不再需要时，应调用[unlinkSuscriber()](#unlinkSuscriber)解除订阅（订阅者ID通过[IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md#IPropertySubscriber).[id()](arkts-arkui-ipropertysubscriber-i-sys.md#id)获取），或由返回的[SyncedPropertyTwoWay](arkts-arkui-syncedpropertytwoway-c-sys.md#SyncedPropertyTwoWay)对象的[aboutToBeDeleted()](arkts-arkui-syncedpropertytwoway-c-sys.md#aboutToBeDeleted)方法处理取消订阅。

**起始版本：** 7

<!--Device-SubscribedAbstractProperty-createTwoWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyTwoWay<T>--><!--Device-SubscribedAbstractProperty-createTwoWaySync(subscribeMe?: IPropertySubscriber, info?: string): SyncedPropertyTwoWay<T>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | 否 |
| [info](#info) | string | 否 |

**返回值：**

| 类型 |
| --- |
| [SyncedPropertyTwoWay](arkts-arkui-syncedpropertytwoway-c-sys.md)&lt;T&gt; |

## get

```TypeScript
abstract get(): T
```

读取[AppStorage](../../../ui/state-management/arkts-appstorage.md)/  
[LocalStorage](../../../ui/state-management/arkts-localstorage.md)中所同步属性的数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-SubscribedAbstractProperty-abstract get(): T--><!--Device-SubscribedAbstractProperty-abstract get(): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| T |

## 示例

```TypeScript
AppStorage.setOrCreate('PropA', 47); 
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');    
prop1.get(); // prop1.get()=47
```

## id

```TypeScript
id(): number
```

获取ID时调用。

**起始版本：** 7

<!--Device-SubscribedAbstractProperty-id(): number--><!--Device-SubscribedAbstractProperty-id(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## info

```TypeScript
info(): string
```

返回[AppStorage](../../../ui/state-management/arkts-appstorage.md)/  
[LocalStorage](../../../ui/state-management/arkts-localstorage.md)中所同步属性的属性名。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SubscribedAbstractProperty-info(): string--><!--Device-SubscribedAbstractProperty-info(): string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| string |

## 示例

```TypeScript
AppStorage.setOrCreate('PropA', 47); 
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
prop1.info(); // prop1.info() = 'PropA'
```

## notifyHasChanged

```TypeScript
protected notifyHasChanged(newValue: T): void
```

通知变化时调用。

**起始版本：** 7

<!--Device-SubscribedAbstractProperty-protected notifyHasChanged(newValue: T): void--><!--Device-SubscribedAbstractProperty-protected notifyHasChanged(newValue: T): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newValue | T | 是 |

## notifyPropertyRead

```TypeScript
protected notifyPropertyRead(): void
```

通知读取时调用。

**起始版本：** 7

<!--Device-SubscribedAbstractProperty-protected notifyPropertyRead(): void--><!--Device-SubscribedAbstractProperty-protected notifyPropertyRead(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## numberOfSubscrbers

```TypeScript
numberOfSubscrbers(): number
```

获取订阅者数量时调用。

**起始版本：** 7

<!--Device-SubscribedAbstractProperty-numberOfSubscrbers(): number--><!--Device-SubscribedAbstractProperty-numberOfSubscrbers(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## set

```TypeScript
abstract set(newValue: T): void
```

设置[AppStorage](../../../ui/state-management/arkts-appstorage.md)/  
[LocalStorage](../../../ui/state-management/arkts-localstorage.md)中所同步属性的数据，newValue必须是T类型，从API version 12开始可以为null或undefined。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-SubscribedAbstractProperty-abstract set(newValue: T): void--><!--Device-SubscribedAbstractProperty-abstract set(newValue: T): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newValue | T | 是 |

## 示例

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');
prop1.set(1); // prop1.get()=1
// 从API version 12开始支持Map、Set、Date类型，支持null、undefined以及联合类型。
let mapValue: Map<string, number> = new Map([['1', 0]]);
let prop2 = AppStorage.setAndProp('MapA', mapValue);
prop2.set(mapValue);
let setValue: Set<string> = new Set(['1']);
let prop3 = AppStorage.setAndProp('SetB', setValue);
prop3.set(setValue);
let dateValue: Date = new Date('2024');
let prop4 = AppStorage.setAndProp('DateC', dateValue);
prop4.set(dateValue);
prop2.set(null);
prop3.set(undefined);
```

## unlinkSuscriber

```TypeScript
unlinkSuscriber(subscriberId: number): void
```

根据订阅者ID解除订阅时调用。

**起始版本：** 7

<!--Device-SubscribedAbstractProperty-unlinkSuscriber(subscriberId: number): void--><!--Device-SubscribedAbstractProperty-unlinkSuscriber(subscriberId: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscriberId | number | 是 |

## id_

```TypeScript
private id_
```

订阅属性的唯一标识ID，用于在订阅关系管理中区分不同的订阅属性实例。

**起始版本：** 7

<!--Device-SubscribedAbstractProperty-private id_--><!--Device-SubscribedAbstractProperty-private id_-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## info_

```TypeScript
private info_?
```

变量信息，用于标识该订阅关系。

**起始版本：** 7

<!--Device-SubscribedAbstractProperty-private info_?--><!--Device-SubscribedAbstractProperty-private info_?-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## subscribers_

```TypeScript
protected subscribers_: Set<number>
```

订阅者集合。

**类型：** Set&lt;number&gt;

**起始版本：** 7

<!--Device-SubscribedAbstractProperty-protected subscribers_: Set<number>--><!--Device-SubscribedAbstractProperty-protected subscribers_: Set<number>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
