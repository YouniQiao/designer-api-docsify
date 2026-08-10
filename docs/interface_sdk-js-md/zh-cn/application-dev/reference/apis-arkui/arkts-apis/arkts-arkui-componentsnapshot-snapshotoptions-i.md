# SnapshotOptions

Defines the extra options for snapshot taking.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-componentSnapshot-export interface SnapshotOptions--><!--Device-componentSnapshot-export interface SnapshotOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { componentSnapshot } from 'kits/@kit.ArkUI';
```

## colorMode

```TypeScript
colorMode?: ColorModeOptions
```

Set the color space options for current snapshot taking.

**类型：** [ColorModeOptions](arkts-arkui-componentsnapshot-colormodeoptions-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SnapshotOptions-colorMode?: ColorModeOptions--><!--Device-SnapshotOptions-colorMode?: ColorModeOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dynamicRangeMode

```TypeScript
dynamicRangeMode?: DynamicRangeModeOptions
```

Set the dynamic range mode options for current snapshot taking.

**类型：** [DynamicRangeModeOptions](arkts-arkui-componentsnapshot-dynamicrangemodeoptions-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SnapshotOptions-dynamicRangeMode?: DynamicRangeModeOptions--><!--Device-SnapshotOptions-dynamicRangeMode?: DynamicRangeModeOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## region

```TypeScript
region?: SnapshotRegionType
```

Defines the rect region type of the snapshot.

**类型：** [SnapshotRegionType](arkts-arkui-componentsnapshot-snapshotregiontype-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SnapshotOptions-region?: SnapshotRegionType--><!--Device-SnapshotOptions-region?: SnapshotRegionType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale?: double
```

Defines the scale property to render the snapshot.

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SnapshotOptions-scale?: double--><!--Device-SnapshotOptions-scale?: double-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## waitUntilRenderFinished

```TypeScript
waitUntilRenderFinished?: boolean
```

Whether to wait the rendering is finished.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SnapshotOptions-waitUntilRenderFinished?: boolean--><!--Device-SnapshotOptions-waitUntilRenderFinished?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

