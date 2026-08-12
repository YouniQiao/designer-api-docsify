# JsonError

Base error class for JSON-related errors.Thrown when general JSON parsing or manipulation errors occur.

**Inheritance/Implementation:** JsonError extends [Error](Error)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-jsonx-export class JsonError extends Error--><!--Device-jsonx-export class JsonError extends Error-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
public constructor(msg: string)
```

Constructs a new JsonError with the specified message.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonError-public constructor(msg: string)--><!--Device-JsonError-public constructor(msg: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msg | string | Yes | Error message. |

