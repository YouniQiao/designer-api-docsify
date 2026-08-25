# enable

## 导入模块

```TypeScript
import { jsLeakWatcher } from '@kit.PerformanceAnalysisKit';
```

## enable

```TypeScript
function enable(isEnable: boolean): void
```

使能ArkTS对象泄漏检测，默认关闭。开启后会收集泄漏信息，可能增加性能开销。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为26.1.0。

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnable | boolean | 是 |

**示例**

```TypeScript
jsLeakWatcher.enable(true);
```
