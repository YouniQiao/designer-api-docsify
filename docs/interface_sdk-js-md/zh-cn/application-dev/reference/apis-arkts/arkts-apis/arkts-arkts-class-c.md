# Class

用于描述运行时类型的类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

<!--Device-unnamed-export class Class--><!--Device-unnamed-export class Class-End-->

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

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-createInstance(): Object--><!--Device-Class-createInstance(): Object-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 该类的新实例。 |

## current

```TypeScript
static current(): Class
```

获取当前类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-static current(): Class--><!--Device-Class-static current(): Class-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | 当前类。 |

## from

```TypeScript
static from<T>(): Class
```

获取对象的类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-static from<T>(): Class--><!--Device-Class-static from<T>(): Class-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | 该对象的类。 |

## getConstructors

```TypeScript
getConstructors(): FixedArray<reflect.Constructor>
```

获取类的所有构造函数。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getConstructors(): FixedArray<reflect.Constructor>--><!--Device-Class-getConstructors(): FixedArray<reflect.Constructor>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;reflect.Constructor&gt; | 由构造函数组成的定长数组。 |

## getDescriptor

```TypeScript
getDescriptor(): string
```

获取描述信息。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getDescriptor(): string--><!--Device-Class-getDescriptor(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 描述信息。 |

## getFixedArrayComponentType

```TypeScript
getFixedArrayComponentType(): Class | undefined
```

如果当前类是定长数组，则获取其元素类型。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getFixedArrayComponentType(): Class | undefined--><!--Device-Class-getFixedArrayComponentType(): Class | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) \| undefined | 定长数组的元素类型；如果当前类不是 定长数组，则返回undefined。 |

## getInstanceField

```TypeScript
getInstanceField(name: string): reflect.InstanceField | undefined
```

在当前类声明的字段中按名称查找实例字段。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getInstanceField(name: string): reflect.InstanceField | undefined--><!--Device-Class-getInstanceField(name: string): reflect.InstanceField | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 待查找的字段名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| reflect.InstanceField \| undefined | 查找到的实例字段，未找到时返回undefined。 |

## getInstanceFields

```TypeScript
getInstanceFields(): FixedArray<reflect.InstanceField>
```

获取类中声明的实例字段。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getInstanceFields(): FixedArray<reflect.InstanceField>--><!--Device-Class-getInstanceFields(): FixedArray<reflect.InstanceField>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;reflect.InstanceField&gt; | 由实例字段组成的定长数组。 |

## getInstanceMethod

```TypeScript
getInstanceMethod(name: string, signature?: FixedArray<Class>): reflect.InstanceMethod | undefined
```

在类中声明的方法（包含所实现接口的默认方法）中查找指定的 实例方法。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getInstanceMethod(name: string, signature?: FixedArray<Class>): reflect.InstanceMethod | undefined--><!--Device-Class-getInstanceMethod(name: string, signature?: FixedArray<Class>): reflect.InstanceMethod | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 待查找的方法名。 |
| signature | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | 否 | 用于确定方法签名的参数类型数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| reflect.InstanceMethod \| undefined | 查找到的实例方法，未找到时返回undefined。 |

## getInstanceMethods

```TypeScript
getInstanceMethods(): FixedArray<reflect.InstanceMethod>
```

获取类中声明的实例方法（包含所实现接口的默认方法）。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getInstanceMethods(): FixedArray<reflect.InstanceMethod>--><!--Device-Class-getInstanceMethods(): FixedArray<reflect.InstanceMethod>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;reflect.InstanceMethod&gt; | 由实例方法组成的定长数组。 |

## getInterfaces

```TypeScript
getInterfaces(): FixedArray<Class>
```

获取当前类实现的接口。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getInterfaces(): FixedArray<Class>--><!--Device-Class-getInterfaces(): FixedArray<Class>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | 该类所实现接口组成的定长数组。 |

## getLinker

```TypeScript
getLinker(): RuntimeLinker
```

获取与当前类关联的运行时链接器。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getLinker(): RuntimeLinker--><!--Device-Class-getLinker(): RuntimeLinker-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RuntimeLinker | 该类对应的运行时链接器。 |

## getName

```TypeScript
getName(): string
```

获取类在程序集中的名称。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getName(): string--><!--Device-Class-getName(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 类名。 |

## getStaticField

```TypeScript
getStaticField(name: string): reflect.StaticField | undefined
```

在当前类声明的字段中按名称查找静态字段。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getStaticField(name: string): reflect.StaticField | undefined--><!--Device-Class-getStaticField(name: string): reflect.StaticField | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 待查找的字段名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| reflect.StaticField \| undefined | 查找到的静态字段，未找到时返回undefined。 |

## getStaticFields

```TypeScript
getStaticFields(): FixedArray<reflect.StaticField>
```

获取当前类中声明的静态字段。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getStaticFields(): FixedArray<reflect.StaticField>--><!--Device-Class-getStaticFields(): FixedArray<reflect.StaticField>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;reflect.StaticField&gt; | 由静态字段组成的定长数组。 |

## getStaticMethod

```TypeScript
getStaticMethod(name: string, signature?: FixedArray<Class>): reflect.StaticMethod | undefined
```

在类中声明的方法中查找指定的静态方法。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getStaticMethod(name: string, signature?: FixedArray<Class>): reflect.StaticMethod | undefined--><!--Device-Class-getStaticMethod(name: string, signature?: FixedArray<Class>): reflect.StaticMethod | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 待查找的方法名。 |
| signature | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | 否 | 用于确定方法签名的参数类型数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| reflect.StaticMethod \| undefined | 查找到的静态方法，未找到时返回undefined。 |

## getStaticMethods

```TypeScript
getStaticMethods(): FixedArray<reflect.StaticMethod>
```

获取类中声明的静态方法。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getStaticMethods(): FixedArray<reflect.StaticMethod>--><!--Device-Class-getStaticMethods(): FixedArray<reflect.StaticMethod>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;reflect.StaticMethod&gt; | 由静态方法组成的定长数组。 |

## getSuper

```TypeScript
getSuper(): Class | undefined
```

获取类的父类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getSuper(): Class | undefined--><!--Device-Class-getSuper(): Class | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) \| undefined | 父类。 |

## getUnionConstituentTypes

```TypeScript
getUnionConstituentTypes(): FixedArray<Class> | undefined
```

获取联合类型类的所有组成类型。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getUnionConstituentTypes(): FixedArray<Class> | undefined--><!--Device-Class-getUnionConstituentTypes(): FixedArray<Class> | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; \| undefined | 由各组成类型构成的定长数组； 如果当前类不是联合类型类，则返回undefined。 |

## initialize

```TypeScript
initialize(): void
```

如果类尚未初始化，则调用一次类初始化器。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-initialize(): void--><!--Device-Class-initialize(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## isAbstract

```TypeScript
isAbstract(): boolean
```

判断该类是否为抽象类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isAbstract(): boolean--><!--Device-Class-isAbstract(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该类是抽象类则返回true，否则返回false。 |

## isEnum

```TypeScript
isEnum(): boolean
```

判断当前类是否为枚举。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isEnum(): boolean--><!--Device-Class-isEnum(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前类是枚举则返回true，否则返回false。 |

## isFinal

```TypeScript
isFinal(): boolean
```

判断该类是否为final类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isFinal(): boolean--><!--Device-Class-isFinal(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该类是final类则返回true，否则返回false。 |

## isFixedArray

```TypeScript
isFixedArray(): boolean
```

判断当前类是否为定长数组。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isFixedArray(): boolean--><!--Device-Class-isFixedArray(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前类是定长数组则返回true，否则返回false。 |

## isInterface

```TypeScript
isInterface(): boolean
```

判断当前类是否为接口。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isInterface(): boolean--><!--Device-Class-isInterface(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前类是接口则返回true，否则返回false。 |

## isNamespace

```TypeScript
public isNamespace(): boolean
```

判断当前类是否为命名空间。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public isNamespace(): boolean--><!--Device-Class-public isNamespace(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前类是命名空间则返回true，否则返回false。 |

## isPrimitive

```TypeScript
isPrimitive(): boolean
```

判断该类是否对应基本类型。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isPrimitive(): boolean--><!--Device-Class-isPrimitive(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该类对应基本类型则返回true，否则返回false。 |

## isSubtypeOf

```TypeScript
isSubtypeOf(other: Class): boolean
```

判断当前类是否为另一个类的子类型。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isSubtypeOf(other: Class): boolean--><!--Device-Class-isSubtypeOf(other: Class): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Class](arkts-arkts-class-c.md) | 是 | 用于比较的类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前类是另一个类的子类型则返回true，否则返回false。 |

## isUnion

```TypeScript
isUnion(): boolean
```

判断当前类是否为联合类型。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isUnion(): boolean--><!--Device-Class-isUnion(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前类是联合类型则返回true，否则返回false。 |

## of

```TypeScript
static of(obj: Object | null): Class
```

获取对象的类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-static of(obj: Object | null): Class--><!--Device-Class-static of(obj: Object | null): Class-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Object \| null | 是 | 待获取类信息的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | 该对象的类。 |

## ofAny

```TypeScript
static ofAny(obj: Any): Class | undefined
```

获取任意类型对象的类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-static ofAny(obj: Any): Class | undefined--><!--Device-Class-static ofAny(obj: Any): Class | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | 待获取类信息的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) \| undefined | 该对象的类；如果该对象不是类实例，则返回undefined。 |

## ofCaller

```TypeScript
static ofCaller(): Class | undefined
```

获取调用者的类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-static ofCaller(): Class | undefined--><!--Device-Class-static ofCaller(): Class | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) \| undefined | 调用者的类；如果不存在调用者的托管栈帧，则返回undefined。 |

## PRIMITIVE_BOOLEAN

```TypeScript
public static readonly PRIMITIVE_BOOLEAN: Class
```

保存boolean基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_BOOLEAN: Class--><!--Device-Class-public static readonly PRIMITIVE_BOOLEAN: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_BYTE

```TypeScript
public static readonly PRIMITIVE_BYTE: Class
```

保存byte基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_BYTE: Class--><!--Device-Class-public static readonly PRIMITIVE_BYTE: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_CHAR

```TypeScript
public static readonly PRIMITIVE_CHAR: Class
```

保存char基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_CHAR: Class--><!--Device-Class-public static readonly PRIMITIVE_CHAR: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_DOUBLE

```TypeScript
public static readonly PRIMITIVE_DOUBLE: Class
```

保存double基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_DOUBLE: Class--><!--Device-Class-public static readonly PRIMITIVE_DOUBLE: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_FLOAT

```TypeScript
public static readonly PRIMITIVE_FLOAT: Class
```

保存float基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_FLOAT: Class--><!--Device-Class-public static readonly PRIMITIVE_FLOAT: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_INT

```TypeScript
public static readonly PRIMITIVE_INT: Class
```

保存int基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_INT: Class--><!--Device-Class-public static readonly PRIMITIVE_INT: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_LONG

```TypeScript
public static readonly PRIMITIVE_LONG: Class
```

保存long基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_LONG: Class--><!--Device-Class-public static readonly PRIMITIVE_LONG: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_NUMBER

```TypeScript
public static readonly PRIMITIVE_NUMBER: Class
```

保存number基本类型对应的Class对象（与double相同）。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_NUMBER: Class--><!--Device-Class-public static readonly PRIMITIVE_NUMBER: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_SHORT

```TypeScript
public static readonly PRIMITIVE_SHORT: Class
```

保存short基本类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_SHORT: Class--><!--Device-Class-public static readonly PRIMITIVE_SHORT: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_VOID

```TypeScript
public static readonly PRIMITIVE_VOID: Class
```

保存void类型对应的Class对象。

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_VOID: Class--><!--Device-Class-public static readonly PRIMITIVE_VOID: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

