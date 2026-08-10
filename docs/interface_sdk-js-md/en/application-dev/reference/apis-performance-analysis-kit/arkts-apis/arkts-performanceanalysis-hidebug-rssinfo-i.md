# RssInfo

����Ӧ�ý��̵������ڴ���Ϣ��

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-hidebug-interface RssInfo--><!--Device-hidebug-interface RssInfo-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## rss

```TypeScript
rss: bigint
```

ʵ��ռ�õ������ڴ��С��Resident Set Size������������ҳ���ļ�ӳ��ҳ�͹����ڴ�ҳ����KBΪ��λ�����㷽ʽ��/proc/{pid}/status: VmRss��

**Type:** bigint

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RssInfo-rss: bigint--><!--Device-RssInfo-rss: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## swapRss

```TypeScript
swapRss: bigint
```

��������������������˽��ҳ�ܴ�С����KBΪ��λ�����㷽ʽ��/proc/{pid}/status: VmSwap��

**Type:** bigint

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RssInfo-swapRss: bigint--><!--Device-RssInfo-swapRss: bigint-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

