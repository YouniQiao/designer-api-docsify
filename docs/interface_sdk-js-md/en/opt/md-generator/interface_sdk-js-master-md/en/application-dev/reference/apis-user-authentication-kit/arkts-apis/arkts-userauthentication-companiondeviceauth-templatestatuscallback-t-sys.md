# TemplateStatusCallback (System API)

```TypeScript
type TemplateStatusCallback = (templateStatusList: TemplateStatus[]) => void
```

Defines the callback triggered for receiving notifications of template status changes. When the template status changes (for example, the template is added, deleted, or its validity changes), the system notifies the application through this callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-companionDeviceAuth-type TemplateStatusCallback = (templateStatusList: TemplateStatus[]) => void--><!--Device-companionDeviceAuth-type TemplateStatusCallback = (templateStatusList: TemplateStatus[]) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| templateStatusList | [TemplateStatus](arkts-userauthentication-companiondeviceauth-templatestatus-i-sys.md)[] | Yes |
