# @ohos.runningLock

该模块为RunningLock锁相关操作的接口，提供阻止系统睡眠和使能接近光控制亮灭屏的能力，适用于设备灭屏后保持后台任务持续运行、接近光控制亮灭屏、以及阻止系统闲时自动睡眠等场景，保证关键任务的持续执行。 包括创建、查询、持锁、释放锁等操作，类型详情见[RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md)。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

## 导入模块

```TypeScript
import { runningLock } from '@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [create](arkts-basicservices-runninglock-create-f.md) |
| [create](arkts-basicservices-runninglock-create-f.md) |
| [createRunningLock](arkts-basicservices-runninglock-createrunninglock-f.md) |
| [createRunningLock](arkts-basicservices-runninglock-createrunninglock-f.md) |
| [isRunningLockTypeSupported](arkts-basicservices-runninglock-isrunninglocktypesupported-f.md) |
| [isRunningLockTypeSupported](arkts-basicservices-runninglock-isrunninglocktypesupported-f.md) |
| [isSupported](arkts-basicservices-runninglock-issupported-f.md) |

### 类

| 名称 |
| --- |
| [RunningLock](arkts-basicservices-runninglock-runninglock-c.md) |

### 枚举

| 名称 |
| --- |
| [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) |
