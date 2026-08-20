# Class

Class used to describe runtime types

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-unnamed-export class Class--><!--Device-unnamed-export class Class-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## createInstance

```TypeScript
createInstance(): Object
```

Create a new instance of this class and invokes its parameterless constructor.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-createInstance(): Object--><!--Device-Class-createInstance(): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Object | a new instance of this class. |

## current

```TypeScript
static current(): Class
```

Get current class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-static current(): Class--><!--Device-Class-static current(): Class-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | the current class. |

## from

```TypeScript
static from<T>(): Class
```

Get the class of an object.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-static from<T>(): Class--><!--Device-Class-static from<T>(): Class-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | the class of the object. |

## getConstructors

```TypeScript
getConstructors(): FixedArray<reflect.Constructor>
```

Get all constructors of a class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getConstructors(): FixedArray<reflect.Constructor>--><!--Device-Class-getConstructors(): FixedArray<reflect.Constructor>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| FixedArray&lt;reflect.Constructor&gt; | a fixed array of constructors. |

## getDescriptor

```TypeScript
getDescriptor(): string
```

Get the description.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getDescriptor(): string--><!--Device-Class-getDescriptor(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | a desceription. |

## getFixedArrayComponentType

```TypeScript
getFixedArrayComponentType(): Class | undefined
```

Get the component type of this class if it is a fixed array.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getFixedArrayComponentType(): Class | undefined--><!--Device-Class-getFixedArrayComponentType(): Class | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [Class](arkts-arkts-class-c.md) \| undefined | the component type of the fixed array, or undefined if this class is not a fixed array. |

## getInstanceField

```TypeScript
getInstanceField(name: string): reflect.InstanceField | undefined
```

Look up a instance field by name among the fields declared in this class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getInstanceField(name: string): reflect.InstanceField | undefined--><!--Device-Class-getInstanceField(name: string): reflect.InstanceField | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | The field name to search for. |

**Return value:**

| Type | Description |
| --- | --- |
| reflect.InstanceField \| undefined | the found instance field, or undefined if not found. |

## getInstanceFields

```TypeScript
getInstanceFields(): FixedArray<reflect.InstanceField>
```

Get instance fields declared in the class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getInstanceFields(): FixedArray<reflect.InstanceField>--><!--Device-Class-getInstanceFields(): FixedArray<reflect.InstanceField>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| FixedArray&lt;reflect.InstanceField&gt; | a fixed array of instance fields. |

## getInstanceMethod

```TypeScript
getInstanceMethod(name: string, signature?: FixedArray<Class>): reflect.InstanceMethod | undefined
```

Look up a instance method (including default methods from implemented interfaces) among the methods declared in the class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getInstanceMethod(name: string, signature?: FixedArray<Class>): reflect.InstanceMethod | undefined--><!--Device-Class-getInstanceMethod(name: string, signature?: FixedArray<Class>): reflect.InstanceMethod | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | The method name to search for. |
| signature | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | No | Array of parameter classes defining the method signature. |

**Return value:**

| Type | Description |
| --- | --- |
| reflect.InstanceMethod \| undefined | the found instance method, or undefined if not found. |

## getInstanceMethods

```TypeScript
getInstanceMethods(): FixedArray<reflect.InstanceMethod>
```

Get instance methods (including default methods from implemented interfaces) declared in the class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getInstanceMethods(): FixedArray<reflect.InstanceMethod>--><!--Device-Class-getInstanceMethods(): FixedArray<reflect.InstanceMethod>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| FixedArray&lt;reflect.InstanceMethod&gt; | a fixed array of instance methods. |

## getInterfaces

```TypeScript
getInterfaces(): FixedArray<Class>
```

Get the interfaces implemented by this class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getInterfaces(): FixedArray<Class>--><!--Device-Class-getInterfaces(): FixedArray<Class>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | a fixed array of interfaces implemented by the class. |

## getLinker

```TypeScript
getLinker(): RuntimeLinker
```

Get the runtime linker associated with this class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getLinker(): RuntimeLinker--><!--Device-Class-getLinker(): RuntimeLinker-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| RuntimeLinker | the runtime linker for this class |

## getName

```TypeScript
getName(): string
```

Get the name of a class in assembly

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getName(): string--><!--Device-Class-getName(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | return class name |

## getStaticField

```TypeScript
getStaticField(name: string): reflect.StaticField | undefined
```

Look up a static field by name among the fields declared in this class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getStaticField(name: string): reflect.StaticField | undefined--><!--Device-Class-getStaticField(name: string): reflect.StaticField | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | The field name to search for. |

**Return value:**

| Type | Description |
| --- | --- |
| reflect.StaticField \| undefined | the found static field, or undefined if not found. |

## getStaticFields

```TypeScript
getStaticFields(): FixedArray<reflect.StaticField>
```

Get static fields declared in this class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getStaticFields(): FixedArray<reflect.StaticField>--><!--Device-Class-getStaticFields(): FixedArray<reflect.StaticField>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| FixedArray&lt;reflect.StaticField&gt; | a fixed array of static fields. |

## getStaticMethod

```TypeScript
getStaticMethod(name: string, signature?: FixedArray<Class>): reflect.StaticMethod | undefined
```

Look up a static method among the methods declared in the class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getStaticMethod(name: string, signature?: FixedArray<Class>): reflect.StaticMethod | undefined--><!--Device-Class-getStaticMethod(name: string, signature?: FixedArray<Class>): reflect.StaticMethod | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | The method name to search for. |
| signature | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | No | Array of parameter classes defining the method signature. |

**Return value:**

| Type | Description |
| --- | --- |
| reflect.StaticMethod \| undefined | the found static method, or undefined if not found. |

## getStaticMethods

```TypeScript
getStaticMethods(): FixedArray<reflect.StaticMethod>
```

Get static methods declared in the class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getStaticMethods(): FixedArray<reflect.StaticMethod>--><!--Device-Class-getStaticMethods(): FixedArray<reflect.StaticMethod>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| FixedArray&lt;reflect.StaticMethod&gt; | a fixed array of static methods. |

## getSuper

```TypeScript
getSuper(): Class | undefined
```

Get the super class of a class

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getSuper(): Class | undefined--><!--Device-Class-getSuper(): Class | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [Class](arkts-arkts-class-c.md) \| undefined | return the super class |

## getUnionConstituentTypes

```TypeScript
getUnionConstituentTypes(): FixedArray<Class> | undefined
```

Get all constituent types of a union class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-getUnionConstituentTypes(): FixedArray<Class> | undefined--><!--Device-Class-getUnionConstituentTypes(): FixedArray<Class> | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; \| undefined | a fixed array of constituent types, or undefined if this is not a union class. |

## initialize

```TypeScript
initialize(): void
```

Invoke class initializer once if class is not initialized.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-initialize(): void--><!--Device-Class-initialize(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## isAbstract

```TypeScript
isAbstract(): boolean
```

Check the class is abstract

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-isAbstract(): boolean--><!--Device-Class-isAbstract(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the class is abstract |

## isEnum

```TypeScript
isEnum(): boolean
```

Check if this class is an enum.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-isEnum(): boolean--><!--Device-Class-isEnum(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this class is an enum, false otherwise. |

## isFinal

```TypeScript
isFinal(): boolean
```

Check the class is final

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-isFinal(): boolean--><!--Device-Class-isFinal(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the class is fianl |

## isFixedArray

```TypeScript
isFixedArray(): boolean
```

Check if this class is a fixed array.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-isFixedArray(): boolean--><!--Device-Class-isFixedArray(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this class is a fixed array, false otherwise. |

## isInterface

```TypeScript
isInterface(): boolean
```

Check if this class is an interface.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-isInterface(): boolean--><!--Device-Class-isInterface(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this class is an interface, false otherwise. |

## isNamespace

```TypeScript
public isNamespace(): boolean
```

Checks if this class is a namespace.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-public isNamespace(): boolean--><!--Device-Class-public isNamespace(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this class is a namespace. |

## isPrimitive

```TypeScript
isPrimitive(): boolean
```

Check if class is primitive type

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-isPrimitive(): boolean--><!--Device-Class-isPrimitive(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the class corresponds to a primitive type |

## isSubtypeOf

```TypeScript
isSubtypeOf(other: Class): boolean
```

Check if this class is a subtype of another class.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-isSubtypeOf(other: Class): boolean--><!--Device-Class-isSubtypeOf(other: Class): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [Class](arkts-arkts-class-c.md) | Yes | The class to check against. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if this class is a subtype of the other class, false otherwise. |

## isUnion

```TypeScript
isUnion(): boolean
```

Check if this class is a union type.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-isUnion(): boolean--><!--Device-Class-isUnion(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if this class is a union type, false otherwise. |

## of

```TypeScript
static of(obj: Object | null): Class
```

Get the class of an object.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-static of(obj: Object | null): Class--><!--Device-Class-static of(obj: Object | null): Class-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Object \| null | Yes | The object to get the class from. |

**Return value:**

| Type | Description |
| --- | --- |
| [Class](arkts-arkts-class-c.md) | the class of the object. |

## ofAny

```TypeScript
static ofAny(obj: Any): Class | undefined
```

Get the class of an object of any type.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-static ofAny(obj: Any): Class | undefined--><!--Device-Class-static ofAny(obj: Any): Class | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Any | Yes | The object to get the class from. |

**Return value:**

| Type | Description |
| --- | --- |
| [Class](arkts-arkts-class-c.md) \| undefined | the class of the object, or undefined if the object is not a class instance. |

## ofCaller

```TypeScript
static ofCaller(): Class | undefined
```

Get class of caller.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-static ofCaller(): Class | undefined--><!--Device-Class-static ofCaller(): Class | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [Class](arkts-arkts-class-c.md) \| undefined | the class of the caller, or undefined if there is no caller managed frame. |

## PRIMITIVE_BOOLEAN

```TypeScript
public static readonly PRIMITIVE_BOOLEAN: Class
```

Stores Class of boolean primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-public static readonly PRIMITIVE_BOOLEAN: Class--><!--Device-Class-public static readonly PRIMITIVE_BOOLEAN: Class-End-->

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_BYTE

```TypeScript
public static readonly PRIMITIVE_BYTE: Class
```

Stores Class of byte primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-public static readonly PRIMITIVE_BYTE: Class--><!--Device-Class-public static readonly PRIMITIVE_BYTE: Class-End-->

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_CHAR

```TypeScript
public static readonly PRIMITIVE_CHAR: Class
```

Stores Class of char primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-public static readonly PRIMITIVE_CHAR: Class--><!--Device-Class-public static readonly PRIMITIVE_CHAR: Class-End-->

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_DOUBLE

```TypeScript
public static readonly PRIMITIVE_DOUBLE: Class
```

Stores Class of double primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-public static readonly PRIMITIVE_DOUBLE: Class--><!--Device-Class-public static readonly PRIMITIVE_DOUBLE: Class-End-->

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_FLOAT

```TypeScript
public static readonly PRIMITIVE_FLOAT: Class
```

Stores Class of float primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-public static readonly PRIMITIVE_FLOAT: Class--><!--Device-Class-public static readonly PRIMITIVE_FLOAT: Class-End-->

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_INT

```TypeScript
public static readonly PRIMITIVE_INT: Class
```

Stores Class of int primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-public static readonly PRIMITIVE_INT: Class--><!--Device-Class-public static readonly PRIMITIVE_INT: Class-End-->

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_LONG

```TypeScript
public static readonly PRIMITIVE_LONG: Class
```

Stores Class of long primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-public static readonly PRIMITIVE_LONG: Class--><!--Device-Class-public static readonly PRIMITIVE_LONG: Class-End-->

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_NUMBER

```TypeScript
public static readonly PRIMITIVE_NUMBER: Class
```

Stores Class of number primitive type (same as double).

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-public static readonly PRIMITIVE_NUMBER: Class--><!--Device-Class-public static readonly PRIMITIVE_NUMBER: Class-End-->

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_SHORT

```TypeScript
public static readonly PRIMITIVE_SHORT: Class
```

Stores Class of short primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-public static readonly PRIMITIVE_SHORT: Class--><!--Device-Class-public static readonly PRIMITIVE_SHORT: Class-End-->

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_VOID

```TypeScript
public static readonly PRIMITIVE_VOID: Class
```

Stores Class of void type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Class-public static readonly PRIMITIVE_VOID: Class--><!--Device-Class-public static readonly PRIMITIVE_VOID: Class-End-->

**System capability:** SystemCapability.Utils.Lang

