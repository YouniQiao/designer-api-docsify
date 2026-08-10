# BundleOption

描述BundleOption信息，即应用的包信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface BundleOption--><!--Device-unnamed-export interface BundleOption-End-->

**System capability:** SystemCapability.Notification.Notification

## bundle

```TypeScript
bundle: string
```

应用的包名。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleOption-bundle: string--><!--Device-BundleOption-bundle: string-End-->

**System capability:** SystemCapability.Notification.Notification

## uid

```TypeScript
uid?: int
```

应用的UID。从[ApplicationInfo](../../apis-ability-kit/arkts-apis/arkts-ability-applicationinfo-i.md/arkts-ability-applicationinfo-i.md)获取，默认为0。应用分身场景下，此参数为必填项。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-BundleOption-uid?: int--><!--Device-BundleOption-uid?: int-End-->

**System capability:** SystemCapability.Notification.Notification

