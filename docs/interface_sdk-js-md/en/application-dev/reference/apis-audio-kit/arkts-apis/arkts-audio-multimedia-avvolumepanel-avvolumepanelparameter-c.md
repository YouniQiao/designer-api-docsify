# AVVolumePanelParameter

音量面板参数设置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class AVVolumePanelParameter--><!--Device-unnamed-export declare class AVVolumePanelParameter-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## Modules to Import

```TypeScript
import { AVVolumePanelParameter, AVVolumePanel } from 'kits/@kit.AudioKit';
```

## position

```TypeScript
position?: Position
```

设置音量面板的位置。

如果不设置该参数，则使用系统默认的音量面板位置。

如果设置该参数且参数对应屏幕内位置，则显示应用设置的位置。

如果设置该参数且参数对应屏幕外位置，例如（-1, -1），则隐藏系统默认音量面板。

**注意：** 若应用需隐藏系统默认音量面板，必须提供自定义音量面板，以确保用户仍可调节音量。

**Type:** [Position](../../apis-arkui/arkts-apis/arkts-arkui-position-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-AVVolumePanelParameter-position?: Position--><!--Device-AVVolumePanelParameter-position?: Position-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

