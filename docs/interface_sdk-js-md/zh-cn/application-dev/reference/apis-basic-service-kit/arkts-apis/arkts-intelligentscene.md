# @ohos.intelligentScene

This module provides system focus modes and Do Not Disturb data access abilities.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace intelligentScene--><!--Device-unnamed-declare namespace intelligentScene-End-->

**系统能力：** SystemCapability.Applications.IntelligentScene

## 导入模块

```TypeScript
import { intelligentScene } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [isDoNotDisturbEnabled](arkts-basicservices-intelligentscene-isdonotdisturbenabled-f.md#isdonotdisturbenabled) | Checks whether Do Not Disturb is enabled on this device.The Do Not Disturb state defines if notifications are allowed to interrupt the user (e.g. via sound & vibration) and is applied globally. |
| [isNotifyAllowedInDoNotDisturb](arkts-basicservices-intelligentscene-isnotifyallowedindonotdisturb-f.md#isnotifyallowedindonotdisturb) | Checks whether calling bundle is allow notify(e.g. sound & vibration) when system Do Not Disturb is on. |

