# JsonTypeError

Error thrown when attempting to access a JSON element with an incompatible type. For example, trying to get a string value from a number element.

**Inheritance/Implementation:** JsonTypeError extends [JsonError](arkts-na-jsonx-jsonerror-c.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-jsonx-export class JsonTypeError--><!--Device-jsonx-export class JsonTypeError-End-->

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonTypeError-public constructor(msg: string)--><!--Device-JsonTypeError-public constructor(msg: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msg | string | Yes | Error message. |

