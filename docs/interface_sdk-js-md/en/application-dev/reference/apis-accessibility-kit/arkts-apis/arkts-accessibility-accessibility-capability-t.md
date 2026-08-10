# Capability

```TypeScript
type Capability = 'retrieve' | 'touchGuide' | 'keyEventObserver' | 'zoom' | 'gesture'
```

辅助应用能力类型。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-type Capability = 'retrieve' | 'touchGuide' | 'keyEventObserver' | 'zoom' | 'gesture'--><!--Device-accessibility-type Capability = 'retrieve' | 'touchGuide' | 'keyEventObserver' | 'zoom' | 'gesture'-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

| Type | Description |
| --- | --- |
| 'retrieve' | 具有检索窗口内容的能力。 |
| 'touchGuide' | 具有触摸探索模式的能力。 |
| 'keyEventObserver' | 具有过滤按键事件的能力。 |
| 'zoom' | 具有控制显示放大的能力，当前版本暂不支持。 |
| 'gesture' | 具有执行手势动作的能力。 |

