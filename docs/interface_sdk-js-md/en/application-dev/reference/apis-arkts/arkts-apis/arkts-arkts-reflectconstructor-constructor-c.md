# Constructor

Represents a class constructor.

**Inheritance/Implementation:** Constructor extends [Method](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-ssap-method-i-sys.md)

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## createInstance

```TypeScript
public createInstance(args?: FixedArray<Any>): Any
```

Creates a new instance of its belonging class using this constructor.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | FixedArray & lt;Any & gt; | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Any |

## equals

```TypeScript
public equals(other: Constructor): boolean
```

Compares whether the current constructor object is equal to another constructor object.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | Constructor | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |
