# LauncherAbilityInfo

桌面应用的Ability信息，可以通过  
[getLauncherAbilityInfoSync](arkts-ability-launcherbundlemanager-getlauncherabilityinfosync-f.md#getlauncherabilityinfosync)&lt;!--Del--&gt;或者  
[getLauncherAbilityInfo](arkts-ability-launcherbundlemanager-getlauncherabilityinfo-f-sys.md#getlauncherabilityinfo)&lt;!--DelEnd--&gt;获取。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface LauncherAbilityInfo--><!--Device-unnamed-export interface LauncherAbilityInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## applicationInfo

```TypeScript
readonly applicationInfo: ApplicationInfo
```

launcher ability的应用程序配置信息。

**Type:** [ApplicationInfo](arkts-ability-applicationinfo-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-LauncherAbilityInfo-readonly applicationInfo: ApplicationInfo--><!--Device-LauncherAbilityInfo-readonly applicationInfo: ApplicationInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## elementName

```TypeScript
readonly elementName: ElementName
```

launcher ability的ElementName信息。

**Type:** [ElementName](arkts-ability-elementname-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-LauncherAbilityInfo-readonly elementName: ElementName--><!--Device-LauncherAbilityInfo-readonly elementName: ElementName-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## iconId

```TypeScript
readonly iconId: long
```

launcher ability的图标的资源ID值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-LauncherAbilityInfo-readonly iconId: long--><!--Device-LauncherAbilityInfo-readonly iconId: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## installTime

```TypeScript
readonly installTime: long
```

launcher ability的安装时间戳，单位毫秒。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-LauncherAbilityInfo-readonly installTime: long--><!--Device-LauncherAbilityInfo-readonly installTime: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## labelId

```TypeScript
readonly labelId: long
```

launcher ability的名称的资源ID值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-LauncherAbilityInfo-readonly labelId: long--><!--Device-LauncherAbilityInfo-readonly labelId: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## userId

```TypeScript
readonly userId: int
```

launcher ability的用户ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-LauncherAbilityInfo-readonly userId: int--><!--Device-LauncherAbilityInfo-readonly userId: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

