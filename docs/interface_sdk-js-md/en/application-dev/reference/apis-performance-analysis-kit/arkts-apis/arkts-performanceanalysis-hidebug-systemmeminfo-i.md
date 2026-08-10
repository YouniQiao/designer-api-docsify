# SystemMemInfo

����ϵͳ�ڴ���Ϣ���������ڴ桢�����ڴ�Ϳ����ڴ档

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-hidebug-interface SystemMemInfo--><!--Device-hidebug-interface SystemMemInfo-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## availableMem

```TypeScript
availableMem: bigint
```

ϵͳ���õ��ڴ棬��KBΪ��λ�����㷽ʽ��/proc/meminfo: MemAvailable��

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SystemMemInfo-availableMem: bigint--><!--Device-SystemMemInfo-availableMem: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## freeMem

```TypeScript
freeMem: bigint
```

ϵͳ���е��ڴ棬��KBΪ��λ�����㷽ʽ��/proc/meminfo: MemFree��

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SystemMemInfo-freeMem: bigint--><!--Device-SystemMemInfo-freeMem: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## totalMem

```TypeScript
totalMem: bigint
```

ϵͳ�ܵ��ڴ棬��KBΪ��λ�����㷽ʽ��/proc/meminfo: MemTotal��

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SystemMemInfo-totalMem: bigint--><!--Device-SystemMemInfo-totalMem: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

