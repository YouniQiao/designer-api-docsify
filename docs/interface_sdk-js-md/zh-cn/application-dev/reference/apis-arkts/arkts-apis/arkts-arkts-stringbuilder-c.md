# StringBuilder

面向性能的字符串构建类。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class StringBuilder--><!--Device-unnamed-export class StringBuilder-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## append

```TypeScript
append(s: string): StringBuilder
```

将字符串追加到构建器的内部缓冲区。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-append(s: string): StringBuilder--><!--Device-StringBuilder-append(s: string): StringBuilder-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | 待追加的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StringBuilder](arkts-arkts-stringbuilder-c.md) | 内部缓冲区已更新的构建器。 |

## append

```TypeScript
append(i: boolean): StringBuilder
```

将boolean值以字符串形式追加到构建器的内部缓冲区。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-append(i: boolean): StringBuilder--><!--Device-StringBuilder-append(i: boolean): StringBuilder-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | boolean | 是 | 待追加的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StringBuilder](arkts-arkts-stringbuilder-c.md) | 内部缓冲区已更新的构建器。 |

## append

```TypeScript
append(i: byte): StringBuilder
```

将byte值以字符串形式追加到构建器的内部缓冲区。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-append(i: byte): StringBuilder--><!--Device-StringBuilder-append(i: byte): StringBuilder-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | byte | 是 | 待追加的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StringBuilder](arkts-arkts-stringbuilder-c.md) | 内部缓冲区已更新的构建器。 |

## append

```TypeScript
append(i: char): StringBuilder
```

将char值追加到构建器的内部缓冲区。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-append(i: char): StringBuilder--><!--Device-StringBuilder-append(i: char): StringBuilder-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | char | 是 | 待追加的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StringBuilder](arkts-arkts-stringbuilder-c.md) | 内部缓冲区已更新的构建器。 |

## append

```TypeScript
append(i: short): StringBuilder
```

将short值以字符串形式追加到构建器的内部缓冲区。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-append(i: short): StringBuilder--><!--Device-StringBuilder-append(i: short): StringBuilder-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | short | 是 | 待追加的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StringBuilder](arkts-arkts-stringbuilder-c.md) | 内部缓冲区已更新的构建器。 |

## append

```TypeScript
append(i: int): StringBuilder
```

将int值以字符串形式追加到构建器的内部缓冲区。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-append(i: int): StringBuilder--><!--Device-StringBuilder-append(i: int): StringBuilder-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | int | 是 | 待追加的值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StringBuilder](arkts-arkts-stringbuilder-c.md) | 内部缓冲区已更新的构建器。 |

## append

```TypeScript
append(i: long): StringBuilder
```

将long值以字符串形式追加到构建器的内部缓冲区。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-append(i: long): StringBuilder--><!--Device-StringBuilder-append(i: long): StringBuilder-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | long | 是 | 待追加的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StringBuilder](arkts-arkts-stringbuilder-c.md) | 内部缓冲区已更新的构建器。 |

## append

```TypeScript
append(i: float): StringBuilder
```

将float值以字符串形式追加到构建器的内部缓冲区。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-append(i: float): StringBuilder--><!--Device-StringBuilder-append(i: float): StringBuilder-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | float | 是 | 待追加的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StringBuilder](arkts-arkts-stringbuilder-c.md) | 内部缓冲区已更新的构建器。 |

## append

```TypeScript
append(i: double): StringBuilder
```

将double值以字符串形式追加到构建器的内部缓冲区。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-append(i: double): StringBuilder--><!--Device-StringBuilder-append(i: double): StringBuilder-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | double | 是 | 待追加的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StringBuilder](arkts-arkts-stringbuilder-c.md) | 内部缓冲区已更新的构建器。 |

## append

```TypeScript
append(o: Object): StringBuilder
```

将对象的字符串表示追加到构建器的内部缓冲区。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-append(o: Object): StringBuilder--><!--Device-StringBuilder-append(o: Object): StringBuilder-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| o | Object | 是 | 将被转换为字符串的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StringBuilder](arkts-arkts-stringbuilder-c.md) | 内部缓冲区已更新的构建器。 |

## concatStrings

```TypeScript
static concatStrings(lhs: string, rhs: string): string
```

连接两个字符串，并以新字符串返回结果。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-static concatStrings(lhs: string, rhs: string): string--><!--Device-StringBuilder-static concatStrings(lhs: string, rhs: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lhs | string | 是 | 左侧字符串（前缀）。 |
| rhs | string | 是 | 右侧字符串（后缀）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 连接后的结果。 |

## constructor

```TypeScript
constructor()
```

构造初始缓冲区为16个字符的新构建器实例。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-constructor()--><!--Device-StringBuilder-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(fromChars: FixedArray<char>)
```

使用指定的字符数组构造新的构建器实例。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-constructor(fromChars: FixedArray<char>)--><!--Device-StringBuilder-constructor(fromChars: FixedArray<char>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fromChars | FixedArray&lt;char&gt; | 是 | 用于初始化构建器的字符数组。 |

## constructor

```TypeScript
constructor(fromChars: char[])
```

使用指定的字符数组构造新的构建器实例。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-constructor(fromChars: char[])--><!--Device-StringBuilder-constructor(fromChars: char[])-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fromChars | char[] | 是 | 用于初始化构建器的字符数组。 |

## constructor

```TypeScript
constructor(s: string)
```

使用指定的字符串构造新的构建器实例。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-constructor(s: string)--><!--Device-StringBuilder-constructor(s: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| s | string | 是 | 用于初始化构建器的字符串。 |

## toString

```TypeScript
toString(): string
```

返回所有追加操作最终形成的字符串。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-toString(): string--><!--Device-StringBuilder-toString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 构建器当前缓冲区对应的字符串。 |

## toString

```TypeScript
static toString(i: boolean): string
```

将基本类型值转换为字符串。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-static toString(i: boolean): string--><!--Device-StringBuilder-static toString(i: boolean): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | boolean | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toString

```TypeScript
static toString(i: byte): string
```

将基本类型值转换为字符串。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-static toString(i: byte): string--><!--Device-StringBuilder-static toString(i: byte): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | byte | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toString

```TypeScript
static toString(i: char): string
```

将基本类型值转换为字符串。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-static toString(i: char): string--><!--Device-StringBuilder-static toString(i: char): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | char | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toString

```TypeScript
static toString(i: short): string
```

将基本类型值转换为字符串。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-static toString(i: short): string--><!--Device-StringBuilder-static toString(i: short): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | short | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toString

```TypeScript
static toString(i: int): string
```

将基本类型值转换为字符串。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-static toString(i: int): string--><!--Device-StringBuilder-static toString(i: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | int | 是 | 待转换的值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toString

```TypeScript
static toString(i: long): string
```

将基本类型值转换为字符串。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-static toString(i: long): string--><!--Device-StringBuilder-static toString(i: long): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | long | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toString

```TypeScript
static toString(f: float): string
```

将基本类型值转换为字符串。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-static toString(f: float): string--><!--Device-StringBuilder-static toString(f: float): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| f | float | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

## toString

```TypeScript
static toString(d: double): string
```

将基本类型值转换为字符串。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-StringBuilder-static toString(d: double): string--><!--Device-StringBuilder-static toString(d: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 | 待转换的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换结果。 |

