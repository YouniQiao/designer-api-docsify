# offSystemLoadChange

## 导入模块

```TypeScript
import { systemLoad } from 'kits/@kit.BasicServicesKit';
```

## offSystemLoadChange

```TypeScript
function offSystemLoadChange(callback?: Callback<SystemLoadLevel>): void
```

Unregister system load callback for perception system load change

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-systemLoad-function offSystemLoadChange(callback?: Callback<SystemLoadLevel>): void--><!--Device-systemLoad-function offSystemLoadChange(callback?: Callback<SystemLoadLevel>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.SystemLoad

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;SystemLoadLevel&gt; | 否 | Asynchronous callback interface. |

