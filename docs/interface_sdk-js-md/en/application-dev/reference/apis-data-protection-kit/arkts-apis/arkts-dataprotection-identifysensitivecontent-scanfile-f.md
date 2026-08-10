# scanFile

## Modules to Import

```TypeScript
import { identifySensitiveContent } from 'kits/@kit.DataProtectionKit';
```

## scanFile

```TypeScript
function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>
```

根据设置的策略，识别指定文件中的敏感内容，返回识别的结果数组，包含匹配的敏感标签、匹配内容及匹配数量。使用Promise异步回调。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Required permissions:** ohos.permission.ENTERPRISE_DATA_IDENTIFY_FILE

<!--Device-identifySensitiveContent-function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>--><!--Device-identifySensitiveContent-function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filePath | string | Yes | 识别的文件路径，需使用物理路径，路径指向的文件必须存在且支持访问。 |
| identifyPolicies | Array&lt;Policy&gt; | Yes | 用于识别敏感内容的策略数组。每个Policy定义识别规则（标签、关键字、正则表达式），系统将根据这些规则扫描文件内容并返回匹配结果。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;MatchResult&gt;&gt; | Promise对象，返回敏感内容识别的结果。成功时返回匹配结果数组，异常返回错误码。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 19110003 | The file is not supported. Possible causes: 1. The file path does not exist. 2. The file type is not supported. 3. The file permission is not supported. |
| 801 | Capability not supported. |
| 19110002 | Sensitive file content identification timed out. |
| 19110001 | Parameter error. Possible causes: 1. Incorrect policy format. 2. Invalid parameter range. |
| 19110004 | A system error has occurred. |
| 201 | permission denied. |

## Examples

```TypeScript
import { identifySensitiveContent } from '@kit.DataProtectionKit';

// Define the physical file path to be scanned.
let filePath = "/data/service/el2/100/hmdfs/account/files/Docs/Documents/test.txt";

// Configure the policy for sensitive content identification.
let policies: Array<identifySensitiveContent.Policy> = [
  {"sensitiveLabel":"name", "keywords":["name"], "regex":""},
  {"sensitiveLabel":"phone", "keywords":[], "regex":"phone"},
  {"sensitiveLabel":"address", "keywords":["address"], "regex":"xx City, xx Province"}
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
    // Identification fails.
    console.error(`Failed to scanFile. Code:${err.code}, message:${err.message}`);
  })
} catch (err) {
  console.error('error message', err.message);
}
```

