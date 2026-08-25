# JsonParseError

Error thrown when parsing JSON fails.

**Inheritance/Implementation:** JsonParseError extends SyntaxError

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_invoke

```TypeScript
static $_invoke(msg: string, start_offset?: int, end_offset?: int): JsonParseError
```

Creates a JsonParseError with location information.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| msg | string | Yes |
| start_offset | int | No |
| end_offset | int | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonParseError](arkts-arkts-json-jsonparseerror-c.md) |

## constructor

```TypeScript
public constructor(message?: string, options?: ErrorOptions)
```

Constructor for creating a JsonParseError.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| message | string | No |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | No |
