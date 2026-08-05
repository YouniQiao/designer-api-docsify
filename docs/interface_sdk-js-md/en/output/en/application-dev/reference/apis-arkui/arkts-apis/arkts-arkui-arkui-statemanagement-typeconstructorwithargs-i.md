# TypeConstructorWithArgs

Represents a class constructor that accepts arbitrary arguments.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export interface TypeConstructorWithArgs<T>--><!--Device-unnamed-export interface TypeConstructorWithArgs<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
new(...args: any): T
```

Creates and returns an instance of the specified type T.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TypeConstructorWithArgs-new(...args: any): T--><!--Device-TypeConstructorWithArgs-new(...args: any): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| args | any | Yes | Function arguments. |

**Return value:**

| Type | Description |
| --- | --- |
| T | Instance of the T type. |

