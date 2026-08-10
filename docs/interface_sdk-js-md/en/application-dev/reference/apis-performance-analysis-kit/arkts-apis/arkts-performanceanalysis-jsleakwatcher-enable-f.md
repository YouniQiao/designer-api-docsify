# enable

## Modules to Import

```TypeScript
import { jsLeakWatcher } from 'kits/@kit.PerformanceAnalysisKit';
```

## enable

```TypeScript
function enable(isEnable: boolean): void
```

ʹ��ArkTS����й©��⣬Ĭ�Ϲرա���������ռ�й©��Ϣ�������������ܿ�����

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 26.1.0.

<!--Device-jsLeakWatcher-function enable(isEnable: boolean): void--><!--Device-jsLeakWatcher-function enable(isEnable: boolean): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnable | boolean | Yes | �Ƿ�ʹ��jsLeakWatcher��true��ʹ��jsLeakWatcher��false����ʹ��jsLeakWatcher�� |

## Examples

```TypeScript
jsLeakWatcher.enable(true);
```

