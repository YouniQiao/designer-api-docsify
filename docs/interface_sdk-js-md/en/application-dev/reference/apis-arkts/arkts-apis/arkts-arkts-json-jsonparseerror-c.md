# JsonParseError

Error thrown when parsing JSON fails.

**Inheritance/Implementation:** JsonParseError extends [SyntaxError](arkts-arkts-errors-syntaxerror-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export class JsonParseError extends SyntaxError--><!--Device-unnamed-export class JsonParseError extends SyntaxError-End-->

**System capability:** SystemCapability.Utils.Lang

## $_invoke

```TypeScript
static $_invoke(msg: string, start_offset?: int, end_offset?: int): JsonParseError
```

Creates a JsonParseError with location information.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonParseError-static $_invoke(msg: string, start_offset?: int, end_offset?: int): JsonParseError--><!--Device-JsonParseError-static $_invoke(msg: string, start_offset?: int, end_offset?: int): JsonParseError-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msg | string | Yes | Error message |
| start_offset | int | No | Start offset in the source string &lt;br&gt;The value should be an integer. |
| end_offset | int | No | End offset in the source string &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| [JsonParseError](arkts-arkts-json-jsonparseerror-c.md) | The created JsonParseError |

## constructor

```TypeScript
public constructor(message?: string, options?: ErrorOptions)
```

Constructor for creating a JsonParseError.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonParseError-public constructor(message?: string, options?: ErrorOptions)--><!--Device-JsonParseError-public constructor(message?: string, options?: ErrorOptions)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| message | string | No | Error message. |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No | Error options. |

