# ControlComponentClickResult

```TypeScript
interface ControlComponentClickResult
```

Simulates the operation result.

**Since:** 26.1.0

<!--Device-abilityToolAccessCtrl-interface ControlComponentClickResult--><!--Device-abilityToolAccessCtrl-interface ControlComponentClickResult-End-->

**System capability:** SystemCapability.Security.Asset

## Modules to Import

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## appInfo

```TypeScript
appInfo: AppInfo
```

Information about the target application that is simulated.

**Type:** [AppInfo](arkts-ability-abilitytoolaccessctrl-appinfo-i.md)

**Since:** 26.1.0

**Model restriction:** This API can be used in both the stage model and FA model.

<!--Device-ControlComponentClickResult-appInfo: AppInfo--><!--Device-ControlComponentClickResult-appInfo: AppInfo-End-->

**System capability:** SystemCapability.Security.Asset

## code

```TypeScript
code: number
```

Result code of the simulated click operation. The value 0 indicates success, and other values indicate failure.

**Type:** number

**Since:** 26.1.0

**Model restriction:** This API can be used in both the stage model and FA model.

<!--Device-ControlComponentClickResult-code: number--><!--Device-ControlComponentClickResult-code: number-End-->

**System capability:** SystemCapability.Security.Asset

## componentId

```TypeScript
componentId: string
```

ID of the component that is simulated to be clicked.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used in both the stage model and FA model.

<!--Device-ControlComponentClickResult-componentId: string--><!--Device-ControlComponentClickResult-componentId: string-End-->

**System capability:** SystemCapability.Security.Asset

## isAllowed

```TypeScript
isAllowed: boolean
```

Indicates whether the simulated click is allowed. true: yes; false: no.

**Type:** boolean

**Since:** 26.1.0

**Model restriction:** This API can be used in both the stage model and FA model.

<!--Device-ControlComponentClickResult-isAllowed: boolean--><!--Device-ControlComponentClickResult-isAllowed: boolean-End-->

**System capability:** SystemCapability.Security.Asset

## reason

```TypeScript
reason: string
```

Reason description of the simulated operation result.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used in both the stage model and FA model.

<!--Device-ControlComponentClickResult-reason: string--><!--Device-ControlComponentClickResult-reason: string-End-->

**System capability:** SystemCapability.Security.Asset
