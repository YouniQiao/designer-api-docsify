# ExemptedAppInfo（系统接口）

豁免应用信息，未进入待机管控的应用信息。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-deviceStandby-export interface ExemptedAppInfo--><!--Device-deviceStandby-export interface ExemptedAppInfo-End-->

**系统能力：** SystemCapability.ResourceSchedule.DeviceStandby

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { deviceStandby } from 'kits/@kit.BackgroundTasksKit';
```

## duration

```TypeScript
duration: int
```

豁免时长。单位：s

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-ExemptedAppInfo-duration: int--><!--Device-ExemptedAppInfo-duration: int-End-->

**系统能力：** SystemCapability.ResourceSchedule.DeviceStandby

**系统接口：** 此接口为系统接口。

## name

```TypeScript
name: string
```

应用名。

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-ExemptedAppInfo-name: string--><!--Device-ExemptedAppInfo-name: string-End-->

**系统能力：** SystemCapability.ResourceSchedule.DeviceStandby

**系统接口：** 此接口为系统接口。

## resourceTypes

```TypeScript
resourceTypes: int
```

资源类型，类型具体说明请参考[ResourceType](arkts-backgroundtasks-devicestandby-resourcetype-e-sys.md)。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-ExemptedAppInfo-resourceTypes: int--><!--Device-ExemptedAppInfo-resourceTypes: int-End-->

**系统能力：** SystemCapability.ResourceSchedule.DeviceStandby

**系统接口：** 此接口为系统接口。

