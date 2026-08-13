# wantAgent

WantAgent模块封装了[Want](arkts-ability-app-ability-want-want-c.md#Want)对象，允许应用程序在未来的某个时间点触发WantAgent实例执行指定操作（如启动Ability、发送公共事件等）。 该模块提供了创建WantAgent实例、获取WantAgent实例所属应用的包名、获取WantAgent实例所属应用的UID、主动触发WantAgent实例、判断两个WantAgent实例是否相等等功能。WantAgent的一个典型应 用场景是通知处理。例如，当用户点击通知时，会触发WantAgent的[trigger](arkts-ability-wantagent-trigger-f.md#trigger)接口，并拉起目标应用。具体使用请参考[Notification](../../../notification/notification-with-wantagent.md)。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace wantAgent--><!--Device-unnamed-declare namespace wantAgent-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 汇总

### 函数

| 名称 |
| --- |
| [getBundleName](arkts-ability-wantagent-getbundlename-f.md#getBundleName) |
| [getBundleName](arkts-ability-wantagent-getbundlename-f.md#getBundleName) |
| [getUid](arkts-ability-wantagent-getuid-f.md#getUid) |
| [getUid](arkts-ability-wantagent-getuid-f.md#getUid) |
| [cancel](arkts-ability-wantagent-cancel-f.md#cancel) |
| [cancel](arkts-ability-wantagent-cancel-f.md#cancel) |
| [trigger](arkts-ability-wantagent-trigger-f.md#trigger) |
| [equal](arkts-ability-wantagent-equal-f.md#equal) |
| [equal](arkts-ability-wantagent-equal-f.md#equal) |
| [getWantAgent](arkts-ability-wantagent-getwantagent-f.md#getWantAgent) |
| [getWantAgent](arkts-ability-wantagent-getwantagent-f.md#getWantAgent) |
| [getOperationType](arkts-ability-wantagent-getoperationtype-f.md#getOperationType) |
| [getOperationType](arkts-ability-wantagent-getoperationtype-f.md#getOperationType) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getWant](arkts-ability-wantagent-getwant-f-sys.md#getWant（系统接口）) |
| [getWant](arkts-ability-wantagent-getwant-f-sys.md#getWant（系统接口）) |
| [triggerAsync](arkts-ability-wantagent-triggerasync-f-sys.md#triggerAsync（系统接口）) |
| [setWantAgentMultithreading](arkts-ability-wantagent-setwantagentmultithreading-f-sys.md#setWantAgentMultithreading（系统接口）) |
| [createLocalWantAgent](arkts-ability-wantagent-createlocalwantagent-f-sys.md#createLocalWantAgent（系统接口）) |
| [isLocalWantAgent](arkts-ability-wantagent-islocalwantagent-f-sys.md#isLocalWantAgent（系统接口）) |
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
