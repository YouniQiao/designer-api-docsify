# fatal

## 导入模块

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
```

## fatal

```TypeScript
function fatal(domain: number, tag: string, format: string, ...args: any[]): void
```

打印FATAL级别的日志。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| domain | number | 是 |
| tag | string | 是 |
| format | string | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | any[] | 是 |

**示例**

输出一条FATAL信息，格式字符串为。其中变参为明文显示的字符串；为隐私的整型数。

```TypeScript
hilog.fatal(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

字符串填入，整型数填入，输出日志：

```TypeScript
08-05 12:21:47.579  2695-2703  A00001/testTag  com.example.hilogDemo  F     hello World <private>
```


## fatal

```TypeScript
function fatal(domain: int, tag: string, format: string, ...args: RecordData[]): void
```

打印FATAL级别的日志。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| domain | int | 是 |
| tag | string | 是 |
| format | string | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)[] | 是 |

**示例**

参见 [fatal](#fatal)
