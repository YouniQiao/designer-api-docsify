# Constructor

Represents a class constructor.

**Inheritance/Implementation:** Constructor extends [Method](Method)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-class Constructor extends Method--><!--Device-unnamed-class Constructor extends Method-End-->

**System capability:** SystemCapability.Utils.Lang

## createInstance

```TypeScript
public createInstance(args?: FixedArray<Any>): Any
```

Creates a new instance of its belonging class using this constructor.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Constructor-public createInstance(args?: FixedArray<Any>): Any--><!--Device-Constructor-public createInstance(args?: FixedArray<Any>): Any-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| args | FixedArray&lt;Any&gt; | No | args The argument list for the constructor. |

**Return value:**

| Type | Description |
| --- | --- |
| Any | The newly created class instance. |

## equals

```TypeScript
public equals(other: Constructor): boolean
```

Compares whether the current constructor object is equal to another constructor object.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Constructor-public equals(other: Constructor): boolean--><!--Device-Constructor-public equals(other: Constructor): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Another constructor object to compare with. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the two constructor objects are equal, otherwise returns false. |

