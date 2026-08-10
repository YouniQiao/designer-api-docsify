# getAppNativeMemInfo

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getAppNativeMemInfo

```TypeScript
function getAppNativeMemInfo(): NativeMemInfo
```

��ȡӦ�ý����ڴ���Ϣ����ȡ/proc/{pid}/smaps_rollup��/proc/{pid}/statm�ڵ�����ݡ�

> **ע��**
> 
> ���ڶ�ȡ/proc/{pid}/smaps_rollup��ʱ�ϳ����Ƽ�ʹ���첽�ӿ�hidebug.getAppNativeMemInfoAsync���Ա���Ӧ�ö�֡�򿨶١�
> 
> �Ƽ�ʹ��hidebug.getRssInfo�ӿڻ�ȡӦ�õ�rssʹ����Ϣ��

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-hidebug-function getAppNativeMemInfo(): NativeMemInfo--><!--Device-hidebug-function getAppNativeMemInfo(): NativeMemInfo-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| [NativeMemInfo](arkts-performanceanalysis-hidebug-nativememinfo-i.md) | Ӧ�ý����ڴ���Ϣ�� |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeMemInfo: hidebug.NativeMemInfo = hidebug.getAppNativeMemInfo();
console.info(`pss: ${nativeMemInfo.pss}, vss: ${nativeMemInfo.vss}, rss: ${nativeMemInfo.rss}, ` +
  `sharedDirty: ${nativeMemInfo.sharedDirty}, privateDirty: ${nativeMemInfo.privateDirty}, ` +
  `sharedClean: ${nativeMemInfo.sharedClean}, privateClean: ${nativeMemInfo.privateClean}`);
```

