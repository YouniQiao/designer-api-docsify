# getGwpAsanGrayscaleState

## getGwpAsanGrayscaleState

```TypeScript
function getGwpAsanGrayscaleState(): number
```

获取当前GWP-ASan剩余使能天数。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为22。

<!--Device-hidebug-function getGwpAsanGrayscaleState(): number--><!--Device-hidebug-function getGwpAsanGrayscaleState(): number-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取当前GWP-ASan剩余使能天数。若当前未使能，返回值0。 |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { taskpool } from '@kit.ArkTS';

@Concurrent
function getGwpAsanStateTask(): number {
  return hidebug.getGwpAsanGrayscaleState();
}
taskpool.execute(getGwpAsanStateTask).then((remainDays: Object) => {
  console.info(`GWP-ASan remain days: ${remainDays as number}.`);
})
```


## getGwpAsanGrayscaleState

```TypeScript
function getGwpAsanGrayscaleState(): int
```

获取当前GWP-ASan剩余使能天数。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-hidebug-function getGwpAsanGrayscaleState(): int--><!--Device-hidebug-function getGwpAsanGrayscaleState(): int-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 获取当前GWP-ASan剩余使能天数。若当前未使能，返回值0。 |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { taskpool } from '@kit.ArkTS';

@Concurrent
function getGwpAsanStateTask(): number {
  return hidebug.getGwpAsanGrayscaleState();
}
taskpool.execute(getGwpAsanStateTask).then((remainDays: Object) => {
  console.info(`GWP-ASan remain days: ${remainDays as number}.`);
})
```

