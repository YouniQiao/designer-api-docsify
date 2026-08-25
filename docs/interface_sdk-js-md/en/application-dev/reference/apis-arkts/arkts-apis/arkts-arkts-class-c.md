# Class

Class used to describe runtime types

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

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

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Object |

## current

```TypeScript
static current(): Class
```

Get current class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Class](arkts-arkts-class-c.md) |

## from

```TypeScript
static from<T>(): Class
```

Get the class of an object.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Class](arkts-arkts-class-c.md) |

## getConstructors

```TypeScript
getConstructors(): FixedArray<reflect.Constructor>
```

Get all constructors of a class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| FixedArray & lt;reflect.Constructor & gt; |

## getDescriptor

```TypeScript
getDescriptor(): string
```

Get the description.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## getFixedArrayComponentType

```TypeScript
getFixedArrayComponentType(): Class | undefined
```

Get the component type of this class if it is a fixed array.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Class](arkts-arkts-class-c.md) \| undefined |

## getInstanceField

```TypeScript
getInstanceField(name: string): reflect.InstanceField | undefined
```

Look up a instance field by name among the fields declared in this class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| reflect.InstanceField \| undefined |

## getInstanceFields

```TypeScript
getInstanceFields(): FixedArray<reflect.InstanceField>
```

Get instance fields declared in the class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| FixedArray & lt;reflect.InstanceField & gt; |

## getInstanceMethod

```TypeScript
getInstanceMethod(name: string, signature?: FixedArray<Class>): reflect.InstanceMethod | undefined
```

Look up a instance method (including default methods from implemented interfaces) among the methods declared in the class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| signature | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| reflect.InstanceMethod \| undefined |

## getInstanceMethods

```TypeScript
getInstanceMethods(): FixedArray<reflect.InstanceMethod>
```

Get instance methods (including default methods from implemented interfaces) declared in the class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| FixedArray & lt;reflect.InstanceMethod & gt; |

## getInterfaces

```TypeScript
getInterfaces(): FixedArray<Class>
```

Get the interfaces implemented by this class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; |

## getLinker

```TypeScript
getLinker(): RuntimeLinker
```

Get the runtime linker associated with this class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| RuntimeLinker |

## getName

```TypeScript
getName(): string
```

Get the name of a class in assembly

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## getStaticField

```TypeScript
getStaticField(name: string): reflect.StaticField | undefined
```

Look up a static field by name among the fields declared in this class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| reflect.StaticField \| undefined |

## getStaticFields

```TypeScript
getStaticFields(): FixedArray<reflect.StaticField>
```

Get static fields declared in this class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| FixedArray & lt;reflect.StaticField & gt; |

## getStaticMethod

```TypeScript
getStaticMethod(name: string, signature?: FixedArray<Class>): reflect.StaticMethod | undefined
```

Look up a static method among the methods declared in the class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| signature | FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| reflect.StaticMethod \| undefined |

## getStaticMethods

```TypeScript
getStaticMethods(): FixedArray<reflect.StaticMethod>
```

Get static methods declared in the class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| FixedArray & lt;reflect.StaticMethod & gt; |

## getSuper

```TypeScript
getSuper(): Class | undefined
```

Get the super class of a class

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Class](arkts-arkts-class-c.md) \| undefined |

## getUnionConstituentTypes

```TypeScript
getUnionConstituentTypes(): FixedArray<Class> | undefined
```

Get all constituent types of a union class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| FixedArray&lt;[Class](arkts-arkts-class-c.md)&gt; \| undefined |

## initialize

```TypeScript
initialize(): void
```

Invoke class initializer once if class is not initialized.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## isAbstract

```TypeScript
isAbstract(): boolean
```

Check the class is abstract

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isEnum

```TypeScript
isEnum(): boolean
```

Check if this class is an enum.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isFinal

```TypeScript
isFinal(): boolean
```

Check the class is final

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isFixedArray

```TypeScript
isFixedArray(): boolean
```

Check if this class is a fixed array.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isInterface

```TypeScript
isInterface(): boolean
```

Check if this class is an interface.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isNamespace

```TypeScript
public isNamespace(): boolean
```

Checks if this class is a namespace.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isPrimitive

```TypeScript
isPrimitive(): boolean
```

Check if class is primitive type

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isSubtypeOf

```TypeScript
isSubtypeOf(other: Class): boolean
```

Check if this class is a subtype of another class.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | [Class](arkts-arkts-class-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isUnion

```TypeScript
isUnion(): boolean
```

Check if this class is a union type.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## of

```TypeScript
static of(obj: Object | null): Class
```

Get the class of an object.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | Object \| null | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Class](arkts-arkts-class-c.md) |

## ofAny

```TypeScript
static ofAny(obj: Any): Class | undefined
```

Get the class of an object of any type.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | Any | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Class](arkts-arkts-class-c.md) \| undefined |

## ofCaller

```TypeScript
static ofCaller(): Class | undefined
```

Get class of caller.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Class](arkts-arkts-class-c.md) \| undefined |

## PRIMITIVE_BOOLEAN

```TypeScript
public static readonly PRIMITIVE_BOOLEAN: Class
```

Stores Class of boolean primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_BYTE

```TypeScript
public static readonly PRIMITIVE_BYTE: Class
```

Stores Class of byte primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_CHAR

```TypeScript
public static readonly PRIMITIVE_CHAR: Class
```

Stores Class of char primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_DOUBLE

```TypeScript
public static readonly PRIMITIVE_DOUBLE: Class
```

Stores Class of double primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_FLOAT

```TypeScript
public static readonly PRIMITIVE_FLOAT: Class
```

Stores Class of float primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_INT

```TypeScript
public static readonly PRIMITIVE_INT: Class
```

Stores Class of int primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_LONG

```TypeScript
public static readonly PRIMITIVE_LONG: Class
```

Stores Class of long primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_NUMBER

```TypeScript
public static readonly PRIMITIVE_NUMBER: Class
```

Stores Class of number primitive type (same as double).

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_SHORT

```TypeScript
public static readonly PRIMITIVE_SHORT: Class
```

Stores Class of short primitive type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## PRIMITIVE_VOID

```TypeScript
public static readonly PRIMITIVE_VOID: Class
```

Stores Class of void type.

**Type:** [Class](arkts-arkts-class-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang
