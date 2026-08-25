# Class

用于描述运行时类型的类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## createInstance

```TypeScript
createInstance(): Object
```

创建当前类的新实例，并调用其无参构造函数。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Object |

## current

```TypeScript
static current(): Class
```

获取当前类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [Class](arkts-arkts-class-c.md) |

## from

```TypeScript
static from<T>(): Class
```

获取对象的类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [Class](arkts-arkts-class-c.md) |

## getConstructors

```TypeScript
getConstructors(): FixedArray<reflect.Constructor>
```

获取类的所有构造函数。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| FixedArray & lt;reflect.Constructor & gt; |

## getDescriptor

```TypeScript
getDescriptor(): string
```

获取描述信息。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## getFixedArrayComponentType

```TypeScript
getFixedArrayComponentType(): Class | undefined
```

如果当前类是定长数组，则获取其元素类型。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [Class](arkts-arkts-class-c.md) \| undefined |

## getInstanceField

```TypeScript
getInstanceField(name: string): reflect.InstanceField | undefined
```

在当前类声明的字段中按名称查找实例字段。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| reflect.InstanceField \| undefined |

## getInstanceFields

```TypeScript
getInstanceFields(): FixedArray<reflect.InstanceField>
```

获取类中声明的实例字段。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| FixedArray & lt;reflect.InstanceField & gt; |

## getInstanceMethod

```TypeScript
getInstanceMethod(name: string, signature?: FixedArray<Class>): reflect.InstanceMethod | undefined
```

在类中声明的方法（包含所实现接口的默认方法）中查找指定的 实例方法。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| signature | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| reflect.InstanceMethod \| undefined |

## getInstanceMethods

```TypeScript
getInstanceMethods(): FixedArray<reflect.InstanceMethod>
```

获取类中声明的实例方法（包含所实现接口的默认方法）。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| FixedArray & lt;reflect.InstanceMethod & gt; |

## getInterfaces

```TypeScript
getInterfaces(): FixedArray<Class>
```

获取当前类实现的接口。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; |

## getLinker

```TypeScript
getLinker(): RuntimeLinker
```

获取与当前类关联的运行时链接器。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| RuntimeLinker |

## getName

```TypeScript
getName(): string
```

获取类在程序集中的名称。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## getStaticField

```TypeScript
getStaticField(name: string): reflect.StaticField | undefined
```

在当前类声明的字段中按名称查找静态字段。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| reflect.StaticField \| undefined |

## getStaticFields

```TypeScript
getStaticFields(): FixedArray<reflect.StaticField>
```

获取当前类中声明的静态字段。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| FixedArray & lt;reflect.StaticField & gt; |

## getStaticMethod

```TypeScript
getStaticMethod(name: string, signature?: FixedArray<Class>): reflect.StaticMethod | undefined
```

在类中声明的方法中查找指定的静态方法。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| signature | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| reflect.StaticMethod \| undefined |

## getStaticMethods

```TypeScript
getStaticMethods(): FixedArray<reflect.StaticMethod>
```

获取类中声明的静态方法。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| FixedArray & lt;reflect.StaticMethod & gt; |

## getSuper

```TypeScript
getSuper(): Class | undefined
```

获取类的父类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [Class](arkts-arkts-class-c.md) \| undefined |

## getUnionConstituentTypes

```TypeScript
getUnionConstituentTypes(): FixedArray<Class> | undefined
```

获取联合类型类的所有组成类型。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; \| undefined |

## initialize

```TypeScript
initialize(): void
```

如果类尚未初始化，则调用一次类初始化器。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## isAbstract

```TypeScript
isAbstract(): boolean
```

判断该类是否为抽象类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isEnum

```TypeScript
isEnum(): boolean
```

判断当前类是否为枚举。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isFinal

```TypeScript
isFinal(): boolean
```

判断该类是否为final类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isFixedArray

```TypeScript
isFixedArray(): boolean
```

判断当前类是否为定长数组。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isInterface

```TypeScript
isInterface(): boolean
```

判断当前类是否为接口。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isNamespace

```TypeScript
public isNamespace(): boolean
```

判断当前类是否为命名空间。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isPrimitive

```TypeScript
isPrimitive(): boolean
```

判断该类是否对应基本类型。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## isSubtypeOf

```TypeScript
isSubtypeOf(other: Class): boolean
```

判断当前类是否为另一个类的子类型。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [Class](arkts-arkts-class-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isUnion

```TypeScript
isUnion(): boolean
```

判断当前类是否为联合类型。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## of

```TypeScript
static of(obj: Object | null): Class
```

获取对象的类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Object \| null | 是 |

**返回值：**

| 类型 |
| --- |
| [Class](arkts-arkts-class-c.md) |

## ofAny

```TypeScript
static ofAny(obj: Any): Class | undefined
```

获取任意类型对象的类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Any | 是 |

**返回值：**

| 类型 |
| --- |
| [Class](arkts-arkts-class-c.md) \| undefined |

## ofCaller

```TypeScript
static ofCaller(): Class | undefined
```

获取调用者的类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [Class](arkts-arkts-class-c.md) \| undefined |

## PRIMITIVE_BOOLEAN

```TypeScript
public static readonly PRIMITIVE_BOOLEAN: Class
```

保存boolean基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_BYTE

```TypeScript
public static readonly PRIMITIVE_BYTE: Class
```

保存byte基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_CHAR

```TypeScript
public static readonly PRIMITIVE_CHAR: Class
```

保存char基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_DOUBLE

```TypeScript
public static readonly PRIMITIVE_DOUBLE: Class
```

保存double基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_FLOAT

```TypeScript
public static readonly PRIMITIVE_FLOAT: Class
```

保存float基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_INT

```TypeScript
public static readonly PRIMITIVE_INT: Class
```

保存int基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_LONG

```TypeScript
public static readonly PRIMITIVE_LONG: Class
```

保存long基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_NUMBER

```TypeScript
public static readonly PRIMITIVE_NUMBER: Class
```

保存number基本类型对应的Class对象（与double相同）。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_SHORT

```TypeScript
public static readonly PRIMITIVE_SHORT: Class
```

保存short基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_VOID

```TypeScript
public static readonly PRIMITIVE_VOID: Class
```

保存void类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
