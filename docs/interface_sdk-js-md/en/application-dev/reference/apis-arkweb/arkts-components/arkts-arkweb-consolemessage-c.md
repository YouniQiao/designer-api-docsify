# ConsoleMessage

ConsoleMessage is an object that encapsulates JavaScript console output information in the **Web** component. When a web page outputs logs through methods such as `console.log()`, `console.warn()`, and `console.error()`, this object is provided to the app through the `onConsole` event callback for monitoring and inspecting web page debug output. For sample code, see [onConsole event](arkts-arkweb-web-attribute.md#onconsole).

**Since:** 8

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(message: string, sourceId: string, lineNumber: number, messageLevel: MessageLevel)
```

Constructs a **ConsoleMessage** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** constructor

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | string | Yes |
| sourceId | string | Yes |
| [lineNumber](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-linemetrics-i.md) | number | Yes |
| messageLevel | [MessageLevel](arkts-arkweb-messagelevel-e.md) | Yes |

## constructor

```TypeScript
constructor()
```

Constructs a **ConsoleMessage** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

## getLineNumber

```TypeScript
getLineNumber(): number
```

Obtains the line number of the console output in the web source file.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getMessage

```TypeScript
getMessage(): string
```

Obtains the log message of the console output.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getMessageLevel

```TypeScript
getMessageLevel(): MessageLevel
```

Obtains the level of this console message.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MessageLevel](arkts-arkweb-messagelevel-e.md) |

## getSource

```TypeScript
getSource() : ConsoleMessageSource
```

Obtains the log source of this console message.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ConsoleMessageSource](arkts-arkweb-consolemessagesource-e.md) |

## getSourceId

```TypeScript
getSourceId(): string
```

Obtains the path and file name of the web source file.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
