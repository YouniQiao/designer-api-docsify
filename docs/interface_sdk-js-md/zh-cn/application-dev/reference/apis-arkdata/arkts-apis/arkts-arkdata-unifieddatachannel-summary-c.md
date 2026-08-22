# Summary

描述统一数据对象的数据摘要，包括数据类型和大小。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unifiedDataChannel-class Summary--><!--Device-unifiedDataChannel-class Summary-End-->

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

## 导入模块

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

**示例**

ArkTS-Dyn示例：

```TypeScript
function parseSummary(summary: unifiedDataChannel.Summary) {
  let summaryRecord = summary.summary as Record<string, number>;
  if (summaryRecord) {
    for (let item of Object.entries(summaryRecord)) {
      if (item && item.length <= 1) {
        continue;
      }
      let summaryStr: string = String(item[1]);
      let info: string[] = summaryStr.split(",");
      if (info.length <= 1) {
        continue;
      }
      let key: string = info[0];
      let value: string = info[1];
    }
  }
  let overviewRecord = summary.overview as Record<string, number>;
  let totalSize = summary.totalSize;
}
```

ArkTS-Sta示例：

```TypeScript
function parseSummary(summary: unifiedDataChannel.Summary) {
  console.info(`summary : ${JSON.stringify(summary.summary)}`);
  console.info(`totalSize: ${summary.totalSize}`);
  console.info(`overview : ${JSON.stringify(summary.overview)}`);
}
```

