# OperationResult (System API)

Defines the result of the operation for subscribing to or unsubscribing from the data changes or published data.

**Since:** 23

<!--Device-dataShare-interface OperationResult--><!--Device-dataShare-interface OperationResult-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dataShare } from '@kit.ArkData';
import { dataSharePredicates } from '@kit.ArkData';
```

## key

```TypeScript
key: string
```

Key of the operation result.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-OperationResult-key: string--><!--Device-OperationResult-key: string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

## result

```TypeScript
result: int
```

Operation result. If the operation is successful, **0** is returned; otherwise, an error code is returned.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-OperationResult-result: int--><!--Device-OperationResult-result: int-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

