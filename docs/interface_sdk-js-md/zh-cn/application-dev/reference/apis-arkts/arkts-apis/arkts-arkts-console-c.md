# Console

提供标准输出流和错误流访问能力的Console类。 支持打印多种数据类型、计时操作以及缩进管理。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-unnamed-class Console--><!--Device-unnamed-class Console-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## assert

```TypeScript
assert(...vals: Any[]): void
```

当断言条件为false时打印错误信息。条件取自vals中的 第一个值（如果存在）。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-assert(...vals: Any[]): void--><!--Device-Console-assert(...vals: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vals | Any[] | 是 | 条件为false时需要打印的值。 |

## count

```TypeScript
count(label?: string): void
```

统计使用指定标识调用该方法的number，并将当前计数 打印到标准输出。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-count(label?: string): void--><!--Device-Console-count(label?: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | 用于计数的标识。 |

## countReset

```TypeScript
countReset(label?: string): void
```

重置指定标识对应的计数器。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-countReset(label?: string): void--><!--Device-Console-countReset(label?: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | 待重置计数器的标识。 |

## debug

```TypeScript
debug(...vals: Any[]): void
```

打印debug级别的日志。如果第一个参数是字符串，则将其作为格式化字符串处理。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-debug(...vals: Any[]): void--><!--Device-Console-debug(...vals: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vals | Any[] | 是 | 待打印的可变number的值。 |

## dir

```TypeScript
dir(obj?: Any): void
```

将对象的格式化表示打印到标准输出，并过滤掉键中包含“field#”的属性。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-dir(obj?: Any): void--><!--Device-Console-dir(obj?: Any): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 否 | 待查看的对象。 |

## dirxml

```TypeScript
dirxml(...obj: Any[]): void
```

将对象的XML表示打印到标准输出，当前实现按原样输出该对象。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-dirxml(...obj: Any[]): void--><!--Device-Console-dirxml(...obj: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any[] | 是 | 以XML形式展示的对象。 |

## error

```TypeScript
error(...vals: Any[]): void
```

打印error级别的日志。如果第一个参数是字符串，则将其作为格式化字符串处理。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-error(...vals: Any[]): void--><!--Device-Console-error(...vals: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vals | Any[] | 是 | 待打印的可变number的值。 |

## getInstance

```TypeScript
public static getInstance(): Console
```

获取Console的单例实例。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public static getInstance(): Console--><!--Device-Console-public static getInstance(): Console-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Console](arkts-arkts-console-c.md) | Console的单例实例。 |

## group

```TypeScript
group(...objs: Any[]): void
```

开启新的日志分组，标识可选，后续日志的缩进级别会相应增加。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-group(...objs: Any[]): void--><!--Device-Console-group(...objs: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| objs | Any[] | 是 | 用于开启新日志分组的标识。 |

## groupCollapsed

```TypeScript
groupCollapsed(...objs: Any[]): void
```

group()方法的别名，在支持的环境中创建折叠分组。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-groupCollapsed(...objs: Any[]): void--><!--Device-Console-groupCollapsed(...objs: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| objs | Any[] | 是 | 用于创建折叠分组的标识。 |

## groupEnd

```TypeScript
groupEnd(): void
```

结束当前日志分组，后续日志的缩进级别会相应减少。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-groupEnd(): void--><!--Device-Console-groupEnd(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## info

```TypeScript
info(...vals: Any[]): void
```

打印info级别的日志。如果第一个参数是字符串，则将其作为格式化字符串处理。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-info(...vals: Any[]): void--><!--Device-Console-info(...vals: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vals | Any[] | 是 | 待打印的可变number的值。 |

## log

```TypeScript
log(i: boolean): void
```

将基本类型值打印到标准输出。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: boolean): void--><!--Device-Console-log(i: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | boolean | 是 | 待打印到标准输出的值。 |

## log

```TypeScript
log(i: byte): void
```

打印日志。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: byte): void--><!--Device-Console-log(i: byte): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | byte | 是 | 待打印的值。 |

## log

```TypeScript
log(i: short): void
```

打印日志。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: short): void--><!--Device-Console-log(i: short): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | short | 是 | 待打印的值。 |

## log

```TypeScript
log(i: char): void
```

打印日志。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: char): void--><!--Device-Console-log(i: char): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | char | 是 | 待打印的值。 |

## log

```TypeScript
log(i: int): void
```

打印日志。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: int): void--><!--Device-Console-log(i: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | int | 是 | 待打印的值。 <br>取值约束：应为整数。 |

## log

```TypeScript
log(i: long): void
```

打印日志。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: long): void--><!--Device-Console-log(i: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | long | 是 | 待打印的值。 |

## log

```TypeScript
log(i: float): void
```

打印日志。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: float): void--><!--Device-Console-log(i: float): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | float | 是 | 待打印的值。 |

## log

```TypeScript
log(i: double): void
```

打印日志。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: double): void--><!--Device-Console-log(i: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | double | 是 | 待打印的值。 |

## log

```TypeScript
log(i: string): void
```

打印日志。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(i: string): void--><!--Device-Console-log(i: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | string | 是 | 待打印的值。 |

## log

```TypeScript
log(): void
```

打印日志。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(): void--><!--Device-Console-log(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## log

```TypeScript
log(...vals: Any[]): void
```

打印log级别的日志。如果第一个参数是字符串，则将其作为格式化字符串处理。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-log(...vals: Any[]): void--><!--Device-Console-log(...vals: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vals | Any[] | 是 | 待打印的可变number的值。 |

## print

```TypeScript
public print(i: boolean): void
```

将基本类型值打印到标准输出，且不换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: boolean): void--><!--Device-Console-public print(i: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | boolean | 是 | 待打印到标准输出的值。 |

## print

```TypeScript
public print(i: byte): void
```

将基本类型值打印到标准输出，且不换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: byte): void--><!--Device-Console-public print(i: byte): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | byte | 是 | 待打印到标准输出的值。 |

## print

```TypeScript
public print(i: short): void
```

将基本类型值打印到标准输出，且不换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: short): void--><!--Device-Console-public print(i: short): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | short | 是 | 待打印到标准输出的值。 |

## print

```TypeScript
public print(i: char): void
```

将基本类型值打印到标准输出，且不换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: char): void--><!--Device-Console-public print(i: char): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | char | 是 | 待打印到标准输出的值。 |

## print

```TypeScript
public print(i: int): void
```

将基本类型值打印到标准输出，且不换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: int): void--><!--Device-Console-public print(i: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | int | 是 | 待打印到标准输出的值。 <br>取值约束：应为整数。 |

## print

```TypeScript
public print(i: long): void
```

将基本类型值打印到标准输出，且不换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: long): void--><!--Device-Console-public print(i: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | long | 是 | 待打印到标准输出的值。 |

## print

```TypeScript
public print(i: float): void
```

将基本类型值打印到标准输出，且不换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: float): void--><!--Device-Console-public print(i: float): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | float | 是 | 待打印到标准输出的值。 |

## print

```TypeScript
public print(i: double): void
```

将基本类型值打印到标准输出，且不换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: double): void--><!--Device-Console-public print(i: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | double | 是 | 待打印到标准输出的值。 |

## print

```TypeScript
public print(i: string): void
```

将基本类型值打印到标准输出，且不换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: string): void--><!--Device-Console-public print(i: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | string | 是 | 待打印到标准输出的值。 |

## print

```TypeScript
public print(i: Any): void
```

将基本类型值打印到标准输出，且不换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public print(i: Any): void--><!--Device-Console-public print(i: Any): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | Any | 是 | 待打印到标准输出的值。 |

## println

```TypeScript
public println(): void
```

向标准输出打印一个换行符。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(): void--><!--Device-Console-public println(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## println

```TypeScript
public println(i: boolean): void
```

将值打印到标准输出，并在其后换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: boolean): void--><!--Device-Console-public println(i: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | boolean | 是 | 待打印到标准输出的值。 |

## println

```TypeScript
public println(i: byte): void
```

将值打印到标准输出，并在其后换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: byte): void--><!--Device-Console-public println(i: byte): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | byte | 是 | 待打印到标准输出的值。 |

## println

```TypeScript
public println(i: short): void
```

将值打印到标准输出，并在其后换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: short): void--><!--Device-Console-public println(i: short): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | short | 是 | 待打印到标准输出的值。 |

## println

```TypeScript
public println(i: char): void
```

将值打印到标准输出，并在其后换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: char): void--><!--Device-Console-public println(i: char): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | char | 是 | 待打印到标准输出的值。 |

## println

```TypeScript
public println(i: int): void
```

将值打印到标准输出，并在其后换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: int): void--><!--Device-Console-public println(i: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | int | 是 | 待打印到标准输出的值。 <br>取值约束：应为整数。 |

## println

```TypeScript
public println(i: long): void
```

将值打印到标准输出，并在其后换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: long): void--><!--Device-Console-public println(i: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | long | 是 | 待打印到标准输出的值。 |

## println

```TypeScript
public println(i: float): void
```

将值打印到标准输出，并在其后换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: float): void--><!--Device-Console-public println(i: float): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | float | 是 | 待打印到标准输出的值。 |

## println

```TypeScript
public println(i: double): void
```

将值打印到标准输出，并在其后换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: double): void--><!--Device-Console-public println(i: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | double | 是 | 待打印到标准输出的值。 |

## println

```TypeScript
public println(i: string): void
```

将值打印到标准输出，并在其后换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: string): void--><!--Device-Console-public println(i: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | string | 是 | 待打印到标准输出的值。 |

## println

```TypeScript
public println(i: Any): void
```

将值打印到标准输出，并在其后换行。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-public println(i: Any): void--><!--Device-Console-public println(i: Any): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| i | Any | 是 | 待打印到标准输出的值。 |

## table

```TypeScript
table(...data: Any[]): void
```

以表格形式展示对象数组，会先将数据转换为DataFrame再进行渲染。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-table(...data: Any[]): void--><!--Device-Console-table(...data: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Any[] | 是 | 以表格形式展示的对象数组。 |

## time

```TypeScript
time(label?: string): void
```

启动计时器，标识可选，用于统计time()与timeEnd()调用之间的执行时间。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-time(label?: string): void--><!--Device-Console-time(label?: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | 定时器的标识。 |

## timeEnd

```TypeScript
timeEnd(label?: string): void
```

停止计时器并打印其耗时，同时移除该计时器；如果计时器不存在，则打印告警信息。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-timeEnd(label?: string): void--><!--Device-Console-timeEnd(label?: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | 定时器的标识。 |

## timeLog

```TypeScript
timeLog(label?: string, ...arguments: Object[]): void
```

打印运行中计时器的当前耗时且不停止该计时器。如果指定的计时器 不存在，则打印告警信息。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-timeLog(label?: string, ...arguments: Object[]): void--><!--Device-Console-timeLog(label?: string, ...arguments: Object[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | 定时器的标识。 |
| arguments | Object[] | 是 | 附加的调试信息。 |

## trace

```TypeScript
trace(...data: Any[]): void
```

打印当前调用栈，标识可选，并跳过第一个栈帧（即trace调用本身）。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-trace(...data: Any[]): void--><!--Device-Console-trace(...data: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Any[] | 是 | 附加的调试信息。 |

## warn

```TypeScript
warn(...vals: Any[]): void
```

打印warn级别的日志。如果第一个参数是字符串，则将其作为格式化字符串处理。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Console-warn(...vals: Any[]): void--><!--Device-Console-warn(...vals: Any[]): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vals | Any[] | 是 | 待打印的可变number的值。 |

