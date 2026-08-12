# scanFile

## Modules to Import

```TypeScript
import { identifySensitiveContent } from '@kit.DataProtectionKit';
```

## scanFile

```TypeScript
function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>
```

Identifies sensitive content in a specified file based on the configured policy and returns the identified result array,including the matched sensitivity labels, matched content, and number of matched items. This API uses a promise to return the result.

**Since:** 21

**Required permissions:** ohos.permission.ENTERPRISE_DATA_IDENTIFY_FILE

<!--Device-identifySensitiveContent-function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>--><!--Device-identifySensitiveContent-function scanFile(filePath: string, identifyPolicies: Array<Policy>): Promise<Array<MatchResult>>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filePath | string | Yes |
| identifyPolicies | Array & lt;Policy & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[MatchResult](arkts-dataprotection-identifysensitivecontent-matchresult-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19110003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19110003-file-not-supported) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19110002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19110002-file-sensitive-content-identification-timed-out) |
| [19110001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19110001-invalid-parameter) |
| [19110004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-data-protection-kit/errorcode-dlp.md#19110004-system-function-abnormal) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

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
