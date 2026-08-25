# AppStorage

AppStorage是与应用进程绑定的全局UI状态存储中心，由UI框架在应用启动时创建，将UI状态数据存储于运行内存，实现应用级全局状态共享。具体UI使用说明，详见 [AppStorage：应用全局的UI状态存储](../../../ui/state-management/arkts-appstorage.md)。

> **说明：**&gt;
> 从API version 12开始，AppStorage支持[Map](../../../ui/state-management/arkts-appstorage.md#装饰map类型变量)、
> [Set](../../../ui/state-management/arkts-appstorage.md#装饰set类型变量)、
> [Date类型](../../../ui/state-management/arkts-appstorage.md#装饰date类型变量)，支持null、undefined以及
> [联合类型](../../../ui/state-management/arkts-appstorage.md#appstorage支持联合类型)。

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## Clear

```TypeScript
static Clear(): boolean
```

删除[AppStorage](../../../ui/state-management/arkts-appstorage.md)中所有属性。前提是AppStorage已经没有任何订阅者。如果有订阅者，Clear将不会生效并返回 false。如果没有订阅者且删除成功则返回true。订阅者的含义参考[delete](#delete)。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [clear](#clear)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## clear

```TypeScript
static clear(): boolean
```

删除[AppStorage](../../../ui/state-management/arkts-appstorage.md)中所有属性。仅当AppStorage没有任何订阅者时可删除成功并返回true；如果有订阅者， clear不会生效并返回false。订阅者的含义参考[delete](#delete)。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## Delete

```TypeScript
static Delete(propName: string): boolean
```

在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中删除propName对应的属性。仅当AppStorage中该属性没有任何订阅者时可删除成功并返回true；如果有订阅者，则返回false。属性的订阅者为[Link](#link)、[Prop](#prop)等接口返回的实例，以及 [@StorageLink](../../../ui/state-management/arkts-appstorage.md#storagelink)和 [@StorageProp](../../../ui/state-management/arkts-appstorage.md#storageprop)装饰的变量。如果\@StorageLink('propName')、\@ StorageProp('propName')装饰的变量或SubscribedAbstractProperty实例依旧对propName有同步关系，则该属性不能从AppStorage中删除。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [delete](#delete)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## delete

```TypeScript
static delete(propName: string): boolean
```

在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中删除propName对应的属性。仅当AppStorage中该属性没有任何订阅者时可删除成功并返回true；如果有订阅者，则返回false。属性的订阅者为：
1. [@StorageLink](../../../ui/state-management/arkts-appstorage.md#storagelink)、[@StorageProp](../../../ui/state-management/arkts-appstorage.md#storageprop)装饰的变量。
2. 通过[link](#link)、[prop](#prop)、[setAndLink](#setandlink)、[setAndProp](#setandprop)接口返回的[SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)的实例。
如需删除这些订阅者，可通过以下方式：
1. 删除\@StorageLink、\@StorageProp所在的自定义组件。删除自定义组件请参考[自定义组件的删除](../../../ui/state-management/arkts-page-custom-components-lifecycle.md#自定义组件的删除)。
2. 对link、prop、setAndLink、setAndProp接口返回的SubscribedAbstractProperty的实例调用[aboutToBeDeleted](arkts-arkui-subscribedabstractproperty-c.md#abouttobedeleted)接口。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## Get

```TypeScript
static Get<T>(propName: string): T | undefined
```

获取propName在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中对应的属性值。如果不存在则返回undefined。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [get](#get)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## get

```TypeScript
static get<T>(propName: string): T | undefined
```

获取propName在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中对应的属性值。如果不存在则返回undefined。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| T \| undefined |

## Has

```TypeScript
static Has(propName: string): boolean
```

判断propName对应的属性是否在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中存在。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [has](#has)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## has

```TypeScript
static has(propName: string): boolean
```

判断propName对应的属性是否在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中存在。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## IsMutable

```TypeScript
static IsMutable(propName: string): boolean
```

返回[AppStorage](../../../ui/state-management/arkts-appstorage.md)中propName对应的属性是否是可变的。

> **说明：**&gt;
> 从API version 7开始支持，从API version 10开始废弃，暂无替代接口。

**起始版本：** 7

**废弃版本：** 10

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## Keys

```TypeScript
static Keys(): IterableIterator<string>
```

返回[AppStorage](../../../ui/state-management/arkts-appstorage.md)中所有的属性名。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [keys](#keys)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;string & gt; |

## keys

```TypeScript
static keys(): IterableIterator<string>
```

返回[AppStorage](../../../ui/state-management/arkts-appstorage.md)中所有的属性名。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| IterableIterator & lt;string & gt; |

## Link

```TypeScript
static Link(propName: string): any
```

与[AppStorage](../../../ui/state-management/arkts-appstorage.md)中对应的propName建立双向数据绑定。如果给定的propName在AppStorage中存在，返回 与AppStorage中propName对应属性的双向绑定数据。双向绑定数据的修改会同步回AppStorage中，AppStorage会将变化同步到所有绑定该propName的数据和自定义组件中。如果AppStorage中不存在propName，则返回undefined。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [link](#link)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| any |

## link

```TypeScript
static link<T>(propName: string): SubscribedAbstractProperty<T>
```

与[AppStorage](../../../ui/state-management/arkts-appstorage.md)中对应的propName建立双向数据绑定。如果给定的propName在AppStorage中存在，返回 AppStorage中propName对应属性的双向绑定数据。与[prop](#prop)的单向数据绑定不同，link的修改会同步回AppStorage，AppStorage会将变化同步到所有绑定该 propName的数据和自定义组件中。如果AppStorage中不存在propName，则返回undefined。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

## Prop

```TypeScript
static Prop(propName: string): any
```

与[AppStorage](../../../ui/state-management/arkts-appstorage.md)中对应的propName建立单向数据绑定。如果给定的propName在AppStorage中存在，则返 回与AppStorage中propName对应属性的单向绑定数据。如果AppStorage中不存在propName，则返回undefined。单向绑定数据的修改不会同步回AppStorage中。

> **说明：**&gt;
> Prop仅支持S类型（number、boolean、string）。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [prop](#prop)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| any |

## prop

```TypeScript
static prop<T>(propName: string): SubscribedAbstractProperty<T>
```

与[AppStorage](../../../ui/state-management/arkts-appstorage.md)中对应的propName建立单向数据绑定。如果给定的propName在AppStorage中存在，则返 回与AppStorage中propName对应属性的单向绑定数据。如果AppStorage中不存在propName，则返回undefined。单向绑定数据的修改不会同步回AppStorage中。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

## ref

```TypeScript
static ref<T>(propName: string): AbstractProperty<T> | undefined
```

如果给定的propName在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中存在，则返回AppStorage中propName对应属性的引用。否则，返 回undefined。与[link](#link)的功能基本一致，区别在于不需要手动释放返回的[AbstractProperty&lt;T&gt;](arkts-arkui-abstractproperty-i.md)类型的变量。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |

**返回值：**

| 类型 |
| --- |
| [AbstractProperty](arkts-arkui-abstractproperty-i.md)&lt;T&gt; \| undefined |

## Set

```TypeScript
static Set<T>(propName: string, newValue: T): boolean
```

在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中设置propName对应属性的值。如果newValue与propName对应属性的值相同，则不做赋值 操作，状态变量不会通知UI刷新propName对应属性的值。与[SetOrCreate](#setorcreate)不同，Set仅在propName已存在时生效，propName不存在时返回 false。从API version 12开始，newValue可以为null或undefined。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [set](#set)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| newValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## set

```TypeScript
static set<T>(propName: string, newValue: T): boolean
```

在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中设置propName对应属性的值。如果newValue与propName对应属性的值相同，则不做赋值 操作，状态变量不会通知UI刷新propName对应属性的值。与[setOrCreate](#setorcreate)不同，set仅在propName已存在时生效，propName不存在时返回 false。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| newValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## SetAndLink

```TypeScript
static SetAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

与[Link](#link)接口类似，如果给定的propName在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中存 在，则返回该propName对应的属性的双向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，并返回其双向绑定数据。defaultValue必须为T类型，且不能为 null或undefined。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [setAndLink](#setandlink)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| defaultValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

## setAndLink

```TypeScript
static setAndLink<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

与[link](#link)接口类似，如果给定的propName在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中存 在，则返回该propName对应的属性的双向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，返回其双向绑定数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| defaultValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

## SetAndProp

```TypeScript
static SetAndProp<S>(propName: string, defaultValue: S): SubscribedAbstractProperty<S>
```

与[Prop](#prop)接口类似，如果给定的propName在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中存 在，则返回该propName对应的属性的单向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，返回其单向绑定数据。defaultValue必须为S类型，且不能为 null或undefined。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [setAndProp](#setandprop)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| defaultValue | S | 是 |

**返回值：**

| 类型 |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;S&gt; |

## setAndProp

```TypeScript
static setAndProp<T>(propName: string, defaultValue: T): SubscribedAbstractProperty<T>
```

与[prop](#prop)接口类似，如果给定的propName在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中存 在，则返回该propName对应的属性的单向绑定数据。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，返回其单向绑定数据。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| defaultValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| [SubscribedAbstractProperty](arkts-arkui-subscribedabstractproperty-c.md)&lt;T&gt; |

## setAndRef

```TypeScript
static setAndRef<T>(propName: string, defaultValue: T): AbstractProperty<T>
```

与[ref](#ref)接口类似，如果给定的propName在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中存在，则 返回AppStorage中propName对应属性的引用。如果不存在，则使用defaultValue在AppStorage中创建和初始化propName对应的属性，并返回其引用。与[setAndLink](#setandlink)的功能基本一致，区别在于不需要手动释放返回的[AbstractProperty&lt;T&gt;](arkts-arkui-abstractproperty-i.md) 类型的变量。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| defaultValue | T | 是 |

**返回值：**

| 类型 |
| --- |
| [AbstractProperty](arkts-arkui-abstractproperty-i.md)&lt;T&gt; |

## SetOrCreate

```TypeScript
static SetOrCreate<T>(propName: string, newValue: T): void
```

如果propName已经在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中存在，并且newValue和propName对应属性的值不同，则设置 propName对应属性的值为newValue，否则状态变量不会通知UI刷新propName对应属性的值。如果不存在，则创建propName属性，值为newValue。从API version 12开始，newValue可以为 null或undefined。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [setOrCreate](#setorcreate)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| newValue | T | 是 |

## setOrCreate

```TypeScript
static setOrCreate<T>(propName: string, newValue: T): void
```

如果propName已经在[AppStorage](../../../ui/state-management/arkts-appstorage.md)中存在，并且newValue和propName对应属性的值不同，则设置 propName对应属性的值为newValue，否则状态变量不会通知UI刷新propName对应属性的值。如果propName不存在，则创建propName属性，值为newValue。setOrCreate仅可创建单个AppStorage的键值对，如需创建多个AppStorage键值对，可多次调用此方法。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| newValue | T | 是 |

## Size

```TypeScript
static Size(): number
```

返回[AppStorage](../../../ui/state-management/arkts-appstorage.md)中的属性数量。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [size](#size)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## size

```TypeScript
static size(): number
```

返回[AppStorage](../../../ui/state-management/arkts-appstorage.md)中的属性数量。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## staticClear

```TypeScript
static staticClear(): boolean
```

删除[AppStorage](../../../ui/state-management/arkts-appstorage.md)中所有属性。仅当AppStorage没有任何订阅者时可删除成功并返回true；如果有订阅者， staticClear不会生效并返回false。订阅者的含义参考[delete](#delete)。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [Clear](#clear)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |
