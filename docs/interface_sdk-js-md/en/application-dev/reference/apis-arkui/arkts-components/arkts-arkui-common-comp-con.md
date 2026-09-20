# Constants

## Styles

```TypeScript
declare const Styles: MethodDecorator & StylesVersionDecorator
```

The @Styles decorator is used to extract multiple style settings into a method, which can be directly called at the component declaration site to define and reuse custom styles. It is suitable for scenarios where multiple components need to share the same styles, reducing repetitive code and improving the efficiency of maintaining style consistency.

**Type:** [MethodDecorator](../../apis-default/arkts-apis/arkts-methoddecorator-t.md) & [StylesVersionDecorator](arkts-arkui-stylesversiondecorator-t.md)

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
