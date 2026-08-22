# SyncedPropertyOneWay（系统接口）

继承自[SubscribedAbstractProperty\&lt;T\&gt;](arkts-arkui-subscribedabstractproperty-c.md)。用于接收父组件状态值的单向同步，当父组件状态变化时更新自身值。

**继承/实现关系：** SyncedPropertyOneWay extends SubscribedAbstractProperty<T> implements ISinglePropertyChangeSubscriber<T>

**起始版本：** 7

<!--Device-unnamed-declare class SyncedPropertyOneWay--><!--Device-unnamed-declare class SyncedPropertyOneWay-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## aboutToBeDeleted

```TypeScript
aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void
```

销毁时调用。

**起始版本：** 7

<!--Device-SyncedPropertyOneWay-aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void--><!--Device-SyncedPropertyOneWay-aboutToBeDeleted(unsubscribeMe?: IPropertySubscriber): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| unsubscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | 否 | 被取消的订阅者，需为已订阅的订阅者；不传入则取消所有订阅者。 |

**示例**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let link = AppStorage.setAndLink('PropB', 49); // PropA -> 47, PropB -> 49
link.aboutToBeDeleted();
```

## constructor

```TypeScript
constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)
```

构造函数。订阅关系不再需要时，应调用[unlinkSuscriber()](arkts-arkui-subscribedabstractproperty-c-sys.md#unlinksuscriber)解除 订阅（订阅者ID通过[IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md).[id()](arkts-arkui-ipropertysubscriber-i-sys.md#id)获取）， 或调用本对象的[aboutToBeDeleted()](#abouttobedeleted)方法处理取消订阅。

**起始版本：** 7

<!--Device-SyncedPropertyOneWay-constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)--><!--Device-SyncedPropertyOneWay-constructor(source: SubscribedAbstractProperty<T>, subscribeMe?: IPropertySubscriber, info?: string)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; | 是 | 单向同步属性的数据源。 |
| subscribeMe | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | 否 | 订阅者，用于接收属性变化通知；不传入则不建立订阅关系。 |
| info | string | 否 | 变量信息，用于标识该订阅关系；不传入时默认为undefined。 |

**示例**

```TypeScript
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
```

## get

```TypeScript
get(): T
```

获取数据时调用。

**起始版本：** 7

<!--Device-SyncedPropertyOneWay-get(): T--><!--Device-SyncedPropertyOneWay-get(): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回单向同步属性当前的数据值。 |

**示例**

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let value: number = AppStorage.get('PropA') as number; // 47
```

```TypeScript
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let value: number = storage.get('PropA') as number; // 47
```

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let ref1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
ref1?.get(); // ref1.get()=47
```

```TypeScript
AppStorage.setOrCreate('PropA', 47); 
let prop1: SubscribedAbstractProperty<number> = AppStorage.prop('PropA');    
prop1.get(); // prop1.get()=47
```

## hasChanged

```TypeScript
hasChanged(newValue: T): void
```

变化时调用。

**起始版本：** 7

<!--Device-SyncedPropertyOneWay-hasChanged(newValue: T): void--><!--Device-SyncedPropertyOneWay-hasChanged(newValue: T): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newValue | T | 是 | 更改后的新值。 |

## set

```TypeScript
set(newValue: T): void
```

赋值时调用。

**起始版本：** 7

<!--Device-SyncedPropertyOneWay-set(newValue: T): void--><!--Device-SyncedPropertyOneWay-set(newValue: T): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newValue | T | 是 | 要设置的新值。 |

**示例**

```TypeScript
AppStorage.setOrCreate('PropA', 48);
let res: boolean = AppStorage.set('PropA', 47); // true
let res1: boolean = AppStorage.set('PropB', 47); // false
```

```TypeScript
let initialData: Record<string, number> = { 'PropA': 47 };
let storage: LocalStorage = new LocalStorage(initialData);
let res: boolean = storage.set('PropA', 47); // true
let res1: boolean = storage.set('PropB', 47); // false
```

```TypeScript
AppStorage.setOrCreate('PropA', 47);
let ref1: AbstractProperty<number> | undefined = AppStorage.ref('PropA');
ref1?.set(1); // ref1.get()=1
let mapValue: Map<string, number> = new Map([['1', 0]]);
let ref2 = AppStorage.setAndRef('MapA', mapValue);
ref2.set(mapValue);
let setValue: Set<string> = new Set(['1']);
let ref3 = AppStorage.setAndRef('SetB', setValue);
ref3.set(setValue);
let dateValue: Date = new Date('2024');
let ref4 = AppStorage.setAndRef('DateC', dateValue);
ref4.set(dateValue);
ref2.set(null);
ref3.set(undefined);
```

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

## source_

```TypeScript
private source_
```

单向同步属性的数据源。

**起始版本：** 7

<!--Device-SyncedPropertyOneWay-private source_--><!--Device-SyncedPropertyOneWay-private source_-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## wrappedValue_

```TypeScript
private wrappedValue_
```

单向绑定时的值。

**起始版本：** 7

<!--Device-SyncedPropertyOneWay-private wrappedValue_--><!--Device-SyncedPropertyOneWay-private wrappedValue_-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

