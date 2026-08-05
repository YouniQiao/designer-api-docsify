# DynamicRangeModeOptions

Defines the dynamic range mode used for current snapshot taking. By default, the system draws snapshot in STANDARD mode. You can set the dynamicRangeMode parameter and set isAuto to false, for using one specific dynamic range mode. Also you can just set isAuto to true for letting the system to determine the dynamic range mode automaticly. When isAuto is set to true, value set by the dynamicRangeMode field will be ignored.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-componentSnapshot-export interface DynamicRangeModeOptions--><!--Device-componentSnapshot-export interface DynamicRangeModeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dynamicRangeMode

```TypeScript
dynamicRangeMode?: DynamicRangeMode
```

Set one specific dynamic range mode that you want to use.

**Type:** DynamicRangeMode

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DynamicRangeModeOptions-dynamicRangeMode?: DynamicRangeMode--><!--Device-DynamicRangeModeOptions-dynamicRangeMode?: DynamicRangeMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isAuto

```TypeScript
isAuto?: boolean
```

Indicate that if the system should decide the dynamic range mode automatically. If set this to true, the one specified by dynamicRangeMode parameter will be ignored. When setting isAuto to true, it is recommended to also set the waitUntilRenderFinished field in SnapshotOptions to true to ensure that the system can properly detect the mode being used.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DynamicRangeModeOptions-isAuto?: boolean--><!--Device-DynamicRangeModeOptions-isAuto?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

