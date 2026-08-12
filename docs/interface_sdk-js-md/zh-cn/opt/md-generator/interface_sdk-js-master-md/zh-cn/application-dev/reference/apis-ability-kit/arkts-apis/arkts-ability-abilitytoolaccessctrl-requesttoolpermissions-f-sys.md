# requestToolPermissions（系统接口）

## requestToolPermissions

```TypeScript
export function requestToolPermissions(permissionQuery: PermissionQuery): Promise<PermissionQueryResult>
```

根据指定的操作查询工具权限。该函数用于检查权限查询中指定的CLI命令或API的权限状态。对于每个操作，它返回权限状态、授权状态以及是否需要用户对话框。当needTicket设置为true时，远程授权会生成一个票据。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.QUERY_TOOL_PERMISSIONS

<!--Device-abilityToolAccessCtrl-export function requestToolPermissions(permissionQuery: PermissionQuery): Promise<PermissionQueryResult>--><!--Device-abilityToolAccessCtrl-export function requestToolPermissions(permissionQuery: PermissionQuery): Promise<PermissionQueryResult>-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| permissionQuery | [PermissionQuery](arkts-ability-abilitytoolaccessctrl-permissionquery-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PermissionQueryResult](arkts-ability-abilitytoolaccessctrl-permissionqueryresult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [24010006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-abilityToolAccessCtrl-sys.md#24010006-设备处于锁屏状态时不允许执行操作) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [24010002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-abilityToolAccessCtrl-sys.md#24010002-服务内部错误) |
| [24010003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-abilityToolAccessCtrl-sys.md#24010003-环境错误) |
| [24010000](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-abilityToolAccessCtrl-sys.md#24010000-入参错误) |
| [24010001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-abilityToolAccessCtrl-sys.md#24010001-系统服务工作异常) |

## 示例

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let permissionQuery: abilityToolAccessCtrl.PermissionQuery = {
  operationInfo: [{
    operationType: abilityToolAccessCtrl.OperationType.CLI,
    info: {
      cliCmdName: 'ohos-displayManager',
      subCliCmdName: 'set-brightness'
    }
  }],
  needTicket: true,
  ticketExpireTimeMs: 10000,
};
abilityToolAccessCtrl.requestToolPermissions(permissionQuery).then((data: abilityToolAccessCtrl.PermissionQueryResult) => {
  console.info('requestToolPermissions success, data: ' + JSON.stringify(data));
}).catch((err: BusinessError): void => {
  console.error(`requestToolPermissions fail, code: ${err.code}, message: ${err.message}`);
});
```
