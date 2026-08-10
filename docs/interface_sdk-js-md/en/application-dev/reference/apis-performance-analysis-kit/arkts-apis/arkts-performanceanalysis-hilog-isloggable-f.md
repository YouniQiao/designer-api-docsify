# isLoggable

## Modules to Import

```TypeScript
import { hilog } from 'kits/@kit.PerformanceAnalysisKit';
```

## isLoggable

```TypeScript
function isLoggable(domain: int, tag: string, level: LogLevel): boolean
```

在打印日志前调用该接口，用于检查指定领域标识、日志标识和级别的日志是否可以打印。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hilog-function isLoggable(domain: int, tag: string, level: LogLevel): boolean--><!--Device-hilog-function isLoggable(domain: int, tag: string, level: LogLevel): boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domain | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。&lt;br/&gt;建议开发者在应用内根据需要自定义划分。 |
| tag | string | Yes | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag长度最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| level | [LogLevel](arkts-performanceanalysis-hilog-loglevel-e.md) | Yes | 日志级别。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 如果返回true，则该领域标识、日志标识和级别的日志可以打印，否则不能打印。 |

## Examples

```TypeScript
hilog.isLoggable(0x0001, "testTag", hilog.LogLevel.INFO);
```

