# SystemUpdateInfo

待更新的系统版本信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-systemManager-export interface SystemUpdateInfo--><!--Device-systemManager-export interface SystemUpdateInfo-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## firstReceivedTime

```TypeScript
firstReceivedTime: number
```

第一次收到系统更新包的时间（单位：秒）。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemUpdateInfo-firstReceivedTime: number--><!--Device-SystemUpdateInfo-firstReceivedTime: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## packageType

```TypeScript
packageType: string
```

待更新的系统更新包类型，类型分为normal和patch类型。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemUpdateInfo-packageType: string--><!--Device-SystemUpdateInfo-packageType: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## versionName

```TypeScript
versionName: string
```

待更新的系统版本名称。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemUpdateInfo-versionName: string--><!--Device-SystemUpdateInfo-versionName: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

