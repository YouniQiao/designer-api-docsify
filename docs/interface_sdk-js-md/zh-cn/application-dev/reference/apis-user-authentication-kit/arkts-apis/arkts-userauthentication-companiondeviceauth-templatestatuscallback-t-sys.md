# TemplateStatusCallback（系统接口）

```TypeScript
type TemplateStatusCallback = (templateStatusList: TemplateStatus[]) => void
```

回调函数，用于接收模板状态变化通知。当模板状态发生变化（如添加、删除、有效性变更等）时，系统会通过此回调通知应用。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| templateStatusList | [TemplateStatus](arkts-userauthentication-companiondeviceauth-templatestatus-i-sys.md)[] | 是 |
