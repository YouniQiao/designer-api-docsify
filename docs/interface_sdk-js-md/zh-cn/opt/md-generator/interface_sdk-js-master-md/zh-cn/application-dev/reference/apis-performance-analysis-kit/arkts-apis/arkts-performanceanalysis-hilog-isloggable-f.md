# isLoggable

## isLoggable

```TypeScript
function isLoggable(domain: number, tag: string, level: LogLevel): boolean
```

在打印日志前调用该接口，用于检查指定领域标识、日志标识和级别的日志是否可以打印。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-hilog-function isLoggable(domain: int, tag: string, level: LogLevel): boolean--><!--Device-hilog-function isLoggable(domain: int, tag: string, level: LogLevel): boolean-End-->

**系统能力：** SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| domain | number | 是 |
| tag | string | 是 |
| level | [LogLevel](arkts-performanceanalysis-hilog-loglevel-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## 示例

```TypeScript
hilog.isLoggable(0x0001, "testTag", hilog.LogLevel.INFO);
```
