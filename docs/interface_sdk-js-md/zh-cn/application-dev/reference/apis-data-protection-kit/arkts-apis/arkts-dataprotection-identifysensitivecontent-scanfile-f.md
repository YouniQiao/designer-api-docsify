# scanFile

## 导入模块

```TypeScript
import { identifySensitiveContent } from 'kits/@kit.DataProtectionKit';
```

## scanFile

```TypeScript
function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>
```

根据设置的策略，识别指定文件中的敏感内容，返回识别的结果数组，包含匹配的敏感标签、匹配内容及匹配数量。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.ENTERPRISE_DATA_IDENTIFY_FILE

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| identifyPolicies | Array & lt;Policy & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[MatchResult](arkts-dataprotection-identifysensitivecontent-matchresult-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [19110001](../errorcode-dlp.md#19110001-参数错误) |
| [19110002](../errorcode-dlp.md#19110002-文件敏感信息识别超时) |
| [19110003](../errorcode-dlp.md#19110003-文件不支持) |
| [19110004](../errorcode-dlp.md#19110004-系统功能运行异常) |
