# Boolean

Represents boxed boolean value and related operations

**Inheritance/Implementation:** Boolean extends [Object](../../../apis-na/arkts-apis/arkts-na-dynamic/lib-es5-object-i.md) and implements [Comparable<boolean>](Comparable<boolean>)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export class Boolean extends Object implements Comparable<boolean>--><!--Device-unnamed-export class Boolean extends Object implements Comparable<boolean>-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(): boolean
```

Creates a new instance of a Boolean based on the specified value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-static $_invoke(): boolean--><!--Device-Boolean-static $_invoke(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | A new Boolean instance representing the specified value. |

## $_invoke

```TypeScript
static $_invoke<T>(value: T): boolean
```

Creates a new instance of a Boolean based on the specified value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-static $_invoke<T>(value: T): boolean--><!--Device-Boolean-static $_invoke<T>(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The value that can be represented in Boolean. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | A new Boolean instance representing the specified value. |

## and

```TypeScript
public and(other: Boolean): Boolean
```

Does logical \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ on this instance and provided instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-public and(other: Boolean): Boolean--><!--Device-Boolean-public and(other: Boolean): Boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Boolean | Yes | provided instance |

**Return value:**

| Type | Description |
| --- | --- |
| Boolean | The logical AND result of both Boolean instances |

## compareTo

```TypeScript
public compareTo(other: Boolean): int
```

Compares this instance to other Boolean object The result is less than 0 if this instance lesser than provided object 0 if they are equal and greater than 0 otherwise.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-public compareTo(other: Boolean): int--><!--Device-Boolean-public compareTo(other: Boolean): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Boolean | Yes | Boolean object to compare with |

**Return value:**

| Type | Description |
| --- | --- |
| int | Negative if this &lt; other,0 if equal, positive if this &gt; other |

## constructor

```TypeScript
constructor(value: boolean)
```

Constructs a new Boolean with provided value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-constructor(value: boolean)--><!--Device-Boolean-constructor(value: boolean)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | value to construct class instance with |

## constructor

```TypeScript
constructor(value: byte)
```

Constructs a new Boolean with provided byte value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-constructor(value: byte)--><!--Device-Boolean-constructor(value: byte)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | byte | Yes | value to construct class instance with |

## constructor

```TypeScript
constructor(value: char)
```

Constructs a new Boolean with provided char value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-constructor(value: char)--><!--Device-Boolean-constructor(value: char)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | char | Yes | value to construct class instance with |

## constructor

```TypeScript
constructor(value: short)
```

Constructs a new Boolean with provided short value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-constructor(value: short)--><!--Device-Boolean-constructor(value: short)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | short | Yes | value to construct class instance with |

## constructor

```TypeScript
constructor(value: int)
```

Constructs a new Boolean with provided int value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-constructor(value: int)--><!--Device-Boolean-constructor(value: int)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | value to construct class instance with\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

## constructor

```TypeScript
constructor(value: long)
```

Constructs a new Boolean with provided long value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-constructor(value: long)--><!--Device-Boolean-constructor(value: long)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | value to construct class instance with |

## constructor

```TypeScript
constructor(value: bigint)
```

Constructs a new Boolean with provided bigint value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-constructor(value: bigint)--><!--Device-Boolean-constructor(value: bigint)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | bigint | Yes | value to construct class instance with |

## constructor

```TypeScript
constructor(value: float)
```

Constructs a new Boolean with provided float value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-constructor(value: float)--><!--Device-Boolean-constructor(value: float)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | float | Yes | value to construct class instance with |

## constructor

```TypeScript
public constructor(value: double)
```

Constructs a new Boolean with provided number value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-public constructor(value: double)--><!--Device-Boolean-public constructor(value: double)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | value to construct class instance with |

## constructor

```TypeScript
constructor(value: string)
```

Constructs a new Boolean with provided string value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-constructor(value: string)--><!--Device-Boolean-constructor(value: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | value to construct class instance with |

## constructor

```TypeScript
constructor(value: Any = undefined)
```

Constructs a new Boolean with provided Object value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-constructor(value: Any = undefined)--><!--Device-Boolean-constructor(value: Any = undefined)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Any | Yes | value to construct class instance with |

## equals

```TypeScript
public equals(other: Any): boolean
```

Checks for equality this instance with provided object, treated as a Boolean Returns false if type of provided object is not the same as this type

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-public equals(other: Any): boolean--><!--Device-Boolean-public equals(other: Any): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Any | Yes | object to be checked against |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the objects are equal, false otherwise |

## isFalse

```TypeScript
public isFalse(): boolean
```

Checks if this instance is false

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-public isFalse(): boolean--><!--Device-Boolean-public isFalse(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the instance value is false, false otherwise |

## isTrue

```TypeScript
public isTrue(): boolean
```

Checks if this instance is true

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-public isTrue(): boolean--><!--Device-Boolean-public isTrue(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the instance value is true, false otherwise |

## negate

```TypeScript
public negate(): Boolean
```

Inverts this instance value

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-public negate(): Boolean--><!--Device-Boolean-public negate(): Boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Boolean | The logical negation of this Boolean instance |

## or

```TypeScript
public or(other: Boolean): Boolean
```

Does logical \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ on this instance and provided instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-public or(other: Boolean): Boolean--><!--Device-Boolean-public or(other: Boolean): Boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Boolean | Yes | provided instance |

**Return value:**

| Type | Description |
| --- | --- |
| Boolean | The logical OR result of both Boolean instances |

## toBoolean

```TypeScript
static toBoolean(value: boolean): boolean
```

Returns the primitive as boolean value

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-static toBoolean(value: boolean): boolean--><!--Device-Boolean-static toBoolean(value: boolean): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | value to cast |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns the input boolean value unchanged. |

## toBoolean

```TypeScript
toBoolean(): boolean
```

Returns value of this instance

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-toBoolean(): boolean--><!--Device-Boolean-toBoolean(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The instance value converted to boolean. |

## toString

```TypeScript
public static toString(v: boolean): string
```

Converts the primitive to a string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-public static toString(v: boolean): string--><!--Device-Boolean-public static toString(v: boolean): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | boolean | Yes | value to be converted |

**Return value:**

| Type | Description |
| --- | --- |
| string | The string representation of the boolean value |

## toString

```TypeScript
public toString(): string
```

Converts this object to a string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-public toString(): string--><!--Device-Boolean-public toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | The string representation of this Boolean object |

## xor

```TypeScript
public xor(other: Boolean): Boolean
```

Does \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ on this instance and provided instance

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Boolean-public xor(other: Boolean): Boolean--><!--Device-Boolean-public xor(other: Boolean): Boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | Boolean | Yes | provided instance |

**Return value:**

| Type | Description |
| --- | --- |
| Boolean | The logical XOR result of both Boolean instances |

