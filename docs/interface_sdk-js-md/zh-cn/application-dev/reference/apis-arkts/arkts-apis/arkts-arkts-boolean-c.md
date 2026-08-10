# Boolean

Represents boxed boolean value and related operations

**继承/实现关系：** Boolean extends [Object](arkts-arkts-object-c.md) implements [Comparable<boolean>](Comparable<boolean>)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Boolean extends Object implements Comparable<boolean>--><!--Device-unnamed-export class Boolean extends Object implements Comparable<boolean>-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(): boolean
```

Creates a new instance of a Boolean based on the specified value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-static $_invoke(): boolean--><!--Device-Boolean-static $_invoke(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | A new Boolean instance representing the specified value. |

## $_invoke

```TypeScript
static $_invoke<T>(value: T): boolean
```

Creates a new instance of a Boolean based on the specified value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-static $_invoke<T>(value: T): boolean--><!--Device-Boolean-static $_invoke<T>(value: T): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | The value that can be represented in Boolean. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | A new Boolean instance representing the specified value. |

## and

```TypeScript
public and(other: Boolean): Boolean
```

Does logical `and` on this instance and provided instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public and(other: Boolean): Boolean--><!--Device-Boolean-public and(other: Boolean): Boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Boolean | 是 | provided instance |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean | The logical AND result of both Boolean instances |

## compareTo

```TypeScript
public compareTo(other: Boolean): int
```

Compares this instance to other Boolean object The result is less than 0 if this instance lesser than provided object 0 if they are equal and greater than 0 otherwise.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public compareTo(other: Boolean): int--><!--Device-Boolean-public compareTo(other: Boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Boolean | 是 | Boolean object to compare with |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Negative if this &lt; other,0 if equal, positive if this &gt; other |

## constructor

```TypeScript
constructor(value: boolean)
```

Constructs a new Boolean with provided value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: boolean)--><!--Device-Boolean-constructor(value: boolean)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | value to construct class instance with |

## constructor

```TypeScript
constructor(value: byte)
```

Constructs a new Boolean with provided byte value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: byte)--><!--Device-Boolean-constructor(value: byte)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | value to construct class instance with |

## constructor

```TypeScript
constructor(value: char)
```

Constructs a new Boolean with provided char value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: char)--><!--Device-Boolean-constructor(value: char)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | value to construct class instance with |

## constructor

```TypeScript
constructor(value: short)
```

Constructs a new Boolean with provided short value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: short)--><!--Device-Boolean-constructor(value: short)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | value to construct class instance with |

## constructor

```TypeScript
constructor(value: int)
```

Constructs a new Boolean with provided int value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: int)--><!--Device-Boolean-constructor(value: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | value to construct class instance with &lt;br&gt;The value should be an integer. |

## constructor

```TypeScript
constructor(value: long)
```

Constructs a new Boolean with provided long value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: long)--><!--Device-Boolean-constructor(value: long)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | value to construct class instance with |

## constructor

```TypeScript
constructor(value: bigint)
```

Constructs a new Boolean with provided bigint value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: bigint)--><!--Device-Boolean-constructor(value: bigint)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint | 是 | value to construct class instance with |

## constructor

```TypeScript
constructor(value: float)
```

Constructs a new Boolean with provided float value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: float)--><!--Device-Boolean-constructor(value: float)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | value to construct class instance with |

## constructor

```TypeScript
public constructor(value: double)
```

Constructs a new Boolean with provided number value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public constructor(value: double)--><!--Device-Boolean-public constructor(value: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | value to construct class instance with |

## constructor

```TypeScript
constructor(value: string)
```

Constructs a new Boolean with provided string value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: string)--><!--Device-Boolean-constructor(value: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | value to construct class instance with |

## constructor

```TypeScript
constructor(value: Any = undefined)
```

Constructs a new Boolean with provided Object value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: Any = undefined)--><!--Device-Boolean-constructor(value: Any = undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Any | 是 | value to construct class instance with |

## equals

```TypeScript
public equals(other: Any): boolean
```

Checks for equality this instance with provided object, treated as a Boolean Returns false if type of provided object is not the same as this type

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public equals(other: Any): boolean--><!--Device-Boolean-public equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | object to be checked against |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the objects are equal, false otherwise |

## isFalse

```TypeScript
public isFalse(): boolean
```

Checks if this instance is false

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public isFalse(): boolean--><!--Device-Boolean-public isFalse(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the instance value is false, false otherwise |

## isTrue

```TypeScript
public isTrue(): boolean
```

Checks if this instance is true

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public isTrue(): boolean--><!--Device-Boolean-public isTrue(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the instance value is true, false otherwise |

## negate

```TypeScript
public negate(): Boolean
```

Inverts this instance value

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public negate(): Boolean--><!--Device-Boolean-public negate(): Boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean | The logical negation of this Boolean instance |

## or

```TypeScript
public or(other: Boolean): Boolean
```

Does logical `or` on this instance and provided instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public or(other: Boolean): Boolean--><!--Device-Boolean-public or(other: Boolean): Boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Boolean | 是 | provided instance |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean | The logical OR result of both Boolean instances |

## toBoolean

```TypeScript
static toBoolean(value: boolean): boolean
```

Returns the primitive as boolean value

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-static toBoolean(value: boolean): boolean--><!--Device-Boolean-static toBoolean(value: boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | value to cast |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns the input boolean value unchanged. |

## toBoolean

```TypeScript
toBoolean(): boolean
```

Returns value of this instance

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-toBoolean(): boolean--><!--Device-Boolean-toBoolean(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | The instance value converted to boolean. |

## toString

```TypeScript
public static toString(v: boolean): string
```

Converts the primitive to a string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public static toString(v: boolean): string--><!--Device-Boolean-public static toString(v: boolean): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | boolean | 是 | value to be converted |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The string representation of the boolean value |

## toString

```TypeScript
public toString(): string
```

Converts this object to a string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public toString(): string--><!--Device-Boolean-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The string representation of this Boolean object |

## xor

```TypeScript
public xor(other: Boolean): Boolean
```

Does `xor` on this instance and provided instance

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public xor(other: Boolean): Boolean--><!--Device-Boolean-public xor(other: Boolean): Boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Boolean | 是 | provided instance |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean | The logical XOR result of both Boolean instances |

