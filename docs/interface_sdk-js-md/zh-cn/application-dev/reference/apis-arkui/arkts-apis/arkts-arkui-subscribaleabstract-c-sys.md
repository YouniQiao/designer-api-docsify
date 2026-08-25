# SubscribaleAbstract（系统接口）

可订阅抽象类，用于管理所持有的属性集合，提供属性的添加、删除和变更通知能力。

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## addOwningProperty

```TypeScript
public addOwningProperty(subscriber: IPropertySubscriber): void
```

添加持有的属性。属性不再使用时，应调用[removeOwningProperty](#removeowningproperty) 或[removeOwningPropertyById](#removeowningpropertybyid)移除。

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscriber | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | 是 |

## constructor

```TypeScript
constructor()
```

构造函数。

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## notifyPropertyHasChanged

```TypeScript
protected notifyPropertyHasChanged(propName: string, newValue: any): void
```

通知属性更改时调用。

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| propName | string | 是 |
| newValue | any | 是 |

## removeOwningProperty

```TypeScript
public removeOwningProperty(property: IPropertySubscriber): void
```

使用ID删除持有的属性时调用。

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| property | [IPropertySubscriber](arkts-arkui-ipropertysubscriber-i-sys.md) | 是 |

## removeOwningPropertyById

```TypeScript
public removeOwningPropertyById(subscriberId: number): void
```

使用ID删除持有的属性时调用。

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscriberId | number | 是 |

## owningProperties_

```TypeScript
private owningProperties_: Set<number>
```

所持有的属性集合。

**类型：** Set&lt;number&gt;

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。
