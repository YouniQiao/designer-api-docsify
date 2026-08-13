# debug

## debug

```TypeScript
function debug(domain: number, tag: string, format: string, ...args: any[]): void
```

打印DEBUG级别的日志。 DEBUG级别的日志在正式发布版本中默认不被打印，只有在调试版本或打开调试开关的情况下才会打印。

**起始版本：** 7

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-hilog-function debug(domain: number, tag: string, format: string, ...args: any[]): void--><!--Device-hilog-function debug(domain: number, tag: string, format: string, ...args: any[]): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| domain | number | 是 |
| tag | string | 是 |
| format | string | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | any[] | 是 |

## 示例

输出一条DEBUG信息，格式字符串为。其中变参为明文显示的字符串；为隐私的整型数。

```TypeScript
hilog.debug(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

字符串填入，整型数填入，输出日志：

```TypeScript
08-05 12:21:47.579  2695-2703  A00001/testTag  com.example.hilogDemo  D     hello World <private>
```


## debug

```TypeScript
function debug(domain: number, tag: string, format: string, ...args: RecordData[]): void
```

打印DEBUG级别的日志。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-hilog-function debug(domain: int, tag: string, format: string, ...args: RecordData[]): void--><!--Device-hilog-function debug(domain: int, tag: string, format: string, ...args: RecordData[]): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| domain | number | 是 |
| tag | string | 是 |
| format | string | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)[] | 是 |
