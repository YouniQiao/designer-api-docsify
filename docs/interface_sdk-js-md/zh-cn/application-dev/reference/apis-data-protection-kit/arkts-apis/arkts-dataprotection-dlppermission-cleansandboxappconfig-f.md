# cleanSandboxAppConfig

## 导入模块

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## cleanSandboxAppConfig

```TypeScript
function cleanSandboxAppConfig(): Promise<void>
```

清理沙箱应用配置信息。调用成功后，沙箱应用配置将被清除，恢复默认状态。使用Promise异步回调。该接口用于清理沙箱应用的配置信息，恢复默认状态以防止配置残留影响后续使用。仅支持在非DLP沙箱应用中调用。

**起始版本：** 11

**系统能力：** SystemCapability.Security.DataLossPrevention

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100007](../errorcode-dlp.md#19100007-dlp沙箱应用不允许调用此接口) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |
| [19100018](../errorcode-dlp.md#19100018-应用未授权) |
