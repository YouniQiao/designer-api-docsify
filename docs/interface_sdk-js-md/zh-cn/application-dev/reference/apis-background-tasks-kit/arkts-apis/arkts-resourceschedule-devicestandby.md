# @ohos.resourceschedule.deviceStandby(设备待机模块)

当设备长时间未被使用，或通过按键操作时，可以使设备进入待机模式。待机模式不影响应用使用，还可以延长电池续航时间。通过本模块接口，可查询设备或应用是否为待机模式，以及为应用申请或取消待机资源管控。

> **说明：**:&gt;
> 本模块接口为系统接口。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ResourceSchedule.DeviceStandby

## 导入模块

```TypeScript
import { deviceStandby } from '@kit.BackgroundTasksKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getExemptedApps(设备待机模块)](arkts-backgroundtasks-devicestandby-getexemptedapps-f-sys.md) |
| [getExemptedApps(设备待机模块)](arkts-backgroundtasks-devicestandby-getexemptedapps-f-sys.md) |
| [releaseExemptionResource(设备待机模块)](arkts-backgroundtasks-devicestandby-releaseexemptionresource-f-sys.md) |
| [requestExemptionResource(设备待机模块)](arkts-backgroundtasks-devicestandby-requestexemptionresource-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [ExemptedAppInfo(设备待机模块)](arkts-backgroundtasks-devicestandby-exemptedappinfo-i-sys.md) |
| [ResourceRequest(设备待机模块)](arkts-backgroundtasks-devicestandby-resourcerequest-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ResourceType(设备待机模块)](arkts-backgroundtasks-devicestandby-resourcetype-e-sys.md) |
<!--DelEnd-->
