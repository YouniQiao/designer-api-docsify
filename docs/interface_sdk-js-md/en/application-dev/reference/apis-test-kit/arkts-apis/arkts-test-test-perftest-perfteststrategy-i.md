# PerfTestStrategy

性能测试执行策略。

> **说明：**
> 
> 属性actionCode和resetCode的入参类型为回调函数"Callback\&lt;boolean&gt;"。在代码段中需要主动调用此回调函数，通知框架代码段执行完成，否则会导致代码段执行超时。
> > 其中，回调函数的参数为boolean类型，true代表代码段执行符合预期，false代表代码段执行不符合预期。[代码示例](arkts-test-test-perftest-perftest-c.md#create)。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface PerfTestStrategy--><!--Device-unnamed-declare interface PerfTestStrategy-End-->

**System capability:** SystemCapability.Test.PerfTest

## Modules to Import

```TypeScript
import { PerfTestStrategy, PerfMetric, PerfTest, PerfMeasureResult } from 'kits/@kit.TestKit';
```

## actionCode

```TypeScript
actionCode: Callback<Callback<boolean>>
```

测试代码段。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Callback&lt;boolean&gt;&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfTestStrategy-actionCode: Callback<Callback<boolean>>--><!--Device-PerfTestStrategy-actionCode: Callback<Callback<boolean>>-End-->

**System capability:** SystemCapability.Test.PerfTest

## bundleName

```TypeScript
bundleName?: string
```

被测应用包名。默认为""，框架运行时测试当前测试应用的性能数据。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfTestStrategy-bundleName?: string--><!--Device-PerfTestStrategy-bundleName?: string-End-->

**System capability:** SystemCapability.Test.PerfTest

## iterations

```TypeScript
iterations?: int
```

测试迭代执行次数，取值范围为大于0的整数，默认值为5。超出范围时抛出异常。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfTestStrategy-iterations?: int--><!--Device-PerfTestStrategy-iterations?: int-End-->

**System capability:** SystemCapability.Test.PerfTest

## metrics

```TypeScript
metrics: Array<PerfMetric>
```

被测性能指标列表，列表为空则不采集任何性能指标数据。

**Type:** Array&lt;PerfMetric&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfTestStrategy-metrics: Array<PerfMetric>--><!--Device-PerfTestStrategy-metrics: Array<PerfMetric>-End-->

**System capability:** SystemCapability.Test.PerfTest

## resetCode

```TypeScript
resetCode?: Callback<Callback<boolean>>
```

测试结束环境重置代码段。默认为空，框架运行时不执行此代码段。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Callback&lt;boolean&gt;&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfTestStrategy-resetCode?: Callback<Callback<boolean>>--><!--Device-PerfTestStrategy-resetCode?: Callback<Callback<boolean>>-End-->

**System capability:** SystemCapability.Test.PerfTest

## timeout

```TypeScript
timeout?: int
```

单次代码段（actionCode/resetCode）执行的超时时间，取值范围为大于0的整数，单位：ms，默认值为10000ms。当测试代码段执行耗时较长时，可适当增大此值以避免超时，超时后将触发异常，并终止测试执行。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PerfTestStrategy-timeout?: int--><!--Device-PerfTestStrategy-timeout?: int-End-->

**System capability:** SystemCapability.Test.PerfTest

