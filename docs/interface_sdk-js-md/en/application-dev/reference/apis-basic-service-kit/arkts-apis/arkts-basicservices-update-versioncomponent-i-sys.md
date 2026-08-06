# VersionComponent (System API)

Represents a version component.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface VersionComponent--><!--Device-update-export interface VersionComponent-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## componentId

```TypeScript
componentId: string
```

Component ID, which uniquely identifies a component in the upgrade package. The value is obtained from the  
**versionComponents** array in the version check result and is used for subsequent description query or component information display.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-componentId: string--><!--Device-VersionComponent-componentId: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## componentType

```TypeScript
componentType: ComponentType
```

Component type.

**Type:** ComponentType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-componentType: ComponentType--><!--Device-VersionComponent-componentType: ComponentType-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## descriptionInfo

```TypeScript
descriptionInfo: DescriptionInfo
```

Information about the version description file.

**Type:** DescriptionInfo

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-descriptionInfo: DescriptionInfo--><!--Device-VersionComponent-descriptionInfo: DescriptionInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## displayVersion

```TypeScript
displayVersion: string
```

Display version number.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-displayVersion: string--><!--Device-VersionComponent-displayVersion: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## effectiveMode

```TypeScript
effectiveMode: EffectiveMode
```

Effective mode. The value **COLD** indicates the cold upgrade, which takes effect after the device is restarted;  
**LIVE** indicates the hot upgrade, which does not require restarting the device to take effect;  
**LIVE\_AND\_COLD** indicates the integrated upgrade, which combines the characteristics of **COLD** and **LIVE**.

**Type:** EffectiveMode

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-effectiveMode: EffectiveMode--><!--Device-VersionComponent-effectiveMode: EffectiveMode-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## innerVersion

```TypeScript
innerVersion: string
```

Internal version number.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-innerVersion: string--><!--Device-VersionComponent-innerVersion: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## otaMode

```TypeScript
otaMode?: OtaMode
```

OTA mode. Pass this parameter to specify a specific upgrade mode, which is applicable to special scenarios such as the upgrade with limited storage space, fast upgrade, and A/B partition device upgrade. The value  
**REGULAR\_OTA** indicates a regular upgrade, which is applicable to most common upgrade scenarios. **STREAM\_OTA**  
indicates a streaming upgrade, which is applicable to scenarios where the storage space is limited or a fast upgrade is required. **AB\_REGULAR\_OTA** indicates the normal A/B upgrade and applies to the A/B partition device.  
**AB\_STREAM\_OTA** indicates the A/B streaming upgrade and applies to the A/B partition device. If this parameter is not specified, the default value **REGULAR\_OTA** is used, indicating that the regular upgrade mode is used.

**Type:** OtaMode

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-VersionComponent-otaMode?: OtaMode--><!--Device-VersionComponent-otaMode?: OtaMode-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## size

```TypeScript
size: int
```

Size of the upgrade package, in bytes. The value range is [0, +∞]. An exception is thrown if the value is out of range.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-size: int--><!--Device-VersionComponent-size: int-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## upgradeAction

```TypeScript
upgradeAction: UpgradeAction
```

Upgrade action. The value **UPGRADE** indicates that the upgrade package is a differential package, which applies to incremental upgrade. The value **RECOVERY** indicates that the upgrade package is a repair package, which applies to system failure repair.

**Type:** UpgradeAction

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionComponent-upgradeAction: UpgradeAction--><!--Device-VersionComponent-upgradeAction: UpgradeAction-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

