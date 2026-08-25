# JsonTypeError

Error thrown when attempting to access a JSON element with an incompatible type. For example, trying to get a string value from a number element.

**Inheritance/Implementation:** JsonTypeError extends [JsonError](arkts-arkts-jsonx-jsonerror-c.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
public constructor(msg: string)
```

Constructs a new JsonTypeError with the specified message.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| msg | string | Yes |
