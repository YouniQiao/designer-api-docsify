# KioskStatus

表示Kiosk状态信息，包括系统是否处于Kiosk模式以及该模式下的应用信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface KioskStatus--><!--Device-unnamed-export interface KioskStatus-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## isKioskMode

```TypeScript
isKioskMode: boolean
```

当前系统是否处于Kiosk模式。true表示处于Kiosk模式，false表示不处于。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KioskStatus-isKioskMode: boolean--><!--Device-KioskStatus-isKioskMode: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## kioskBundleName

```TypeScript
kioskBundleName: string
```

进入Kiosk模式的应用的名称。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KioskStatus-kioskBundleName: string--><!--Device-KioskStatus-kioskBundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## kioskBundleUid

```TypeScript
kioskBundleUid: int
```

进入Kiosk模式的应用的UID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KioskStatus-kioskBundleUid: int--><!--Device-KioskStatus-kioskBundleUid: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

