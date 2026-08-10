# TemplateStatusCallback (System API)

```TypeScript
type TemplateStatusCallback = (templateStatusList: TemplateStatus[]) => void
```

回调函数，用于接收模板状态变化通知。当模板状态发生变化（如添加、删除、有效性变更等）时，系统会通过此回调通知应用。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-companionDeviceAuth-type TemplateStatusCallback = (templateStatusList: TemplateStatus[]) => void--><!--Device-companionDeviceAuth-type TemplateStatusCallback = (templateStatusList: TemplateStatus[]) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| templateStatusList | [TemplateStatus](arkts-userauthentication-companiondeviceauth-templatestatus-i-sys.md)[] | Yes | 模板状态列表。包含当前用户下所有已注册模板的状态信息，应用可根据列表中的isValid字段判断模板有效性，根据isConfirmed 字段判断数据是否为实时数据。 |

