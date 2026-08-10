# ImmersiveMaterial

沉浸式材质类，继承自[Material](arkts-arkui-uimaterial-materialtype-e.md)。

沉浸式材质根据设备算力有分档表现，设备算力的高、中、低档由设备厂商决定，定义在系统配置文件中。在高档和中档算力设备上，影响材质层滤镜效果和阴影  
[shadow](arkts-arkui-common-commonmethod-i.md#shadow)效果。在低档算力设备上，影响背景色  
[backgroundColor](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md#backgroundcolor)、边框颜色[borderColor](arkts-arkui-common-commonmethod-i.md#bordercolor)、边框宽度[borderWidth](arkts-arkui-common-commonmethod-i.md#borderwidth)、阴影  
[shadow](arkts-arkui-common-commonmethod-i.md#shadow)效果。且同一材质的效果，会受到设置应用中沉浸光感配置项的影响，不同强弱程度的沉浸光感配置下，材质的参数和效果存在差异。

**Inheritance/Implementation:** ImmersiveMaterial extends [Material](arkts-arkui-uimaterial-material-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-uiMaterial-export class ImmersiveMaterial extends Material--><!--Device-uiMaterial-export class ImmersiveMaterial extends Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiMaterial } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ImmersiveOptions)
```

ImmersiveMaterial的构造函数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ImmersiveMaterial-constructor(options?: ImmersiveOptions)--><!--Device-ImmersiveMaterial-constructor(options?: ImmersiveOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ImmersiveOptions](arkts-arkui-uimaterial-immersiveoptions-i.md) | No | 系统材质配置选项，包括材质样式、材质层赋色等。&lt;br/&gt;默认值参考ImmersiveOptions接口各参数的默认值，即{style: ImmersiveStyle.REGULAR, materialColor:Color.Transparent, colorInvert:false, applyShadow:true, interactive: false, lightEffect:undefined}。 |

