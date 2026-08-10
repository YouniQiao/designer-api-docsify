# NativeMemInfo

����Ӧ�ý��̵��ڴ���Ϣ��

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-hidebug-interface NativeMemInfo--><!--Device-hidebug-interface NativeMemInfo-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## privateClean

```TypeScript
privateClean: bigint
```

˽�иɾ��ڴ��С����KBΪ��λ�����㷽ʽ��/proc/{pid}/smaps_rollup: Private_Clean��

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NativeMemInfo-privateClean: bigint--><!--Device-NativeMemInfo-privateClean: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## privateDirty

```TypeScript
privateDirty: bigint
```

˽�����ڴ��С����KBΪ��λ�����㷽ʽ��/proc/{pid}/smaps_rollup: Private_Dirty��

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NativeMemInfo-privateDirty: bigint--><!--Device-NativeMemInfo-privateDirty: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## pss

```TypeScript
pss: bigint
```

ʵ��ռ�õ������ڴ��С(�������乲����ռ�õ��ڴ�)����KBΪ��λ�����㷽ʽ��/proc/{pid}/smaps_rollup: Pss + SwapPss��

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NativeMemInfo-pss: bigint--><!--Device-NativeMemInfo-pss: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## rss

```TypeScript
rss: bigint
```

ʵ��ռ�õ������ڴ��С(����������ռ��)����KBΪ��λ�����㷽ʽ��/proc/{pid}/smaps_rollup: Rss��

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NativeMemInfo-rss: bigint--><!--Device-NativeMemInfo-rss: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## sharedClean

```TypeScript
sharedClean: bigint
```

�������ڴ��С����KBΪ��λ�����㷽ʽ��/proc/{pid}/smaps_rollup: Shared_Clean��

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NativeMemInfo-sharedClean: bigint--><!--Device-NativeMemInfo-sharedClean: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## sharedDirty

```TypeScript
sharedDirty: bigint
```

�������ڴ��С����KBΪ��λ�����㷽ʽ��/proc/{pid}/smaps_rollup: Shared_Dirty��

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NativeMemInfo-sharedDirty: bigint--><!--Device-NativeMemInfo-sharedDirty: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## vss

```TypeScript
vss: bigint
```

ռ�õ������ڴ��С(������������ռ�õ��ڴ�)����KBΪ��λ�����㷽ʽ��/proc/{pid}/statm: size * 4��

**Type:** bigint

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NativeMemInfo-vss: bigint--><!--Device-NativeMemInfo-vss: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

