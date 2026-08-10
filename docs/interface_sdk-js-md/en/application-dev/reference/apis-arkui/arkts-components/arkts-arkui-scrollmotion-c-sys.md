# ScrollMotion (System API)

滚动动画模型。可以根据初始位置、初始速度、边界位置和弹簧属性构建滚动动画。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 22

<!--Device-unnamed-declare class ScrollMotion--><!--Device-unnamed-declare class ScrollMotion-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## constructor

```TypeScript
constructor(position: number, velocity: number, min: number, max: number, prop: SpringProp)
```

构造器参数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 22

<!--Device-ScrollMotion-constructor(position: number, velocity: number, min: number, max: number, prop: SpringProp)--><!--Device-ScrollMotion-constructor(position: number, velocity: number, min: number, max: number, prop: SpringProp)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | number | Yes |  |
| velocity | number | Yes |  |
| min | number | Yes |  |
| max | number | Yes |  |
| prop | [SpringProp](arkts-arkui-springprop-c-sys.md) | Yes |  |

