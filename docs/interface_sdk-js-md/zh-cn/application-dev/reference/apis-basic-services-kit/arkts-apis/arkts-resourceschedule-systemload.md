# @ohos.resourceschedule.systemload(性能功耗热融合档位)

系统根据当前温度、负载以及是否处于高负载场景等信息决策出系统负载融合档位，并在档位变化时通知已注册的应用。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ResourceSchedule.SystemLoad

## 导入模块

```TypeScript
import { systemLoad } from '@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getLevel(性能功耗热融合档位)](arkts-basicservices-systemload-getlevel-f.md) |
| [off(性能功耗热融合档位)](arkts-basicservices-systemload-off-f.md#offsystemloadchange) |
| [offSystemLoadChange(性能功耗热融合档位)](arkts-basicservices-systemload-offsystemloadchange-f.md) |
| [on(性能功耗热融合档位)](arkts-basicservices-systemload-on-f.md#onsystemloadchange) |
| [onSystemLoadChange(性能功耗热融合档位)](arkts-basicservices-systemload-onsystemloadchange-f.md) |

### 枚举

| 名称 |
| --- |
| [SystemLoadLevel(性能功耗热融合档位)](arkts-basicservices-systemload-systemloadlevel-e.md) |
