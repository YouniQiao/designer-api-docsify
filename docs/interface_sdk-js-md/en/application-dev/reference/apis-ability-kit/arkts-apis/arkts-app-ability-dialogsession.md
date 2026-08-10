# @ohos.app.ability.dialogSession

dialogSession模块用于支持系统应用弹框功能。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace dialogSession--><!--Device-unnamed-declare namespace dialogSession-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dialogSession } from 'kits/@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getDialogSessionInfo](arkts-ability-dialogsession-getdialogsessioninfo-f-sys.md#getdialogsessioninfo) | 通过dialogSessionId获取会话信息。 |
| [getDialogSessionInfo](arkts-ability-dialogsession-getdialogsessioninfo-f-sys.md#getdialogsessioninfo-1) | 根据dialogSessionId获取会话信息。 |
| [sendDialogResult](arkts-ability-dialogsession-senddialogresult-f-sys.md#senddialogresult) | 发送用户请求。使用Promise异步回调。 |
| [sendDialogResult](arkts-ability-dialogsession-senddialogresult-f-sys.md#senddialogresult-1) | 发送用户请求。使用callback异步回调。 |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [DialogAbilityInfo](arkts-ability-dialogsession-dialogabilityinfo-i-sys.md) | 提供会话组件信息，包括包名、模块名、组件名等信息。 |
| [DialogSessionInfo](arkts-ability-dialogsession-dialogsessioninfo-i-sys.md) | 提供会话信息，包括请求方信息、目标组件信息列表、其他参数。 |
<!--DelEnd-->

