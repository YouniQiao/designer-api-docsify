# TypeConstructorWithArgs

Represents a class constructor that accepts arbitrary arguments.

**Since:** 12

<!--Device-unnamed-export interface TypeConstructorWithArgs--><!--Device-unnamed-export interface TypeConstructorWithArgs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
new(...args: any): T
```

Creates and returns an instance of the specified type T.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TypeConstructorWithArgs-new(...args: any): T--><!--Device-TypeConstructorWithArgs-new(...args: any): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | any | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |
