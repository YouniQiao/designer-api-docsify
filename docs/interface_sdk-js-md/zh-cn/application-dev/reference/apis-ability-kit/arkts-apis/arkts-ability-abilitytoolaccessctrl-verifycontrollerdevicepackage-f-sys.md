# verifyControllerDevicePackage（系统接口）

## 导入模块

```TypeScript
```

## verifyControllerDevicePackage

```TypeScript
export function verifyControllerDevicePackage(ticketInfo: RemoteAuthPackage[], remoteInfo: RemoteInfo):
    Promise<boolean[]>
```

验证来自控制器设备的授权包。 验证控制器设备发送的远程授权包。 它验证票证和远程设备信息，以确保授权是合法的。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.QUERY_TOOL_PERMISSIONS

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| ticketInfo | [RemoteAuthPackage](arkts-ability-abilitytoolaccessctrl-remoteauthpackage-i-sys.md)[] | 是 |
| remoteInfo | [RemoteInfo](arkts-ability-abilitytoolaccessctrl-remoteinfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [24010000](../errorcode-abilityToolAccessCtrl-sys.md#24010000-入参错误) |
| [24010001](../errorcode-abilityToolAccessCtrl-sys.md#24010001-系统服务工作异常) |
| [24010002](../errorcode-abilityToolAccessCtrl-sys.md#24010002-服务内部错误) |
| [24010003](../errorcode-abilityToolAccessCtrl-sys.md#24010003-环境错误) |
