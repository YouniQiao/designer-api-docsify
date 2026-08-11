# ConsoleMessage

Encompassed message information as parameters to {@link onConsole} method.

**Since:** 8

<!--Device-unnamed-declare class ConsoleMessage--><!--Device-unnamed-declare class ConsoleMessage-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor(message: string, sourceId: string, lineNumber: number, messageLevel: MessageLevel)
```

Constructor.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.web.ConsoleMessage#constructor

<!--Device-ConsoleMessage-constructor(message: string, sourceId: string, lineNumber: number, messageLevel: MessageLevel)--><!--Device-ConsoleMessage-constructor(message: string, sourceId: string, lineNumber: number, messageLevel: MessageLevel)-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | string | Yes |
| sourceId | string | Yes |
| lineNumber | number | Yes |
| messageLevel | [MessageLevel](arkts-arkweb-messagelevel-e.md) | Yes |

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ConsoleMessage-constructor()--><!--Device-ConsoleMessage-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getLineNumber

```TypeScript
getLineNumber(): number
```

Gets the line number of a console message.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ConsoleMessage-getLineNumber(): number--><!--Device-ConsoleMessage-getLineNumber(): number-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getMessage

```TypeScript
getMessage(): string
```

Gets the message of a console message.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ConsoleMessage-getMessage(): string--><!--Device-ConsoleMessage-getMessage(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## getMessageLevel

```TypeScript
getMessageLevel(): MessageLevel
```

Gets the message level of a console message.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ConsoleMessage-getMessageLevel(): MessageLevel--><!--Device-ConsoleMessage-getMessageLevel(): MessageLevel-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MessageLevel](arkts-arkweb-messagelevel-e.md) |

## getSource

```TypeScript
getSource(): ConsoleMessageSource
```

Gets the source of a console message.

**Since:** 23

<!--Device-ConsoleMessage-getSource(): ConsoleMessageSource--><!--Device-ConsoleMessage-getSource(): ConsoleMessageSource-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ConsoleMessageSource](arkts-arkweb-consolemessagesource-e.md) |

## getSourceId

```TypeScript
getSourceId(): string
```

Gets the Web source file's path and name of a console message.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ConsoleMessage-getSourceId(): string--><!--Device-ConsoleMessage-getSourceId(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
