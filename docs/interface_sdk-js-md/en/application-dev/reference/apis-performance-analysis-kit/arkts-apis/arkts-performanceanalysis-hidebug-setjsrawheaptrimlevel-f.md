# setJsRawHeapTrimLevel

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## setJsRawHeapTrimLevel

```TypeScript
function setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void
```

���õ�ǰ����ת�������ԭʼ�ѿ��յĲü�����ʹ�øýӿڲ��������TRIM_LEVEL_2��������Ч���ٶѿ��յ��ļ���С��

> **ע��**
> 
> Ĭ�ϲü�������TRIM_LEVEL_1�����������TRIM_LEVEL_2�ü�����ʹ��API version 20֮���rawheap-translator���߲��ܽ�.rawheap�ļ�ת��Ϊ.heapsnapshot�ļ���������ܵ���ת��ʧ�ܡ�
> 
> �ýӿ�Ӱ��dumpJsRawHeapData�Ľ����

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 26.1.0.

<!--Device-hidebug-function setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void--><!--Device-hidebug-function setJsRawHeapTrimLevel(level: JsRawHeapTrimLevel): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | [JsRawHeapTrimLevel](arkts-performanceanalysis-hidebug-jsrawheaptrimlevel-e.md) | Yes | ת���ѿ��յĲü�����Ĭ��ΪTRIM_LEVEL_1�� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

hidebug.setJsRawHeapTrimLevel(hidebug.JsRawHeapTrimLevel.TRIM_LEVEL_2);
```

