# LeakWatcherConfig

LeakWatcherConfig�������ͣ������а�����������ڴ�й©���Ŀ��������ԡ�

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.1.0.

<!--Device-jsLeakWatcher-interface LeakWatcherConfig--><!--Device-jsLeakWatcher-interface LeakWatcherConfig-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

## Modules to Import

```TypeScript
import { jsLeakWatcher } from 'kits/@kit.PerformanceAnalysisKit';
```

## bgLeakCountThreshold

```TypeScript
bgLeakCountThreshold?: int
```

Ӧ���ں�̨й©�����ﵽ�趨ֵ����dump��ȡֵ��ΧΪ[0, +��)��

GC/Dump�׶Σ����ڵ���1ʱ����Dump��

��ֵĬ��Ϊ1��

���벻��ȡֵ��Χ�ڵ�ֵʱ��ʹ��Ĭ��ֵ��

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.1.0.

<!--Device-LeakWatcherConfig-bgLeakCountThreshold?: int--><!--Device-LeakWatcherConfig-bgLeakCountThreshold?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

## checkInterval

```TypeScript
checkInterval?: int
```

ÿ��й©�����ʱ�䣬��λ��ms��ȡֵ��ΧΪ[90000, +��)��

Ĭ��Ϊ90000ms��

���Ӧ��������Զ�������ʱ��С��Ĭ��ֵ��JSLeakWatcherǿ�ƽ��������ΪĬ��ֵ��

��ǰjsLeakWatcherй©������ܿ����ϴ󣬻ᵼ��Ӧ�ÿ��٣���������ò��������ٿ���Ƶ�ʡ�

���벻��ȡֵ��Χ�ڵ�ֵʱ��ʹ��Ĭ��ֵ��

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.1.0.

<!--Device-LeakWatcherConfig-checkInterval?: int--><!--Device-LeakWatcherConfig-checkInterval?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

## dumpHeapWaitTimeMs

```TypeScript
dumpHeapWaitTimeMs?: int
```

�ӳ�ִ��dump����֤GC�ܵ�����ִ������ִ��dump���ӳټ��С�ڵ���й©�����ʱ�䣬��λ��ms��ȡֵ��ΧΪ[0, +��)��

�����ӳ�ʱ������й©���ʱ����Ĭ����й©���ʱ������һ�¡�

��������й©���󽫲��ᴥ��dump��

GC������Ĭ���ӳ�5��ִ��dump��

���벻��ȡֵ��Χ�ڵ�ֵʱ��ʹ��Ĭ��ֵ��

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.1.0.

<!--Device-LeakWatcherConfig-dumpHeapWaitTimeMs?: int--><!--Device-LeakWatcherConfig-dumpHeapWaitTimeMs?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

## exclusionList

```TypeScript
exclusionList?: Array<string>
```

���˲�����Ķ���������

������Window��CustomComponent��Ability���������Ӱ������������͵Ĺ��ˡ�

���ڻ�������ʱ�޷����й��ˣ�ֻ�ڿ���̬��Ч��

�������ͻ���ȼ���ID�б� > ��������

Ĭ��Ϊ�����顣

**Type:** Array&lt;string&gt;

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.1.0.

<!--Device-LeakWatcherConfig-exclusionList?: Array<string>--><!--Device-LeakWatcherConfig-exclusionList?: Array<string>-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

## fgLeakCountThreshold

```TypeScript
fgLeakCountThreshold?: int
```

Ӧ����ǰ̨й©�����ﵽ�趨ֵ����dump��ȡֵ��ΧΪ[0, +��)��

GC/Dump�׶Σ����ڵ���5ʱ����Dump��

��ֵĬ��Ϊ5��

���벻��ȡֵ��Χ�ڵ�ֵʱ��ʹ��Ĭ��ֵ��

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.1.0.

<!--Device-LeakWatcherConfig-fgLeakCountThreshold?: int--><!--Device-LeakWatcherConfig-fgLeakCountThreshold?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

## maxStoredHeapDumps

```TypeScript
maxStoredHeapDumps?: int
```

���dump���������ȡֵ��ΧΪ(0, 10]��������̿ռ�ռ����������ɾ��ʱ�����С��rawheap��jsleaklist�ļ���

Ĭ�ϱ���10��rawheap��10��jsleaklist�ļ���

���벻��ȡֵ��Χ�ڵ�ֵʱ��ʹ��Ĭ��ֵ��

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.1.0.

<!--Device-LeakWatcherConfig-maxStoredHeapDumps?: int--><!--Device-LeakWatcherConfig-maxStoredHeapDumps?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

## monitorObjectTypes

```TypeScript
monitorObjectTypes: MonitorObjectType
```

�����������͡�

Ĭ�ϼ������������͡�

**Type:** [MonitorObjectType](arkts-performanceanalysis-jsleakwatcher-monitorobjecttype-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.1.0.

<!--Device-LeakWatcherConfig-monitorObjectTypes: MonitorObjectType--><!--Device-LeakWatcherConfig-monitorObjectTypes: MonitorObjectType-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

## objectUniqueIDs

```TypeScript
objectUniqueIDs?: Array<int>
```

�����й©����ID�б���

ֻ�������Զ������������Ӱ������������͵ļ�⡣

���磺�����������õĶ�������ID���Զ���ID�б�������ֵͬʱ����Ч�Զ���ID�б�������

Ĭ��Ϊ�����顣

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.1.0.

<!--Device-LeakWatcherConfig-objectUniqueIDs?: Array<int>--><!--Device-LeakWatcherConfig-objectUniqueIDs?: Array<int>-End-->

**System capability:** SystemCapability.HiviewDFX.HiChecker

