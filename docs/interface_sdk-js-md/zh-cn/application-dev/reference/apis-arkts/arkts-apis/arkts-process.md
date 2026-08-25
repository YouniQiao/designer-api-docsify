# @ohos.process

获取进程相关的信息，提供进程管理的相关功能。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { process } from '@kit.ArkTS';
```

## 汇总

### 函数

| 名称 |
| --- |
| [abort](arkts-arkts-process-abort-f.md) |
| [exit](arkts-arkts-process-exit-f.md) |
| [getEnvironmentVar](arkts-arkts-process-getenvironmentvar-f.md) |
| [getPastCpuTime](arkts-arkts-process-getpastcputime-f.md) |
| [getStartRealtime](arkts-arkts-process-getstartrealtime-f.md) |
| [getSystemConfig](arkts-arkts-process-getsystemconfig-f.md) |
| [getThreadPriority](arkts-arkts-process-getthreadpriority-f.md) |
| [getUidForName](arkts-arkts-process-getuidforname-f.md) |
| [is64Bit](arkts-arkts-process-is64bit-f.md) |
| [isAppUid](arkts-arkts-process-isappuid-f.md) |
| [isIsolatedProcess](arkts-arkts-process-isisolatedprocess-f.md) |
| [kill](arkts-arkts-process-kill-f.md) |
| [uptime](arkts-arkts-process-uptime-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [chdir](arkts-arkts-process-chdir-f-sys.md) |
| [cwd](arkts-arkts-process-cwd-f-sys.md) |
| [off](arkts-arkts-process-off-f-sys.md) |
| [on](arkts-arkts-process-on-f-sys.md) |
| [runCmd](arkts-arkts-process-runcmd-f-sys.md) |
<!--DelEnd-->

### 类

| 名称 |
| --- |
| [ProcessManager](arkts-arkts-process-processmanager-c.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ChildProcess](arkts-arkts-process-childprocess-i-sys.md) |
| [ConditionType](arkts-arkts-process-conditiontype-i-sys.md) |
<!--DelEnd-->

### 类型

| 名称 |
| --- |
| [EventListener](arkts-arkts-process-eventlistener-t.md) |

### 常量

| 名称 |
| --- |
| [pid](arkts-arkts-process-con.md#pid) |
| [tid](arkts-arkts-process-con.md#tid) |
| [uid](arkts-arkts-process-con.md#uid) |

<!--Del-->
### 常量（系统接口）

| 名称 |
| --- |
| [egid](arkts-arkts-process-con-sys.md#egid) |
| [euid](arkts-arkts-process-con-sys.md#euid) |
| [gid](arkts-arkts-process-con-sys.md#gid) |
| [groups](arkts-arkts-process-con-sys.md#groups) |
| [ppid](arkts-arkts-process-con-sys.md#ppid) |
<!--DelEnd-->
