# bundleManager/Skill

The module defines a skill object. Such an object can be obtained through
 [bundleManager.getBundleInfoForSelf](../arkts-ability-bundlemanager-getbundleinfoforself-f.md#getbundleinfoforself)
 , with at least **GET_BUNDLE_INFO_WITH_HAP_MODULE**, **GET_BUNDLE_INFO_WITH_ABILITY**, and
 **GET_BUNDLE_INFO_WITH_SKILL** passed in to **bundleFlags**. (The skill information is contained in
 [BundleInfo](../arkts-ability-bundlemanager/bundleinfo-bundleinfo-i.md) -> [HapModuleInfo](../arkts-ability-bundlemanager/hapmoduleinfo-hapmoduleinfo-i.md) -> [AbilityInfo](../arkts-ability-bundlemanager/abilityinfo-abilityinfo-i.md) or
 [ExtensionAbilityInfo](../arkts-ability-bundlemanager/extensionabilityinfo-extensionabilityinfo-i.md).)


## 汇总

### 接口

| 名称 | 说明 |
| --- | --- |
| [Skill](skill-skill-i.md) | skill标签对象。 |
| [SkillUri](skill-skilluri-i.md) | Want匹配的Uri集合。 |

