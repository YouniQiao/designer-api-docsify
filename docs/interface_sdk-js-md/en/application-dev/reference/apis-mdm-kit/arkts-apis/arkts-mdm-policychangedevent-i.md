# PolicyChangedEvent

The policy event.

**Since:** 26.0.0

<!--Device-common-export interface PolicyChangedEvent--><!--Device-common-export interface PolicyChangedEvent-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { common } from '@kit.MDMKit';
```

## bundleName

```TypeScript
bundleName : string
```

The bundle name of the application that sets the policy.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolicyChangedEvent-bundleName : string--><!--Device-PolicyChangedEvent-bundleName : string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## functionName

```TypeScript
functionName : string
```

The function name for setting policy.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolicyChangedEvent-functionName : string--><!--Device-PolicyChangedEvent-functionName : string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## parameters

```TypeScript
parameters: string
```

The JSON string containing policy parameters.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolicyChangedEvent-parameters: string--><!--Device-PolicyChangedEvent-parameters: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## time

```TypeScript
time: number
```

The timestamp when the policy was set.Unit: milliseconds, The value must be an integer greater than or equal to 0.

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolicyChangedEvent-time: number--><!--Device-PolicyChangedEvent-time: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

