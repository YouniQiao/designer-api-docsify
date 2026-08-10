# debug

## Modules to Import

```TypeScript
import { hilog } from 'kits/@kit.PerformanceAnalysisKit';
```

## debug

```TypeScript
function debug(domain: number, tag: string, format: string, ...args: any[]): void
```

打印DEBUG级别的日志。

DEBUG级别的日志在正式发布版本中默认不被打印，只有在调试版本或打开调试开关的情况下才会打印。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hilog-function debug(domain: number, tag: string, format: string, ...args: any[]): void--><!--Device-hilog-function debug(domain: number, tag: string, format: string, ...args: any[]): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domain | number | Yes | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。&lt;br/&gt;建议开发者在应用内根据需要自定义划分。 |
| tag | string | Yes | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag长度最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| format | string | Yes | 格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。&lt;br&gt;隐私标识分为{public}和{private}，缺省为{private }。标识{public}的内容明文输出，标识{private}的内容以&lt;private&gt;过滤回显。 |
| args | any[] | Yes | 与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。 |

## Examples

This example is used to output a DEBUG log with the format string being "%{public}s World %{private}d". The variable  is a plaintext string, and the variable  is a private integer.

```TypeScript
hilog.debug(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

If "hello" is filled in %{public}s and 3 in %{private}d, the output log is as follows:

```TypeScript
08-05 12:21:47.579  2695-2703  A00001/testTag  com.example.hilogDemo  D     hello World <private>
```


## debug

```TypeScript
function debug(domain: int, tag: string, format: string, ...args: RecordData[]): void
```

打印DEBUG级别的日志。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-hilog-function debug(domain: int, tag: string, format: string, ...args: RecordData[]): void--><!--Device-hilog-function debug(domain: int, tag: string, format: string, ...args: RecordData[]): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domain | int | Yes | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。&lt;br/&gt;建议开发者在应用内根据需要自定义划分。 |
| tag | string | Yes | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag长度最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| format | string | Yes | 格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。&lt;br&gt;隐私标识分为{public}和{private}，缺省为{private }。标识{public}的内容明文输出，标识{private}的内容以&lt;private&gt;过滤回显。 |
| args | [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)[] | Yes | 与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。 |

