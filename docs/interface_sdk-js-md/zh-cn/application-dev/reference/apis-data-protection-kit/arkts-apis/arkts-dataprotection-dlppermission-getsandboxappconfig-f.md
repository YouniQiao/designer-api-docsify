# getSandboxAppConfig

## 导入模块

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## getSandboxAppConfig

```TypeScript
function getSandboxAppConfig(): Promise<string>
```

获取沙箱应用配置信息，使用Promise异步回调。该接口用于获取沙箱应用的配置信息，便于读取或验证当前的配置状态。

**起始版本：** 11

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |
| [19100018](../errorcode-dlp.md#19100018-应用未授权) |
