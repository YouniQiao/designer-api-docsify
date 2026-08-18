# grantToolPermissionsByUser（系统接口）

## 导入模块

```TypeScript
```

## grantToolPermissionsByUser

```TypeScript
export function grantToolPermissionsByUser(userAuthResult: UserAuthResult[]): Promise<TicketInfo[]>
```

根据用户授权结果授予工具权限。 该功能根据用户的授权决定授予工具（CLI命令或API）的权限。 授权成功后，会生成工单，用于权限验证。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.MANAGE_TOOL_RUNTIME_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function grantToolPermissionsByUser(userAuthResult: UserAuthResult[]): Promise<TicketInfo[]>--><!--Device-abilityToolAccessCtrl-export function grantToolPermissionsByUser(userAuthResult: UserAuthResult[]): Promise<TicketInfo[]>-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userAuthResult | [UserAuthResult[]](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-userauthresult-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[TicketInfo](arkts-ability-abilitytoolaccessctrl-ticketinfo-i-sys.md)[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [24010004](../errorcode-abilityToolAccessCtrl-sys.md#24010004-权限不存在) |
| [24010005](../errorcode-abilityToolAccessCtrl-sys.md#24010005-授权失败) |
| [24010002](../errorcode-abilityToolAccessCtrl-sys.md#24010002-服务内部错误) |
| [24010003](../errorcode-abilityToolAccessCtrl-sys.md#24010003-环境错误) |
| [24010000](../errorcode-abilityToolAccessCtrl-sys.md#24010000-入参错误) |
| [24010001](../errorcode-abilityToolAccessCtrl-sys.md#24010001-系统服务工作异常) |

**示例**

```TypeScript
import { abilityToolAccessCtrl, abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userAuthResult: Array<abilityToolAccessCtrl.UserAuthResult> = [{
  permissionInfo: [{
    permission: 'ohos.permission.cli.BUNDLE_ACTIVE_INFO' as Permissions,
    permissionStatus: abilityAccessCtrl.PermissionStatus.GRANTED
  }],
  permissionQuery: {
    operationInfo: [{
      operationType: abilityToolAccessCtrl.OperationType.CLI,
      info: 'ohos.permission.cli.BUNDLE_ACTIVE_INFO'
    }],
    needTicket: true
  }
}];
abilityToolAccessCtrl.grantToolPermissionsByUser(userAuthResult).then((data: Array<abilityToolAccessCtrl.TicketInfo>) => {
  console.info('grantToolPermissionsByUser success, data: ' + JSON.stringify(data));
}).catch((err: BusinessError): void => {
  console.error(`grantToolPermissionsByUser fail, code: ${err.code}, message: ${err.message}`);
});
```
