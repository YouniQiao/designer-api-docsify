# Summary

Summarizes the data information of the **unifiedData** object, including the data type and size.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unifiedDataChannel-class Summary--><!--Device-unifiedDataChannel-class Summary-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

**Examples**

```TypeScript
function parseSummary(summary : unifiedDataChannel.Summary) {
  let summaryRecord = summary.summary as Record<string, number>;
  if (summaryRecord) {
    for (let item of Object.entries(summaryRecord)) {
      if (item && item.length <= 1) {
        continue;
      }
      let summaryStr : string = String(item[1]);
      let info : string[] = summaryStr.split(",");
      if (info.length <= 1) {
        continue;
      }
      let key : string = info[0];
      let value : string = info[1];
    }
  }
  let overviewRecord = summary.overview as Record<string, number>;
  let totalSize = summary.totalSize;
}
```

