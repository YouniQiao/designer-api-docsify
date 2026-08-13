# @ohos.enterprise.dateTimeManager

The **dateTimeManager** module provides APIs for system time management. > **NOTE：**> > The APIs of this module are available only to > [MDM applications](../../../mdm/mdm-kit-term.md#mdm-application-device-administrator-application), and can be > called only after the device administrator application is activated via > [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableAdmin-(System-API)).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace dateTimeManager--><!--Device-unnamed-declare namespace dateTimeManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dateTimeManager } from '@kit.MDMKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [disallowModifyDateTime](arkts-mdm-datetimemanager-disallowmodifydatetime-f-sys.md#disallowModifyDateTime) | Disallows the device to modify the system time. This API uses an asynchronous callback to return the result. |
| [disallowModifyDateTime](arkts-mdm-datetimemanager-disallowmodifydatetime-f-sys.md#disallowModifyDateTime-(System-API)) | Disallows the device to modify the system time. This API uses a promise to return the result. |
| [isModifyDateTimeDisallowed](arkts-mdm-datetimemanager-ismodifydatetimedisallowed-f-sys.md#isModifyDateTimeDisallowed) | Queries whether the system time of a device can be modified. This API uses an asynchronous callback to return the result. |
| [isModifyDateTimeDisallowed](arkts-mdm-datetimemanager-ismodifydatetimedisallowed-f-sys.md#isModifyDateTimeDisallowed-(System-API)) | Queries whether the system time of a device can be modified. This API uses a promise to return the result. |
| [setDateTime](arkts-mdm-datetimemanager-setdatetime-f-sys.md#setDateTime) | Sets the system time. This API uses an asynchronous callback to return the result. |
| [setDateTime](arkts-mdm-datetimemanager-setdatetime-f-sys.md#setDateTime-(System-API)) | Sets the system time. This API uses a promise to return the result. |
<!--DelEnd-->

