# Constants

## ArcScrollBar

```TypeScript
export declare const ArcScrollBar: ArcScrollBarInterface
```

弧形滚动条组件ArcScrollBar，适用于圆形屏幕等需要弧形滚动条的场景，用于配合可滚动组件使用，如[ArcList](arkts-arkui-arclist.md)、  
[List](../../apis-arkui/arkts-components/arkts-arkui-list-i)、[Grid](../../apis-arkui/arkts-components/arkts-arkui-grid-i)、  
[Scroll](../../apis-arkui/arkts-components/arkts-arkui-scroll-i)、[WaterFlow](../../apis-arkui/arkts-components/arkts-arkui-water_flow-i)。

> **说明：**
> 
> - 未设置宽高时，ArcScrollBar采用父组件[LayoutConstraint](arkts-arkui-framenode-layoutconstraint-i.md)中的maxSize作为尺寸。若父组件存在可滚动组件，如
> [ArcList](arkts-arkui-arclist.md)、[List](../../apis-arkui/arkts-components/arkts-arkui-list-i)、
> [Grid](../../apis-arkui/arkts-components/arkts-arkui-grid-i)、[Scroll](../../apis-arkui/arkts-components/arkts-arkui-scroll-i)、
> [WaterFlow](../../apis-arkui/arkts-components/arkts-arkui-water_flow-i)，建议设置ArcScrollBar宽高，否则尺寸可能为无穷大。
> 
> - 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

### 子组件

不包含子组件。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-export declare const ArcScrollBar: ArcScrollBarInterface--><!--Device-unnamed-export declare const ArcScrollBar: ArcScrollBarInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## ArcScrollBarInstance

```TypeScript
export declare const ArcScrollBarInstance: ArcScrollBarAttribute
```

定义ArcScrollBar组件实例。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-export declare const ArcScrollBarInstance: ArcScrollBarAttribute--><!--Device-unnamed-export declare const ArcScrollBarInstance: ArcScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

