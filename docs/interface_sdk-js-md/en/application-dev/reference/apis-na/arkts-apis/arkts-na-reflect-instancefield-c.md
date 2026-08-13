# InstanceField

Represents an instance field of a class or interface.

**Inheritance/Implementation:** InstanceField extends Field

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

<!--Device-reflect-class InstanceField--><!--Device-reflect-class InstanceField-End-->

**System capability:** SystemCapability.Utils.Lang

## equals

```TypeScript
equals(other: InstanceField): boolean
```

Checks if the current instance field is equal to the given instance field.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstanceField-equals(other: InstanceField): boolean--><!--Device-InstanceField-equals(other: InstanceField): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | [InstanceField](arkts-na-reflect-instancefield-c.md) | Yes | Another StaticField object to compare with the current StaticField instance. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the two instance fields are equal, otherwise returns false. |

## getValue

```TypeScript
getValue(thisObj: Object): Any
```

Reads the value from the instance field.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstanceField-getValue(thisObj: Object): Any--><!--Device-InstanceField-getValue(thisObj: Object): Any-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| thisObj | Object | Yes | The target object as the `this` context. |

**Return value:**

| Type | Description |
| --- | --- |
| Any | Returns the value read from the instance field.When thisobj is null, it returns null; when it is undefined, it returns undefined. |

## setValue

```TypeScript
setValue(thisObj: Object, value: Any): void
```

Writes a value to the instance field.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstanceField-setValue(thisObj: Object, value: Any): void--><!--Device-InstanceField-setValue(thisObj: Object, value: Any): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| thisObj | Object | Yes | The target object as the `this` context. |
| value | Any | Yes | The value to write. |

