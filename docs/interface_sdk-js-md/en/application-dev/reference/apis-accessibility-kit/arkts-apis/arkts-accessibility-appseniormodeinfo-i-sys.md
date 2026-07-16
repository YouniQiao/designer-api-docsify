# AppSeniorModeInfo (System API)

Indicates the senior mode information of an application.

**Since:** 26.0.0

<!--Device-config-interface AppSeniorModeInfo--><!--Device-config-interface AppSeniorModeInfo-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { config } from '@kit.AccessibilityKit';
```

## appIndex

```TypeScript
appIndex?: number
```

Indicates the index of clone app.The value must be an integer greater than or equal to 0. Default value: 0.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppSeniorModeInfo-appIndex?: int--><!--Device-AppSeniorModeInfo-appIndex?: int-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

The bundle name of application.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppSeniorModeInfo-bundleName: string--><!--Device-AppSeniorModeInfo-bundleName: string-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## seniorModeState

```TypeScript
seniorModeState: boolean
```

The state of senior mode for application.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppSeniorModeInfo-seniorModeState: boolean--><!--Device-AppSeniorModeInfo-seniorModeState: boolean-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

