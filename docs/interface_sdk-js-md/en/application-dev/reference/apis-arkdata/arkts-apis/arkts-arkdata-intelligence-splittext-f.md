# splitText

## Modules to Import

```TypeScript
import { intelligence } from 'kits/@kit.ArkData';
```

## splitText

```TypeScript
function splitText(text: string, config: SplitConfig): Promise<Array<string>>
```

获取文本的分块。使用Promise异步回调。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-intelligence-function splitText(text: string, config: SplitConfig): Promise<Array<string>>--><!--Device-intelligence-function splitText(text: string, config: SplitConfig): Promise<Array<string>>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 待分块的文本。单个文本长度上限为100000个字符。超出长度时抛出异常。 |
| config | [SplitConfig](arkts-arkdata-intelligence-splitconfig-i.md) | Yes | 文本分块的配置信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise对象，返回分块结果的数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let splitConfig: intelligence.SplitConfig = {
  size: 10,
  overlapRatio: 0.1
}
let splitText = 'text';

intelligence.splitText(splitText, splitConfig)
  .then((data: Array<string>) => {
    console.info("Succeeded in splitting Text");
  })
  .catch((err: BusinessError) => {
    console.error("Failed to split Text and code is " + err.code);
  })
```

