# Boolean

表示装箱后的boolean值及其相关操作。

**继承/实现关系：** Boolean extends [Object](arkts-arkts-object-c.md) implements Comparable<boolean>

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class Boolean--><!--Device-unnamed-export class Boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(): boolean
```

根据指定的值创建新的Boolean实例。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-static $_invoke(): boolean--><!--Device-Boolean-static $_invoke(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示指定值的新Boolean实例。 |

## $_invoke

```TypeScript
static $_invoke<T>(value: T): boolean
```

根据指定的值创建新的Boolean实例。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-static $_invoke<T>(value: T): boolean--><!--Device-Boolean-static $_invoke<T>(value: T): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 | 可用Boolean表示的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示指定值的新Boolean实例。 |

## and

```TypeScript
public and(other: Boolean): Boolean
```

对当前实例与传入实例做逻辑与运算。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public and(other: Boolean): Boolean--><!--Device-Boolean-public and(other: Boolean): Boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Boolean | 是 | 传入的实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean | 两个Boolean实例逻辑与运算的结果。 |

## compareTo

```TypeScript
public compareTo(other: Boolean): int
```

将当前实例与另一个Boolean对象进行比较。当前实例小于传入对象时结果小于0， 相等时为0，否则大于0。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public compareTo(other: Boolean): int--><!--Device-Boolean-public compareTo(other: Boolean): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Boolean | 是 | 用于比较的Boolean对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 当前实例小于传入对象时返回负数，相等时返回0，大于时返回正数。 |

## constructor

```TypeScript
constructor(value: boolean)
```

使用指定的值构造新的Boolean对象。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: boolean)--><!--Device-Boolean-constructor(value: boolean)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 用于构造类实例的值。 |

## constructor

```TypeScript
constructor(value: byte)
```

使用指定的byte值构造新的Boolean对象。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: byte)--><!--Device-Boolean-constructor(value: byte)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | byte | 是 | 用于构造类实例的值。 |

## constructor

```TypeScript
constructor(value: char)
```

使用指定的char值构造新的Boolean对象。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: char)--><!--Device-Boolean-constructor(value: char)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | char | 是 | 用于构造类实例的值。 |

## constructor

```TypeScript
constructor(value: short)
```

使用指定的short值构造新的Boolean对象。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: short)--><!--Device-Boolean-constructor(value: short)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | short | 是 | 用于构造类实例的值。 |

## constructor

```TypeScript
constructor(value: int)
```

使用指定的int值构造新的Boolean对象。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: int)--><!--Device-Boolean-constructor(value: int)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 用于构造类实例的值。 <br>取值约束：应为整数。 |

## constructor

```TypeScript
constructor(value: long)
```

使用指定的long值构造新的Boolean对象。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: long)--><!--Device-Boolean-constructor(value: long)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 用于构造类实例的值。 |

## constructor

```TypeScript
constructor(value: bigint)
```

使用指定的bigint值构造新的Boolean对象。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: bigint)--><!--Device-Boolean-constructor(value: bigint)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint | 是 | 用于构造类实例的值。 |

## constructor

```TypeScript
constructor(value: float)
```

使用指定的float值构造新的Boolean对象。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: float)--><!--Device-Boolean-constructor(value: float)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | float | 是 | 用于构造类实例的值。 |

## constructor

```TypeScript
public constructor(value: double)
```

使用指定的number值构造新的Boolean对象。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public constructor(value: double)--><!--Device-Boolean-public constructor(value: double)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 用于构造类实例的值。 |

## constructor

```TypeScript
constructor(value: string)
```

使用指定的字符串值构造新的Boolean对象。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: string)--><!--Device-Boolean-constructor(value: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 用于构造类实例的值。 |

## constructor

```TypeScript
constructor(value: Any = undefined)
```

使用指定的Object值构造新的Boolean对象。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-constructor(value: Any = undefined)--><!--Device-Boolean-constructor(value: Any = undefined)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Any | 是 | 用于构造类实例的值。 |

## equals

```TypeScript
public equals(other: Any): boolean
```

判断当前实例与按Boolean处理的传入对象是否相等。如果传入对象的类型 与当前类型不一致，则返回false。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public equals(other: Any): boolean--><!--Device-Boolean-public equals(other: Any): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Any | 是 | 待比较的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果两个对象相等则返回true，否则返回false。 |

## isFalse

```TypeScript
public isFalse(): boolean
```

判断当前实例的值是否为false。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public isFalse(): boolean--><!--Device-Boolean-public isFalse(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果实例值为false则返回true，否则返回false。 |

## isTrue

```TypeScript
public isTrue(): boolean
```

判断当前实例的值是否为true。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public isTrue(): boolean--><!--Device-Boolean-public isTrue(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果实例值为true则返回true，否则返回false。 |

## negate

```TypeScript
public negate(): Boolean
```

对当前实例的值取反。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public negate(): Boolean--><!--Device-Boolean-public negate(): Boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean | 该Boolean实例逻辑取反后的结果。 |

## or

```TypeScript
public or(other: Boolean): Boolean
```

对当前实例与传入实例做逻辑或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public or(other: Boolean): Boolean--><!--Device-Boolean-public or(other: Boolean): Boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Boolean | 是 | 传入的实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean | 两个Boolean实例逻辑或运算的结果。 |

## toBoolean

```TypeScript
static toBoolean(value: boolean): boolean
```

以boolean值的形式返回该基本类型值。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-static toBoolean(value: boolean): boolean--><!--Device-Boolean-static toBoolean(value: boolean): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 原样返回传入的boolean值。 |

## toBoolean

```TypeScript
toBoolean(): boolean
```

返回当前实例的值。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-toBoolean(): boolean--><!--Device-Boolean-toBoolean(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 转换为boolean的实例值。 |

## toString

```TypeScript
public static toString(v: boolean): string
```

将基本类型值转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public static toString(v: boolean): string--><!--Device-Boolean-public static toString(v: boolean): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| v | boolean | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该boolean值的字符串表示。 |

## toString

```TypeScript
public toString(): string
```

将当前对象转换为字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public toString(): string--><!--Device-Boolean-public toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该Boolean对象的字符串表示。 |

## xor

```TypeScript
public xor(other: Boolean): Boolean
```

对当前实例与传入实例做逻辑异或运算。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Boolean-public xor(other: Boolean): Boolean--><!--Device-Boolean-public xor(other: Boolean): Boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Boolean | 是 | 传入的实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean | 两个Boolean实例逻辑异或运算的结果。 |

