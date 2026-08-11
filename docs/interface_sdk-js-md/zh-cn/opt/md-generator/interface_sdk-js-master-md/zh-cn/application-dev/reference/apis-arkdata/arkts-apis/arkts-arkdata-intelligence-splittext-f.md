# splitText

## splitText

```TypeScript
function splitText(text: string, config: SplitConfig): Promise<Array<string>>
```

获取文本的分块。使用Promise异步回调。

**起始版本：** 15

<!--Device-intelligence-function splitText(text: string, config: SplitConfig): Promise<Array<string>>--><!--Device-intelligence-function splitText(text: string, config: SplitConfig): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| config | [SplitConfig](arkts-arkdata-intelligence-splitconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31300000](../errorcode-intelligence.md#31300000-服务内部异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let splitConfig: intelligence.SplitConfig = {
  size: 10,
  overlapRatio: 0.1
}
let textToSplit = 'text';

intelligence.splitText(textToSplit, splitConfig)
  .then((data: Array<string>) => {
    console.info("Succeeded in splitting Text");
  })
  .catch((err: BusinessError) => {
    console.error(`Failed to split Text. Code: ${err.code}, message: ${err.message}`);
  })
```
