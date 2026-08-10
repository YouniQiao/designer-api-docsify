# Class

Class used to describe runtime types

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Class--><!--Device-unnamed-export class Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## createInstance

```TypeScript
createInstance(): Object
```

Create a new instance of this class and invokes its parameterless constructor.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-createInstance(): Object--><!--Device-Class-createInstance(): Object-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | a new instance of this class. |

## current

```TypeScript
static current(): Class
```

Get current class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-static current(): Class--><!--Device-Class-static current(): Class-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | the current class. |

## from

```TypeScript
static from<T>(): Class
```

Get the class of an object.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-static from<T>(): Class--><!--Device-Class-static from<T>(): Class-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | the class of the object. |

## getConstructors

```TypeScript
getConstructors(): FixedArray<reflect.Constructor>
```

Get all constructors of a class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getConstructors(): FixedArray<reflect.Constructor>--><!--Device-Class-getConstructors(): FixedArray<reflect.Constructor>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;reflect.Constructor&gt; | a fixed array of constructors. |

## getDescriptor

```TypeScript
getDescriptor(): string
```

Get the description.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getDescriptor(): string--><!--Device-Class-getDescriptor(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | a desceription. |

## getFixedArrayComponentType

```TypeScript
getFixedArrayComponentType(): Class | undefined
```

Get the component type of this class if it is a fixed array.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getFixedArrayComponentType(): Class | undefined--><!--Device-Class-getFixedArrayComponentType(): Class | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | the component type of the fixed array, or undefined if this class is not a fixed array. |

## getInstanceField

```TypeScript
getInstanceField(name: string): reflect.InstanceField | undefined
```

Look up a instance field by name among the fields declared in this class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getInstanceField(name: string): reflect.InstanceField | undefined--><!--Device-Class-getInstanceField(name: string): reflect.InstanceField | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | The field name to search for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| reflect.InstanceField | the found instance field, or undefined if not found. |

## getInstanceFields

```TypeScript
getInstanceFields(): FixedArray<reflect.InstanceField>
```

Get instance fields declared in the class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getInstanceFields(): FixedArray<reflect.InstanceField>--><!--Device-Class-getInstanceFields(): FixedArray<reflect.InstanceField>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;reflect.InstanceField&gt; | a fixed array of instance fields. |

## getInstanceMethod

```TypeScript
getInstanceMethod(name: string, signature?: FixedArray<Class>): reflect.InstanceMethod | undefined
```

Look up a instance method (including default methods from implemented interfaces) among the methods declared in the class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getInstanceMethod(name: string, signature?: FixedArray<Class>): reflect.InstanceMethod | undefined--><!--Device-Class-getInstanceMethod(name: string, signature?: FixedArray<Class>): reflect.InstanceMethod | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | The method name to search for. |
| signature | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | 否 | Array of parameter classes defining the method signature. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| reflect.InstanceMethod | the found instance method, or undefined if not found. |

## getInstanceMethods

```TypeScript
getInstanceMethods(): FixedArray<reflect.InstanceMethod>
```

Get instance methods (including default methods from implemented interfaces) declared in the class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getInstanceMethods(): FixedArray<reflect.InstanceMethod>--><!--Device-Class-getInstanceMethods(): FixedArray<reflect.InstanceMethod>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;reflect.InstanceMethod&gt; | a fixed array of instance methods. |

## getInterfaces

```TypeScript
getInterfaces(): FixedArray<Class>
```

Get the interfaces implemented by this class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getInterfaces(): FixedArray<Class>--><!--Device-Class-getInterfaces(): FixedArray<Class>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | a fixed array of interfaces implemented by the class. |

## getLinker

```TypeScript
getLinker(): RuntimeLinker
```

Get the runtime linker associated with this class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getLinker(): RuntimeLinker--><!--Device-Class-getLinker(): RuntimeLinker-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| RuntimeLinker | the runtime linker for this class |

## getName

```TypeScript
getName(): string
```

Get the name of a class in assembly

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getName(): string--><!--Device-Class-getName(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | return class name |

## getStaticField

```TypeScript
getStaticField(name: string): reflect.StaticField | undefined
```

Look up a static field by name among the fields declared in this class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getStaticField(name: string): reflect.StaticField | undefined--><!--Device-Class-getStaticField(name: string): reflect.StaticField | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | The field name to search for. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| reflect.StaticField | the found static field, or undefined if not found. |

## getStaticFields

```TypeScript
getStaticFields(): FixedArray<reflect.StaticField>
```

Get static fields declared in this class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getStaticFields(): FixedArray<reflect.StaticField>--><!--Device-Class-getStaticFields(): FixedArray<reflect.StaticField>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;reflect.StaticField&gt; | a fixed array of static fields. |

## getStaticMethod

```TypeScript
getStaticMethod(name: string, signature?: FixedArray<Class>): reflect.StaticMethod | undefined
```

Look up a static method among the methods declared in the class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getStaticMethod(name: string, signature?: FixedArray<Class>): reflect.StaticMethod | undefined--><!--Device-Class-getStaticMethod(name: string, signature?: FixedArray<Class>): reflect.StaticMethod | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | The method name to search for. |
| signature | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | 否 | Array of parameter classes defining the method signature. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| reflect.StaticMethod | the found static method, or undefined if not found. |

## getStaticMethods

```TypeScript
getStaticMethods(): FixedArray<reflect.StaticMethod>
```

Get static methods declared in the class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getStaticMethods(): FixedArray<reflect.StaticMethod>--><!--Device-Class-getStaticMethods(): FixedArray<reflect.StaticMethod>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;reflect.StaticMethod&gt; | a fixed array of static methods. |

## getSuper

```TypeScript
getSuper(): Class | undefined
```

Get the super class of a class

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getSuper(): Class | undefined--><!--Device-Class-getSuper(): Class | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | return the super class |

## getUnionConstituentTypes

```TypeScript
getUnionConstituentTypes(): FixedArray<Class> | undefined
```

Get all constituent types of a union class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-getUnionConstituentTypes(): FixedArray<Class> | undefined--><!--Device-Class-getUnionConstituentTypes(): FixedArray<Class> | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | a fixed array of constituent types, or undefined if this is not a union class. |

## initialize

```TypeScript
initialize(): void
```

Invoke class initializer once if class is not initialized.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-initialize(): void--><!--Device-Class-initialize(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## isAbstract

```TypeScript
isAbstract(): boolean
```

Check the class is abstract

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isAbstract(): boolean--><!--Device-Class-isAbstract(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the class is abstract |

## isEnum

```TypeScript
isEnum(): boolean
```

Check if this class is an enum.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isEnum(): boolean--><!--Device-Class-isEnum(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this class is an enum, false otherwise. |

## isFinal

```TypeScript
isFinal(): boolean
```

Check the class is final

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isFinal(): boolean--><!--Device-Class-isFinal(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the class is fianl |

## isFixedArray

```TypeScript
isFixedArray(): boolean
```

Check if this class is a fixed array.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isFixedArray(): boolean--><!--Device-Class-isFixedArray(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this class is a fixed array, false otherwise. |

## isInterface

```TypeScript
isInterface(): boolean
```

Check if this class is an interface.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isInterface(): boolean--><!--Device-Class-isInterface(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this class is an interface, false otherwise. |

## isNamespace

```TypeScript
public isNamespace(): boolean
```

Checks if this class is a namespace.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public isNamespace(): boolean--><!--Device-Class-public isNamespace(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this class is a namespace. |

## isPrimitive

```TypeScript
isPrimitive(): boolean
```

Check if class is primitive type

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isPrimitive(): boolean--><!--Device-Class-isPrimitive(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if the class corresponds to a primitive type |

## isSubtypeOf

```TypeScript
isSubtypeOf(other: Class): boolean
```

Check if this class is a subtype of another class.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isSubtypeOf(other: Class): boolean--><!--Device-Class-isSubtypeOf(other: Class): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [Class](arkts-arkts-class-c.md) | 是 | The class to check against. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if this class is a subtype of the other class, false otherwise. |

## isUnion

```TypeScript
isUnion(): boolean
```

Check if this class is a union type.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-isUnion(): boolean--><!--Device-Class-isUnion(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true if this class is a union type, false otherwise. |

## of

```TypeScript
static of(obj: Object | null): Class
```

Get the class of an object.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-static of(obj: Object | null): Class--><!--Device-Class-static of(obj: Object | null): Class-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Object \| null | 是 | The object to get the class from. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | the class of the object. |

## ofAny

```TypeScript
static ofAny(obj: Any): Class | undefined
```

Get the class of an object of any type.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-static ofAny(obj: Any): Class | undefined--><!--Device-Class-static ofAny(obj: Any): Class | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | The object to get the class from. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | the class of the object, or undefined if the object is not a class instance. |

## ofCaller

```TypeScript
static ofCaller(): Class | undefined
```

Get class of caller.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-static ofCaller(): Class | undefined--><!--Device-Class-static ofCaller(): Class | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | the class of the caller, or undefined if there is no caller managed frame. |

## PRIMITIVE_BOOLEAN

```TypeScript
public static readonly PRIMITIVE_BOOLEAN: Class
```

Stores Class of boolean primitive type.

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_BOOLEAN: Class--><!--Device-Class-public static readonly PRIMITIVE_BOOLEAN: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_BYTE

```TypeScript
public static readonly PRIMITIVE_BYTE: Class
```

Stores Class of byte primitive type.

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_BYTE: Class--><!--Device-Class-public static readonly PRIMITIVE_BYTE: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_CHAR

```TypeScript
public static readonly PRIMITIVE_CHAR: Class
```

Stores Class of char primitive type.

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_CHAR: Class--><!--Device-Class-public static readonly PRIMITIVE_CHAR: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_DOUBLE

```TypeScript
public static readonly PRIMITIVE_DOUBLE: Class
```

Stores Class of double primitive type.

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_DOUBLE: Class--><!--Device-Class-public static readonly PRIMITIVE_DOUBLE: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_FLOAT

```TypeScript
public static readonly PRIMITIVE_FLOAT: Class
```

Stores Class of float primitive type.

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_FLOAT: Class--><!--Device-Class-public static readonly PRIMITIVE_FLOAT: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_INT

```TypeScript
public static readonly PRIMITIVE_INT: Class
```

Stores Class of int primitive type.

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_INT: Class--><!--Device-Class-public static readonly PRIMITIVE_INT: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_LONG

```TypeScript
public static readonly PRIMITIVE_LONG: Class
```

Stores Class of long primitive type.

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_LONG: Class--><!--Device-Class-public static readonly PRIMITIVE_LONG: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_NUMBER

```TypeScript
public static readonly PRIMITIVE_NUMBER: Class
```

Stores Class of number primitive type (same as double).

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_NUMBER: Class--><!--Device-Class-public static readonly PRIMITIVE_NUMBER: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_SHORT

```TypeScript
public static readonly PRIMITIVE_SHORT: Class
```

Stores Class of short primitive type.

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_SHORT: Class--><!--Device-Class-public static readonly PRIMITIVE_SHORT: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

## PRIMITIVE_VOID

```TypeScript
public static readonly PRIMITIVE_VOID: Class
```

Stores Class of void type.

**类型：** [Class](arkts-arkts-class-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Class-public static readonly PRIMITIVE_VOID: Class--><!--Device-Class-public static readonly PRIMITIVE_VOID: Class-End-->

**系统能力：** SystemCapability.Utils.Lang

