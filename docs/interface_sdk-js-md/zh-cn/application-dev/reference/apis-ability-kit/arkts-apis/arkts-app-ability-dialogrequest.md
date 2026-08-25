# @ohos.app.ability.dialogRequest

dialogRequest模块用于处理模态弹框的能力，包括获取RequestInfo（用于绑定模态弹框）、获取RequestCallback（用于设置结果）。模态弹框是指一个系统弹框，该弹框会拦截弹框之下的页面的鼠标、键盘、触屏等事件。销毁该弹框后，才能对页面进行操作。

> **说明：**&gt;
> - 本模块接口可以在ServiceExtensionAbility下使用，如果ServiceExtensionAbility实现了模态弹框，则可以使用本模块的接口获取请求方的RequestInfo、RequestCallback并
> 返回请求结果。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { dialogRequest } from 'kits/@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getRequestCallback](arkts-ability-dialogrequest-getrequestcallback-f.md) |
| [getRequestInfo](arkts-ability-dialogrequest-getrequestinfo-f.md) |

### 接口

| 名称 |
| --- |
| [RequestCallback](arkts-ability-dialogrequest-requestcallback-i.md) |
| [RequestInfo](arkts-ability-dialogrequest-requestinfo-i.md) |
| [RequestResult](arkts-ability-dialogrequest-requestresult-i.md) |
| [WindowRect](arkts-ability-dialogrequest-windowrect-i.md) |

### 枚举

| 名称 |
| --- |
| [ResultCode](arkts-ability-dialogrequest-resultcode-e.md) |
