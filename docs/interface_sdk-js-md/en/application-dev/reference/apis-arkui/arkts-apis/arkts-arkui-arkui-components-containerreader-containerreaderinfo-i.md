# ContainerReaderInfo

Defines the configuration options for ContainerReader component.Used to specify the parameters for container dimension reading and breakpoint analysis.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface ContainerReaderInfo--><!--Device-unnamed-export declare interface ContainerReaderInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## heightBreakpoint

```TypeScript
heightBreakpoint?: Bindable<HeightBreakpoint>
```

Optional height breakpoint configuration for container height analysis.Defines the height thresholds that trigger different layout behaviors.

**Type:** Bindable&lt;HeightBreakpoint&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContainerReaderInfo-heightBreakpoint?: Bindable<HeightBreakpoint>--><!--Device-ContainerReaderInfo-heightBreakpoint?: Bindable<HeightBreakpoint>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size: Bindable<Size>
```

The target container size for layout analysis.Defines the reference dimensions used for breakpoint calculation and layout adaptation.

**Type:** Bindable&lt;Size&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContainerReaderInfo-size: Bindable<Size>--><!--Device-ContainerReaderInfo-size: Bindable<Size>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## widthBreakpoint

```TypeScript
widthBreakpoint?: Bindable<WidthBreakpoint>
```

Optional width breakpoint configuration for container width analysis.Defines the width thresholds that trigger different layout behaviors.

**Type:** Bindable&lt;WidthBreakpoint&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContainerReaderInfo-widthBreakpoint?: Bindable<WidthBreakpoint>--><!--Device-ContainerReaderInfo-widthBreakpoint?: Bindable<WidthBreakpoint>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

