# @ohos.bundle.skillManager

This module provides skill query capabilities for applications.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare namespace skillManager--><!--Device-unnamed-declare namespace skillManager-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAllSkillInfos](arkts-ability-skillmanager-getallskillinfos-f.md#getallskillinfos) | Obtains all SkillInfo objects installed on the device.To query information for other local accounts, the permission ohos.permission.INTERACT\_\_\_ESCAPED\_UNDERSCORE\_\_\_ACROSS\_\_\_ESCAPED\_UNDERSCORE\_\_\_LOCAL\_\_\_ESCAPED\_UNDERSCORE\_\_\_ACCOUNTS must additionally be granted. |
| [getSkillInfo](arkts-ability-skillmanager-getskillinfo-f.md#getskillinfo) | Obtains SkillInfo of a specified application based on bundleName, moduleName and skillName.To query information for other local accounts, the permission ohos.permission.INTERACT\_\_\_ESCAPED\_UNDERSCORE\_\_\_ACROSS\_\_\_ESCAPED\_UNDERSCORE\_\_\_LOCAL\_\_\_ESCAPED\_UNDERSCORE\_\_\_ACCOUNTS must additionally be granted. |
| [getSkillInfoForSelf](arkts-ability-skillmanager-getskillinfoforself-f.md#getskillinfoforself) | Obtains SkillInfo of the calling application based on moduleName and skillName. |
| [getSkillInfos](arkts-ability-skillmanager-getskillinfos-f.md#getskillinfos) | Obtains all SkillInfo of a specified application based on bundleName.To query information for other local accounts, the permission ohos.permission.INTERACT\_\_\_ESCAPED\_UNDERSCORE\_\_\_ACROSS\_\_\_ESCAPED\_UNDERSCORE\_\_\_LOCAL\_\_\_ESCAPED\_UNDERSCORE\_\_\_ACCOUNTS must additionally be granted. |
| [getSkillInfosForSelf](arkts-ability-skillmanager-getskillinfosforself-f.md#getskillinfosforself) | Obtains all SkillInfo objects of the calling application. |

### Enums

| Name | Description |
| --- | --- |
| [SkillInfoFlag](arkts-ability-skillmanager-skillinfoflag-e.md) | Enumeration of flags used to control what content is populated in a SkillInfo.Multiple flags can be combined using bitwise OR, for example GET\_\_\_ESCAPED\_UNDERSCORE\_\_\_SKILL\_\_\_ESCAPED\_UNDERSCORE\_\_\_INFO\_\_\_ESCAPED\_UNDERSCORE\_\_\_WITH\_\_\_ESCAPED\_UNDERSCORE\_\_\_SRC\_\_\_ESCAPED\_UNDERSCORE\_\_\_ENTRIES \| GET\_\_\_ESCAPED\_UNDERSCORE\_\_\_SKILL\_\_\_ESCAPED\_UNDERSCORE\_\_\_INFO\_\_\_ESCAPED\_UNDERSCORE\_\_\_WITH\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESCRIPTION. |

### Types

| Name | Description |
| --- | --- |
| [SkillInfo](arkts-ability-skillmanager-skillinfo-t.md) | Provides information about a skill, including skill name, type, and associated metadata. |
| [SkillType](arkts-ability-skillmanager-skilltype-t.md) | Enumerates the skill types. |

