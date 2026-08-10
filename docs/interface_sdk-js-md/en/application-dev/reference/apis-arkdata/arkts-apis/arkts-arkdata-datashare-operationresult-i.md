# OperationResult

订阅/取消订阅数据变更和发布数据的操作结果。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-dataShare-interface OperationResult--><!--Device-dataShare-interface OperationResult-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## key

```TypeScript
key: string
```

指定运算结果的键。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OperationResult-key: string--><!--Device-OperationResult-key: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## result

```TypeScript
result: int
```

指定运算结果。正常情况下返回0，异常情况下返回错误码。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OperationResult-result: int--><!--Device-OperationResult-result: int-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

