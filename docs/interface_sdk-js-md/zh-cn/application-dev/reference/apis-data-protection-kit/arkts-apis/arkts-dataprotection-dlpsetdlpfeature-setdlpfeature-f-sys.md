# setDlpFeature（系统接口）

## 导入模块

```TypeScript
import { dlpSetDlpFeature } from 'kits/@kit.DataProtectionKit';
```

## setDlpFeature

```TypeScript
function setDlpFeature(status: DlpFeatureStatus): Promise<StatusInfoResult>
```

设置DLP特性开关状态。使用Promise异步回调。调用成功后，DLP特性开关将设置为指定状态，系统将根据该状态启用或禁用DLP保护功能。当特性开关处于开启状态时，右键单击支持加密的文件，右键菜单中会显示“加密保护”选项。可加密类型包括：.txt，.pdf，.xls，.xlsx，.ppt，.pptx，.doc，.docx。企业策略开启或关闭数据防泄漏功能时使用此接口。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DataLossPrevention

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| status | [DlpFeatureStatus](arkts-dataprotection-dlpsetdlpfeature-dlpfeaturestatus-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[StatusInfoResult](arkts-dataprotection-dlpsetdlpfeature-statusinforesult-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |
