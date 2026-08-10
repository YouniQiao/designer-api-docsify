# @ohos.arkui.componentSnapshot

This module allows developers to export snapshot image from a component or a custom builder.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace componentSnapshot--><!--Device-unnamed-declare namespace componentSnapshot-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { componentSnapshot } from 'kits/@kit.ArkUI';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [getSync](arkts-arkui-componentsnapshot-getsync-f.md#getsync) | Take a screenshot of the specified component in synchronous mode,this mode will block the main thread, please use it with caution, the maximum waiting time of the interface is 3s, if it does not return after 3s, an exception will be thrown. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [ColorModeOptions](arkts-arkui-componentsnapshot-colormodeoptions-i.md) | Defines the color mode used for current snapshot taking.By default, the system draws snapshot in sRGB mode. Therefore, snapshot for components with wide color display mode enabled will lose some effect. If you know the color space used in the component to be taken snapshot,you can specify the colorSpace parameter and set isAuto to false, for achieving the expected screenshot effect.But it is difficult to know which color space is used by the component to be taken. Therefore, in general,you can just set isAuto to true for letting the system to determine the color space to use based on the actual situation automaticly. When isAuto is set to true, value set by the colorSpace field will be ignored. |
| [DynamicRangeModeOptions](arkts-arkui-componentsnapshot-dynamicrangemodeoptions-i.md) | Defines the dynamic range mode used for current snapshot taking.By default, the system draws snapshot in STANDARD mode. You can set the dynamicRangeMode parameter and set isAuto to false, for using one specific dynamic range mode.Also you can just set isAuto to true for letting the system to determine the dynamic range mode automaticly.When isAuto is set to true, value set by the dynamicRangeMode field will be ignored. |
| [LocalizedSnapshotRegion](arkts-arkui-componentsnapshot-localizedsnapshotregion-i.md) | Defines the extra options for snapshot taking, if this is used, the start and end will be assigned to left and right value according to the layout direction of node automatically. |
| [SnapshotOptions](arkts-arkui-componentsnapshot-snapshotoptions-i.md) | Defines the extra options for snapshot taking. |
| [SnapshotRegion](arkts-arkui-componentsnapshot-snapshotregion-i.md) | Defines the target region information for snapshot taking. |
| [SnapshotSizeLimitation](arkts-arkui-componentsnapshot-snapshotsizelimitation-i.md) | Defines the size limitation for component snapshot taking. |

### 类型

| 名称 | 说明 |
| --- | --- |
| [SnapshotRegionType](arkts-arkui-componentsnapshot-snapshotregiontype-t.md) | Defines the snapshot region rect type. |

