# @ohos.app.ability.application

开发者可以通过该模块创建[Context](../../../application-models/application-context-stage.md)。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { application } from '@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createModuleContext](arkts-ability-application-createmodulecontext-f.md) |
| [createModuleContextSync](arkts-ability-application-createmodulecontextsync-f.md) |
| [createPluginModuleContext](arkts-ability-application-createpluginmodulecontext-f.md) |
| [demoteCurrentFromCandidateMasterProcess](arkts-ability-application-demotecurrentfromcandidatemasterprocess-f.md) |
| [exitMasterProcessRole](arkts-ability-application-exitmasterprocessrole-f.md) |
| [getApplicationContext](arkts-ability-application-getapplicationcontext-f.md) |
| [getApplicationContextInstance](arkts-ability-application-getapplicationcontextinstance-f.md) |
| [getAppPreloadType](arkts-ability-application-getapppreloadtype-f.md) |
| [promoteCurrentToCandidateMasterProcess](arkts-ability-application-promotecurrenttocandidatemasterprocess-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [createBundleContext](arkts-ability-application-createbundlecontext-f-sys.md) |
| [createModuleContext](arkts-ability-application-createmodulecontext-f-sys.md) |
| [createPluginModuleContextForHostBundle](arkts-ability-application-createpluginmodulecontextforhostbundle-f-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AppPreloadType](arkts-ability-application-apppreloadtype-e.md) |
