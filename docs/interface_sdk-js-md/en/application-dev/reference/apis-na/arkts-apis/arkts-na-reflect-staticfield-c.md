# StaticField

Represents static field of class

**Inheritance/Implementation:** StaticField extends Field

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-reflect-class StaticField--><!--Device-reflect-class StaticField-End-->

**System capability:** SystemCapability.Utils.Lang

## equals

```TypeScript
equals(other: StaticField): boolean
```

Determine whether the current Static Field object is equal to another object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StaticField-equals(other: StaticField): boolean--><!--Device-StaticField-equals(other: StaticField): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [StaticField](arkts-na-reflect-staticfield-c.md) | Yes | Another Static Field object to compare. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | If two objects are equal, return true; otherwise, return false. |

## getValue

```TypeScript
getValue(): Any
```

Reads value from an instance field.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StaticField-getValue(): Any--><!--Device-StaticField-getValue(): Any-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Any | field value. |

## setValue

```TypeScript
setValue(value: Any): void
```

Writes value into a static field.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-StaticField-setValue(value: Any): void--><!--Device-StaticField-setValue(value: Any): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Any | Yes | value to write. |

