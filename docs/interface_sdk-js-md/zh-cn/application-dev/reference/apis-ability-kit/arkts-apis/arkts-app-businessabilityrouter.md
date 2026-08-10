# @ohos.app.businessAbilityRouter

This module is used to obtain business ability information of various applications installed on the current device.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace businessAbilityRouter--><!--Device-unnamed-declare namespace businessAbilityRouter-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { businessAbilityRouter } from 'kits/@kit.AbilityKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [queryBusinessAbilityInfo](arkts-ability-businessabilityrouter-querybusinessabilityinfo-f-sys.md#querybusinessabilityinfo) | Query the business ability info of by the given filter. ohos.permission.GET_BUNDLE_INFO_PRIVILEGED is required for cross user access. |
| [queryBusinessAbilityInfo](arkts-ability-businessabilityrouter-querybusinessabilityinfo-f-sys.md#querybusinessabilityinfo-1) | Query the business ability info of by the given filter. ohos.permission.GET_BUNDLE_INFO_PRIVILEGED is required for cross user access. |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [BusinessAbilityFilter](arkts-ability-businessabilityrouter-businessabilityfilter-i-sys.md) | This filter value is used to filter business ability info |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [BusinessType](arkts-ability-businessabilityrouter-businesstype-e-sys.md) | This enumeration value is used to identify various types of business ability info |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 | 说明 |
| --- | --- |
| [BusinessAbilityInfo](arkts-ability-businessabilityrouter-businessabilityinfo-t-sys.md) | Obtains business ability info. |
<!--DelEnd-->

