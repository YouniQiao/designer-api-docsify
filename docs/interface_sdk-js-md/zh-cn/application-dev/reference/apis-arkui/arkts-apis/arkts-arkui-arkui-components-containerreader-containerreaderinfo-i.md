# ContainerReaderInfo

Defines the configuration options for ContainerReader component.Used to specify the parameters for container dimension reading and breakpoint analysis.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare interface ContainerReaderInfo--><!--Device-unnamed-export declare interface ContainerReaderInfo-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { BreakpointOptions, ContainerReader, ContainerReaderAttribute } from 'kits/@kit.ArkUI';
```

## heightBreakpoint

```TypeScript
heightBreakpoint?: Bindable<HeightBreakpoint>
```

Optional height breakpoint configuration for container height analysis.Defines the height thresholds that trigger different layout behaviors.

**类型：** [Bindable](arkts-arkui-common-bindable-i.md)&lt;[HeightBreakpoint](arkts-arkui-heightbreakpoint-e.md)&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ContainerReaderInfo-heightBreakpoint?: Bindable<HeightBreakpoint>--><!--Device-ContainerReaderInfo-heightBreakpoint?: Bindable<HeightBreakpoint>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size: Bindable<Size>
```

The target container size for layout analysis.Defines the reference dimensions used for breakpoint calculation and layout adaptation.

**类型：** [Bindable](arkts-arkui-common-bindable-i.md)&lt;[Size](arkts-arkui-graphics-size-i.md)&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ContainerReaderInfo-size: Bindable<Size>--><!--Device-ContainerReaderInfo-size: Bindable<Size>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## widthBreakpoint

```TypeScript
widthBreakpoint?: Bindable<WidthBreakpoint>
```

Optional width breakpoint configuration for container width analysis.Defines the width thresholds that trigger different layout behaviors.

**类型：** [Bindable](arkts-arkui-common-bindable-i.md)&lt;[WidthBreakpoint](arkts-arkui-widthbreakpoint-e.md)&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ContainerReaderInfo-widthBreakpoint?: Bindable<WidthBreakpoint>--><!--Device-ContainerReaderInfo-widthBreakpoint?: Bindable<WidthBreakpoint>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

