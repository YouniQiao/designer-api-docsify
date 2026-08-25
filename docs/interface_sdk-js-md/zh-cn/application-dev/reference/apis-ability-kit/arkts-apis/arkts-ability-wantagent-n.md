# wantAgent

WantAgent模块封装了[Want](arkts-ability-app-ability-want-want-c.md)对象，允许应用程序在未来的某个时间点触发WantAgent实例执行指定操作（如启动Ability、发送公共事件等）。该模块提供了创建WantAgent实例、获取WantAgent实例所属应用的包名、获取WantAgent实例所属应用的UID、主动触发WantAgent实例、判断两个WantAgent实例是否相等等功能。WantAgent的一个典型应 用场景是通知处理。例如，当用户点击通知时，会触发WantAgent的[trigger](arkts-ability-wantagent-trigger-f.md)接口，并拉起目标应用。具体使用请参考[Notification](../../../notification/notification-with-wantagent.md)。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { wantAgent, WantAgent } from 'kits/@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getBundleName](arkts-ability-wantagent-getbundlename-f.md) |
| [getBundleName](arkts-ability-wantagent-getbundlename-f.md) |
| [getUid](arkts-ability-wantagent-getuid-f.md) |
| [getUid](arkts-ability-wantagent-getuid-f.md) |
| [cancel](arkts-ability-wantagent-cancel-f.md) |
| [cancel](arkts-ability-wantagent-cancel-f.md) |
| [trigger](arkts-ability-wantagent-trigger-f.md) |
| [equal](arkts-ability-wantagent-equal-f.md) |
| [equal](arkts-ability-wantagent-equal-f.md) |
| [getWantAgent](arkts-ability-wantagent-getwantagent-f.md) |
| [getWantAgent](arkts-ability-wantagent-getwantagent-f.md) |
| [getOperationType](arkts-ability-wantagent-getoperationtype-f.md) |
| [getOperationType](arkts-ability-wantagent-getoperationtype-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getWant](arkts-ability-wantagent-getwant-f-sys.md) |
| [getWant](arkts-ability-wantagent-getwant-f-sys.md) |
| [triggerAsync](arkts-ability-wantagent-triggerasync-f-sys.md) |
| [setWantAgentMultithreading](arkts-ability-wantagent-setwantagentmultithreading-f-sys.md) |
| [createLocalWantAgent](arkts-ability-wantagent-createlocalwantagent-f-sys.md) |
| [isLocalWantAgent](arkts-ability-wantagent-islocalwantagent-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [CompleteData](arkts-ability-wantagent-completedata-i.md) |

### 枚举

| 名称 |
| --- |
| [WantAgentFlags](arkts-ability-wantagent-wantagentflags-e.md) |
| [OperationType](arkts-ability-wantagent-operationtype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [OperationType](arkts-ability-wantagent-operationtype-e-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [TriggerInfo](arkts-ability-wantagent-triggerinfo-t.md) |
| [WantAgentInfo](arkts-ability-wantagent-wantagentinfo-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [LocalWantAgentInfo](arkts-ability-wantagent-localwantagentinfo-t-sys.md) |
<!--DelEnd-->
