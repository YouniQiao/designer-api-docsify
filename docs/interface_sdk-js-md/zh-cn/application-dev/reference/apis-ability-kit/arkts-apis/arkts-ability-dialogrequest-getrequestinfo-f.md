# getRequestInfo

## 导入模块

```TypeScript
import { dialogRequest } from 'kits/@kit.AbilityKit';
```

## getRequestInfo

```TypeScript
function getRequestInfo(want: Want): RequestInfo
```

从Want中获取请求方的RequestInfo。

> **说明：**&gt;
> 该接口可以在ServiceExtensionAbility下使用，如果ServiceExtensionAbility实现了模态弹框，则能从Want中获取请求方的RequestInfo。其他场景使用该接口，均无法获取返回值。

**起始版本：** 9

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RequestInfo](arkts-ability-dialogrequest-requestinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
