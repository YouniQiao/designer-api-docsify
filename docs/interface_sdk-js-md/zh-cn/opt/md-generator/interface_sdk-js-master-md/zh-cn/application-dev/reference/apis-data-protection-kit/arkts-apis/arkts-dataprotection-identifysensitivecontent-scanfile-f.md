# scanFile

## scanFile

```TypeScript
function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>
```

根据设置的策略，识别指定文件中的敏感内容，返回识别的结果数组，包含匹配的敏感标签、匹配内容及匹配数量。使用Promise异步回调。

**起始版本：** 21

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_DATA_IDENTIFY_FILE

<!--Device-identifySensitiveContent-function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>--><!--Device-identifySensitiveContent-function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>-End-->

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
| [19110003](../errorcode-dlp.md#19110003-文件不支持) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [19110002](../errorcode-dlp.md#19110002-文件敏感信息识别超时) |
| [19110001](../errorcode-dlp.md#19110001-参数错误) |
| [19110004](../errorcode-dlp.md#19110004-系统功能运行异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { identifySensitiveContent } from '@kit.DataProtectionKit';

// 定义待扫描的文件物理路径
let filePath = "/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt";

// 配置敏感内容识别策略
let policies: Array<identifySensitiveContent.Policy> = [
  {"sensitiveLabel":"name", "keywords":["姓名"], "regex":""},
  {"sensitiveLabel":"phone", "keywords":[], "regex":"电话"},
  {"sensitiveLabel":"address", "keywords":["地址"], "regex":"xx省xx市"}
];
try {
  identifySensitiveContent.scanFile(filePath, policies).then(records => {
    console.info('scanFile finish');
    for (let i = 0; i < records.length; ++i) {
      const sensitiveLabel = records[i].sensitiveLabel;
      const matchContent = records[i].matchContent;
      const matchNumber = records[i].matchNumber;
      console.info(`scanFile result sensitiveLabel: ${sensitiveLabel} matchNumber ${matchNumber} matchContent ${matchContent}`);
    }
  }).catch((err: BusinessError) => {
    // 处理识别失败
    console.error(`Failed to scanFile. Code:${err.code}, message:${err.message}`);
  })
} catch (err) {
  console.error('error message', err.message);
}
```
