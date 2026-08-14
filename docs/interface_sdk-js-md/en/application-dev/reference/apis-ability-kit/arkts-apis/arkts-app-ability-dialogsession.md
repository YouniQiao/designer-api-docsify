# @ohos.app.ability.dialogSession

The dialogSession module provides APIs related to the dialog box.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace dialogSession--><!--Device-unnamed-declare namespace dialogSession-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dialogSession } from 'dialogSession';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getDialogSessionInfo](arkts-ability-dialogsession-getdialogsessioninfo-f-sys.md#getDialogSessionInfo) | Obtains the session information based on the session ID. |
| [getDialogSessionInfo](arkts-ability-dialogsession-getdialogsessioninfo-f-sys.md#getDialogSessionInfo-(System-API)) | Query the session info of dialog. |
| [sendDialogResult](arkts-ability-dialogsession-senddialogresult-f-sys.md#sendDialogResult) | Sends a request for a dialog box. This API uses a promise to return the result. |
| [sendDialogResult](arkts-ability-dialogsession-senddialogresult-f-sys.md#sendDialogResult-(System-API)) | Sends a request for a dialog box. This API uses an asynchronous callback to return the result. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [DialogAbilityInfo](arkts-ability-dialogsession-dialogabilityinfo-i-sys.md) | Provides DialogAbility information, including the bundle name, module name, and ability name. |
| [DialogSessionInfo](arkts-ability-dialogsession-dialogsessioninfo-i-sys.md) | Provides session information, including the requester information, target ability information list, and other parameters. |
<!--DelEnd-->

