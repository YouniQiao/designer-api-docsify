# addPortAuthorization（系统接口）

## 导入模块

```TypeScript
import { serial } from 'kits/@kit.BasicServicesKit';
```

## addPortAuthorization

```TypeScript
function addPortAuthorization(tokenId: string, deviceId: string): Promise<void>
```

添加应用访问串口的权限。此函数通过将应用的Token ID与串口设备ID关联，建立应用的串口访问权限关系。适用于系统管理类应用为第三方应用授予串口访问权限的场景，如设备管理工具为工业数据采集应用分配串口权限。 仅用于会弹出串口授权弹窗的系统应用，在用户授权后，权限信息将持久化存储。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BusManager.Serial

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenId | string | 是 |
| deviceId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [35700001](../errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700002](../errorcode-busmanager-serial.md#35700002-参数错误) |
| [35700008](../errorcode-busmanager-serial.md#35700008-权限被拒绝) |
