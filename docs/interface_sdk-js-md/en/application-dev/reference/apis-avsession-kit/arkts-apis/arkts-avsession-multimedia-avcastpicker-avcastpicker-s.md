# AVCastPicker

本模块提供创建投播组件AVCastPicker的功能，提供设备发现连接的统一入口。

> **说明：**
> 
> - 示例效果请以真机为准，当前DevEco Studio预览器无实际投播功能。&lt;!--Del--&gt;
> 
> - 当前组件的使用，依赖于设备支持“设备选择界面”。当前暂无OpenHarmony设备支持，需要OEM厂商实现具体的“设备选择界面”。&lt;!--DelEnd--&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Component

<!--Device-unnamed-declare struct AVCastPicker--><!--Device-unnamed-declare struct AVCastPicker-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## Modules to Import

```TypeScript
import { AVCastPicker } from 'kits/@kit.AVSessionKit';
```

## build

```TypeScript
build(): void
```

构造组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

<!--Device-AVCastPicker-build(): void--><!--Device-AVCastPicker-build(): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## onStateChange

```TypeScript
onStateChange?: OnPickerStateCallback
```

投播状态更改回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastPicker-onStateChange?: OnPickerStateCallback--><!--Device-AVCastPicker-onStateChange?: OnPickerStateCallback-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## activeColor

```TypeScript
activeColor?: Color | int | string
```

设备连接成功状态下投播组件的颜色。

未设置时，系统将优先根据normalColor的颜色匹配；如果normalColor也未设置，将采用colorMode下的颜色设置。

**Type:** [Color](../../apis-arkui/arkts-apis/arkts-arkui-color-e.md) \| int \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastPicker-activeColor?: Color | int | string--><!--Device-AVCastPicker-activeColor?: Color | int | string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## colorMode

```TypeScript
colorMode?: AVCastPickerColorMode
```

显示模式。默认值为AUTO。

- 当colorMode设置为AUTO时，跟随系统的深浅色模式的默认色值。  
- 当colorMode设置为DARK、LIGHT时，使用对应模式的系统预设色值。

**Type:** [AVCastPickerColorMode](arkts-avsession-multimedia-avcastpickerparam-avcastpickercolormode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastPicker-colorMode?: AVCastPickerColorMode--><!--Device-AVCastPicker-colorMode?: AVCastPickerColorMode-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## customPicker

```TypeScript
customPicker?: CustomBuilder
```

自定义样式。建议使用自定义组件样式，可有效提升组件显示速度。

If not set, system will show the default appearance for different device type.

**Type:** [CustomBuilder](../../apis-arkui/arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @BuilderParam

<!--Device-AVCastPicker-customPicker?: CustomBuilder--><!--Device-AVCastPicker-customPicker?: CustomBuilder-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## normalColor

```TypeScript
normalColor?: Color | int | string
```

正常状态下投播组件的颜色。

未设置时，将采用colorMode下的颜色设置。

**Type:** [Color](../../apis-arkui/arkts-apis/arkts-arkui-color-e.md) \| int \| string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastPicker-normalColor?: Color | int | string--><!--Device-AVCastPicker-normalColor?: Color | int | string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## pickerStyle

```TypeScript
pickerStyle?: AVCastPickerStyle
```

投播样式。

- 当sessionType是audio或者video时，默认值为STYLE_PANEL。  
- 当sessionType是voice_call或者video_call时，默认值为STYLE_MENU，且不可修改为STYLE_PANEL。

**Type:** [AVCastPickerStyle](arkts-avsession-multimedia-avcastpickerparam-avcastpickerstyle-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastPicker-pickerStyle?: AVCastPickerStyle--><!--Device-AVCastPicker-pickerStyle?: AVCastPickerStyle-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## sessionType

```TypeScript
sessionType?: string
```

会话类型，可参考[AVSessionType](arkts-avsession-avsession-avsessiontype-t.md)。默认值为当前应用创建的AVSessionType。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVCastPicker-sessionType?: string--><!--Device-AVCastPicker-sessionType?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

