# @ohos.app.ability.dialogRequest

dialogRequest模块用于处理模态弹框的能力，包括获取RequestInfo（用于绑定模态弹框）、获取RequestCallback（用于设置结果）。

模态弹框是指一个系统弹框，该弹框会拦截弹框之下的页面的鼠标、键盘、触屏等事件。销毁该弹框后，才能对页面进行操作。

> **说明：**
> 
> - 本模块接口可以在ServiceExtensionAbility下使用，如果ServiceExtensionAbility实现了模态弹框，则可以使用本模块的接口获取请求方的RequestInfo、RequestCallback并
> 返回请求结果。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace dialogRequest--><!--Device-unnamed-declare namespace dialogRequest-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { dialogRequest } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getRequestCallback](arkts-ability-dialogrequest-getrequestcallback-f.md#getrequestcallback) | 从Want中获取请求方的RequestCallback。 |
| [getRequestInfo](arkts-ability-dialogrequest-getrequestinfo-f.md#getrequestinfo) | 从Want中获取请求方的RequestInfo。 |

### Interfaces

| Name | Description |
| --- | --- |
| [RequestCallback](arkts-ability-dialogrequest-requestcallback-i.md) | 用于设置模态弹框请求结果的callback接口。 |
| [RequestInfo](arkts-ability-dialogrequest-requestinfo-i.md) | 表示发起方请求信息，作为窗口绑定模态弹框的入参。 |
| [RequestResult](arkts-ability-dialogrequest-requestresult-i.md) | 模态弹框请求结果，包含结果码ResultCode和请求结果ResultWant。 |
| [WindowRect](arkts-ability-dialogrequest-windowrect-i.md) | 表示模态弹框的属性。 |

### Enums

| Name | Description |
| --- | --- |
| [ResultCode](arkts-ability-dialogrequest-resultcode-e.md) | 模态弹框请求结果码。 |

