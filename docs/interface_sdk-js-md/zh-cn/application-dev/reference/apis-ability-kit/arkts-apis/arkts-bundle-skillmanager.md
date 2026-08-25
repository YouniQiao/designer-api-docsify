# @ohos.bundle.skillManager

本模块提供技能（Skill）信息的查询能力，支持查询应用自身的技能信息、指定应用的技能信息以及所有应用的技能信息。AI代理框架在规划任务时，可通过本模块查询设备上所有应用可用的技能， 选择合适的技能来完成用户请求。通过技能信息查询，可以实现智能任务调度、能力匹配优化，提升AI代理的任务执行效率，降低开发者的技能集成复杂度。@namespace skillManager

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

## 导入模块

```TypeScript
import { skillManager } from 'kits/@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getAllSkillInfos](arkts-ability-skillmanager-getallskillinfos-f.md) |
| [getSkillInfo](arkts-ability-skillmanager-getskillinfo-f.md) |
| [getSkillInfoForSelf](arkts-ability-skillmanager-getskillinfoforself-f.md) |
| [getSkillInfos](arkts-ability-skillmanager-getskillinfos-f.md) |
| [getSkillInfosForSelf](arkts-ability-skillmanager-getskillinfosforself-f.md) |

### 枚举

| 名称 |
| --- |
| [SkillInfoFlag](arkts-ability-skillmanager-skillinfoflag-e.md) |

### 类型

| 名称 |
| --- |
| [SkillInfo](arkts-ability-skillmanager-skillinfo-t.md) |
| [SkillType](arkts-ability-skillmanager-skilltype-t.md) |
