# MultithreadingDetectionOptions

多线程检测功能参数配置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-util-interface MultithreadingDetectionOptions--><!--Device-util-interface MultithreadingDetectionOptions-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## abort

```TypeScript
abort?: boolean
```

若 abort 为 **true**，应用将崩溃；若 abort 为 **false**，应用将不崩溃。默认值为 **true**。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultithreadingDetectionOptions-abort?: boolean--><!--Device-MultithreadingDetectionOptions-abort?: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## frequency

```TypeScript
frequency?: number
```

多线程检测的采样频率。该值必须为整数，最小为 **100**，最大为 **2147483647**（默认 **100**）。该值应为整数。

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultithreadingDetectionOptions-frequency?: number--><!--Device-MultithreadingDetectionOptions-frequency?: number-End-->

**System capability:** SystemCapability.Utils.Lang

## interval

```TypeScript
interval?: number
```

多线程检测的时间间隔（分钟）。只有距离上次检测的时间超过此间隔时才会再次上报错误。该值必须为 [0,1440] 范围内的整数（默认 5min）。

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultithreadingDetectionOptions-interval?: number--><!--Device-MultithreadingDetectionOptions-interval?: number-End-->

**System capability:** SystemCapability.Utils.Lang

