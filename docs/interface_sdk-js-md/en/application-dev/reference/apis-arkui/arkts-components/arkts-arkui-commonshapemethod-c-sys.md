# CommonShapeMethod

CommonShapeMethod

@extends CommonMethod&lt;T&gt;

**Inheritance/Implementation:** CommonShapeMethod extends CommonMethod<T>

**Since:** 11

<!--Device-unnamed-declare class CommonShapeMethod--><!--Device-unnamed-declare class CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

constructor.

**Since:** 9

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CommonShapeMethod-constructor()--><!--Device-CommonShapeMethod-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Examples**

```TypeScript
@Builder
function MyBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
}
let builderVar: WrappedBuilder<[string, number]> = new WrappedBuilder<[string, number]>(MyBuilder);
```

