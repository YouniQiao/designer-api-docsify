# console

提供一个简单的调试控制台，类似于浏览器提供的JavaScript控制台机制。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-export declare class console--><!--Device-unnamed-export declare class console-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## assert

```TypeScript
static assert(value?: Object, ...arguments: Object[]): void
```

断言打印。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static assert(value?: Object, ...arguments: Object[]): void--><!--Device-console-static assert(value?: Object, ...arguments: Object[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | No | 语句结果值。若value为假（false）或者省略，则输出以"Assertion failed"开头。 如果value为真值（true），则无打印。 |
| arguments | Object[] | Yes | value为假（false）的后续错误消息打印。省略则不打印。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## count

```TypeScript
static count(label?: string): void
```

维护一个内部计数器，调用时，打印此标签名以及对应的计数次数。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static count(label?: string): void--><!--Device-console-static count(label?: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | string | No | 计数器标签名。默认值为'default'。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## countReset

```TypeScript
static countReset(label?: string): void
```

清除指定标签名的计数。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static countReset(label?: string): void--><!--Device-console-static countReset(label?: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | string | No | 计数器标签名。默认值为'default'。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## debug

```TypeScript
static debug(message: string, ...arguments: any[]): void
```

以格式化输出方式打印调试信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-console-static debug(message: string, ...arguments: any[]): void--><!--Device-console-static debug(message: string, ...arguments: any[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | Yes | 要打印的文本信息。 |
| arguments | any[] | Yes | 其余要打印的信息或message的替换值。 |

## dir

```TypeScript
static dir(dir?: Object): void
```

打印对象内容。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static dir(dir?: Object): void--><!--Device-console-static dir(dir?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dir | Object | No | 需要打印内容的对象。省略则无任何打印。 |

## dirxml

```TypeScript
static dirxml(...arguments: Object[]): void
```

此方法通过内部调用console.log()实现。此方法不会产生任何XML格式。使用方法与console.log()一致。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static dirxml(...arguments: Object[]): void--><!--Device-console-static dirxml(...arguments: Object[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arguments | Object[] | Yes | 要打印的信息。省略则无任何打印。 |

## error

```TypeScript
static error(message: string, ...arguments: any[]): void
```

以格式化输出方式打印错误信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-console-static error(message: string, ...arguments: any[]): void--><!--Device-console-static error(message: string, ...arguments: any[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | Yes | 要打印的错误信息。 |
| arguments | any[] | Yes | 其余要打印的信息或message的替换值。 |

## group

```TypeScript
static group(...arguments: Object[]): void
```

默认将后续行的缩进增加两个空格。如果提供需要打印的信息，则首先打印信息，没有额外的缩进。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static group(...arguments: Object[]): void--><!--Device-console-static group(...arguments: Object[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arguments | Object[] | Yes | 要打印的信息。省略则仅打印两个空格。 |

## groupCollapsed

```TypeScript
static groupCollapsed(...arguments: Object[]): void
```

使用与功能同console.group()一致。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static groupCollapsed(...arguments: Object[]): void--><!--Device-console-static groupCollapsed(...arguments: Object[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arguments | Object[] | Yes | 要打印的信息。省略则仅打印两个空格。 |

## groupEnd

```TypeScript
static groupEnd(): void
```

将后续行的缩进减少两个空格。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static groupEnd(): void--><!--Device-console-static groupEnd(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## info

```TypeScript
static info(message: string, ...arguments: any[]): void
```

以格式化输出方式打印日志信息（console.log()的别名）。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-console-static info(message: string, ...arguments: any[]): void--><!--Device-console-static info(message: string, ...arguments: any[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | Yes | 要打印的文本信息。 |
| arguments | any[] | Yes | 其余要打印的信息或message的替换值。 |

## log

```TypeScript
static log(message: string, ...arguments: any[]): void
```

以格式化输出方式打印日志信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-console-static log(message: string, ...arguments: any[]): void--><!--Device-console-static log(message: string, ...arguments: any[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | Yes | 要打印的文本信息。 |
| arguments | any[] | Yes | 其余要打印的信息或message的替换值。 |

## table

```TypeScript
static table(tableData?: Object): void
```

以表格形式打印数据。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static table(tableData?: Object): void--><!--Device-console-static table(tableData?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tableData | Object | No | 要打印为表格形式的对象。省略则无任何打印。 |

## time

```TypeScript
static time(label?: string): void
```

启动可用于计算操作持续时间的计时器。可使用console.timeEnd()关闭计时器并打印经过的时间（单位：ms）。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static time(label?: string): void--><!--Device-console-static time(label?: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | string | No | 计时器标识。默认值为'default'。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## timeEnd

```TypeScript
static timeEnd(label?: string): void
```

停止之前通过调用console.time()启动的计时器并打印经过的时间（单位：ms）。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static timeEnd(label?: string): void--><!--Device-console-static timeEnd(label?: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | string | No | 计时器标识。默认值为'default'。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## timeLog

```TypeScript
static timeLog(label?: string, ...arguments: Object[]): void
```

对于先前通过调用console.time()启动的计时器，打印经过时间和其他data参数。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static timeLog(label?: string, ...arguments: Object[]): void--><!--Device-console-static timeLog(label?: string, ...arguments: Object[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| label | string | No | 计时器标识。默认值为'default'。 |
| arguments | Object[] | Yes | 需要打印的其他日志。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

## trace

```TypeScript
static trace(...arguments: Object[]): void
```

打印当前堆栈。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static trace(...arguments: Object[]): void--><!--Device-console-static trace(...arguments: Object[]): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arguments | Object[] | Yes | 需要打印的其他日志。省略则仅打印堆栈信息。 |

## traceHybridStack

```TypeScript
static traceHybridStack(): void
```

在主线程或worker线程中打印当前线程混合堆栈信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-console-static traceHybridStack(): void--><!--Device-console-static traceHybridStack(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## warn

```TypeScript
static warn(message: string, ...arguments: any[]): void
```

以格式化输出方式打印警告信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-console-static warn(message: string, ...arguments: any[]): void--><!--Device-console-static warn(message: string, ...arguments: any[]): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | Yes | 要打印的警告信息。 |
| arguments | any[] | Yes | 其余要打印的信息或message的替换值。 |

