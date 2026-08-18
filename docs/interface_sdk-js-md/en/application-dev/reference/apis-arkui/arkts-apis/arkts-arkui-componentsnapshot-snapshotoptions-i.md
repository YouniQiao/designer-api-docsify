# SnapshotOptions

Defines the extra options for snapshot taking.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-componentSnapshot-export interface SnapshotOptions--><!--Device-componentSnapshot-export interface SnapshotOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { componentSnapshot } from '@kit.ArkUI';
```

## colorMode

```TypeScript
colorMode?: ColorModeOptions
```

Set the color space options for current snapshot taking.

**Type:** [ColorModeOptions](arkts-arkui-componentsnapshot-colormodeoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SnapshotOptions-colorMode?: ColorModeOptions--><!--Device-SnapshotOptions-colorMode?: ColorModeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dynamicRangeMode

```TypeScript
dynamicRangeMode?: DynamicRangeModeOptions
```

Set the dynamic range mode options for current snapshot taking.

**Type:** [DynamicRangeModeOptions](arkts-arkui-componentsnapshot-dynamicrangemodeoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SnapshotOptions-dynamicRangeMode?: DynamicRangeModeOptions--><!--Device-SnapshotOptions-dynamicRangeMode?: DynamicRangeModeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## region

```TypeScript
region?: SnapshotRegionType
```

Defines the rect region type of the snapshot.

**Type:** [SnapshotRegionType](arkts-arkui-componentsnapshot-snapshotregiontype-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SnapshotOptions-region?: SnapshotRegionType--><!--Device-SnapshotOptions-region?: SnapshotRegionType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scale

```TypeScript
scale?: double
```

Defines the scale property to render the snapshot.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SnapshotOptions-scale?: double--><!--Device-SnapshotOptions-scale?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## waitUntilRenderFinished

```TypeScript
waitUntilRenderFinished?: boolean
```

Whether to wait the rendering is finished.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SnapshotOptions-waitUntilRenderFinished?: boolean--><!--Device-SnapshotOptions-waitUntilRenderFinished?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

