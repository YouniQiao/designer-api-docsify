# SkillInfo

提供Skill的相关信息。Skill是一个可安装的能力单位，可以被发现并由Agent框架调用。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export interface SkillInfo--><!--Device-unnamed-export interface SkillInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## abilityName

```TypeScript
readonly abilityName: string
```

Skill关联的ability名称。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SkillInfo-readonly abilityName: string--><!--Device-SkillInfo-readonly abilityName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## bundleName

```TypeScript
readonly bundleName: string
```

Skill的应用名称。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SkillInfo-readonly bundleName: string--><!--Device-SkillInfo-readonly bundleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## description

```TypeScript
readonly description?: string
```

Skill的描述信息。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SkillInfo-readonly description?: string--><!--Device-SkillInfo-readonly description?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## moduleName

```TypeScript
readonly moduleName: string
```

Skill的模块名称。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SkillInfo-readonly moduleName: string--><!--Device-SkillInfo-readonly moduleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## permissions

```TypeScript
readonly permissions?: Array<string>
```

Skill所需的权限。

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SkillInfo-readonly permissions?: Array<string>--><!--Device-SkillInfo-readonly permissions?: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## requestPermissions

```TypeScript
readonly requestPermissions?: Array<string>
```

表示应用包中requestPermissions下声明的权限。

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SkillInfo-readonly requestPermissions?: Array<string>--><!--Device-SkillInfo-readonly requestPermissions?: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## skillName

```TypeScript
readonly skillName: string
```

Skill名称。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SkillInfo-readonly skillName: string--><!--Device-SkillInfo-readonly skillName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## skillPath

```TypeScript
readonly skillPath: string
```

Skill的安装包路径。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SkillInfo-readonly skillPath: string--><!--Device-SkillInfo-readonly skillPath: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## skillType

```TypeScript
readonly skillType: SkillType
```

Skill类型。

**Type:** [SkillType](arkts-ability-skillmanager-skilltype-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SkillInfo-readonly skillType: SkillType--><!--Device-SkillInfo-readonly skillType: SkillType-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## srcEntries

```TypeScript
readonly srcEntries?: Array<string>
```

Skill的srcEntries信息。

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SkillInfo-readonly srcEntries?: Array<string>--><!--Device-SkillInfo-readonly srcEntries?: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## versionCode

```TypeScript
readonly versionCode: long
```

Skill的版本号。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-SkillInfo-readonly versionCode: long--><!--Device-SkillInfo-readonly versionCode: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

