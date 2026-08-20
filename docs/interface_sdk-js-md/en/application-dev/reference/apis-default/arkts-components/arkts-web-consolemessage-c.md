# ConsoleMessage

Encompassed message information as parameters to [onConsole](arkts-web-attribute.md#onconsole) method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class ConsoleMessage--><!--Device-unnamed-export declare class ConsoleMessage-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ConsoleMessage-constructor()--><!--Device-ConsoleMessage-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getLineNumber

```TypeScript
getLineNumber(): int
```

Gets the line number of a console message.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ConsoleMessage-getLineNumber(): int--><!--Device-ConsoleMessage-getLineNumber(): int-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | Return the line number of a console message. |

## getMessage

```TypeScript
getMessage(): string
```

Gets the message of a console message.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ConsoleMessage-getMessage(): string--><!--Device-ConsoleMessage-getMessage(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the message of a console message. |

## getMessageLevel

```TypeScript
getMessageLevel(): MessageLevel
```

Gets the message level of a console message.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ConsoleMessage-getMessageLevel(): MessageLevel--><!--Device-ConsoleMessage-getMessageLevel(): MessageLevel-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [MessageLevel](arkts-web-messagelevel-e.md) | Return the message level of a console message, which can be { |

## getSource

```TypeScript
getSource(): ConsoleMessageSource
```

Gets the source of a console message.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ConsoleMessage-getSource(): ConsoleMessageSource--><!--Device-ConsoleMessage-getSource(): ConsoleMessageSource-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ConsoleMessageSource](arkts-web-consolemessagesource-e.md) | Return the source of a console message. |

## getSourceId

```TypeScript
getSourceId(): string
```

Gets the Web source file's path and name of a console message.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ConsoleMessage-getSourceId(): string--><!--Device-ConsoleMessage-getSourceId(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the Web source file's path and name of a console message. |

