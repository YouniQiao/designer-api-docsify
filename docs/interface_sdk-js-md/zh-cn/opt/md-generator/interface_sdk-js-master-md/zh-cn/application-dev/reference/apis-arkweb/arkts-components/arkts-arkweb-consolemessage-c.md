# ConsoleMessage

Encompassed message information as parameters to onConsole method.

**起始版本：** 8

**废弃版本：** -1

<!--Device-unnamed-declare class ConsoleMessage--><!--Device-unnamed-declare class ConsoleMessage-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor(message: string, sourceId: string, lineNumber: number, messageLevel: MessageLevel)
```

Constructor.

**起始版本：** 8

**废弃版本：** 9

**替代接口：** constructor

<!--Device-ConsoleMessage-constructor(message: string, sourceId: string, lineNumber: number, messageLevel: MessageLevel)--><!--Device-ConsoleMessage-constructor(message: string, sourceId: string, lineNumber: number, messageLevel: MessageLevel)-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | string | 是 |
| sourceId | string | 是 |
| [lineNumber](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-linemetrics-i.md) | number | 是 |
| messageLevel | [MessageLevel](arkts-arkweb-messagelevel-e.md) | 是 |

## constructor

```TypeScript
constructor()
```

ConsoleMessage的构造函数。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ConsoleMessage-constructor()--><!--Device-ConsoleMessage-constructor()-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## getLineNumber

```TypeScript
getLineNumber(): number
```

获取ConsoleMessage的行数。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ConsoleMessage-getLineNumber(): number--><!--Device-ConsoleMessage-getLineNumber(): number-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| number |

## getMessage

```TypeScript
getMessage(): string
```

获取ConsoleMessage的日志信息。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ConsoleMessage-getMessage(): string--><!--Device-ConsoleMessage-getMessage(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |

## getMessageLevel

```TypeScript
getMessageLevel(): MessageLevel
```

获取ConsoleMessage的信息级别。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ConsoleMessage-getMessageLevel(): MessageLevel--><!--Device-ConsoleMessage-getMessageLevel(): MessageLevel-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [MessageLevel](arkts-arkweb-messagelevel-e.md) |

## getSource

```TypeScript
getSource() : ConsoleMessageSource
```

获取ConsoleMessage的日志来源。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ConsoleMessage-getSource() : ConsoleMessageSource--><!--Device-ConsoleMessage-getSource() : ConsoleMessageSource-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| [ConsoleMessageSource](arkts-arkweb-consolemessagesource-e.md) |

## getSourceId

```TypeScript
getSourceId(): string
```

获取网页源文件路径和文件名。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ConsoleMessage-getSourceId(): string--><!--Device-ConsoleMessage-getSourceId(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 |
| --- |
| string |
