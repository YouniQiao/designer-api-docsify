# ModuleInfo

应用程序的模块信息。

> **说明：**
> 
> 从API version 9开始，该模块不再维护，建议使用[bundleManager-HapModuleInfo](arkts-ability-hapmoduleinfo-i.md)替代。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [hapModuleInfo:HapModuleInfo](arkts-ability-hapmoduleinfo-i.md)

<!--Device-unnamed-export interface ModuleInfo--><!--Device-unnamed-export interface ModuleInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## moduleName

```TypeScript
readonly moduleName: string
```

模块名称。

**Type:** string

**Default:** Indicates the name of the .hap package to which the capability belongs

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.bundle.bundleManager/bundleManager.HapModuleInfo#name

<!--Device-ModuleInfo-readonly moduleName: string--><!--Device-ModuleInfo-readonly moduleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

## moduleSourceDir

```TypeScript
readonly moduleSourceDir: string
```

安装目录。不能拼接路径访问资源文件，请使用[资源管理接口](../../apis-localization-kit/arkts-apis/arkts-resourcemanager.md/arkts-resourcemanager.md)访问资源。

**Type:** string

**Default:** Indicates the module source dir of this module

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-ModuleInfo-readonly moduleSourceDir: string--><!--Device-ModuleInfo-readonly moduleSourceDir: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

