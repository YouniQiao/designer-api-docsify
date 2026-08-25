# startDLPManagerForResult

## 导入模块

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## startDLPManagerForResult

```TypeScript
function startDLPManagerForResult(context: common.UIAbilityContext, want: Want): Promise<DLPManagerResult>
```

在当前[UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md)界面以无边框形式打开DLP权限管理应用。使用Promise异步回调。该接口用于拉起DLP权限管理应用配置文件权限，并将用户操作结果返回给调用方。

> **说明：**&gt;
> 该接口仅支持域账号调用。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | common.UIAbilityContext | 是 |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DLPManagerResult](arkts-dataprotection-dlppermission-dlpmanagerresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |
| [19100016](../errorcode-dlp.md#19100016-want参数中没有uri) |
| [19100017](../errorcode-dlp.md#19100017-want参数中parameters内没有displayname) |
