# getAppNativeMemInfoWithCache

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getAppNativeMemInfoWithCache

```TypeScript
function getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo
```

��ȡӦ�ý����ڴ���Ϣ����`getAppNativeMemInfo`�ӿ���ȣ��ýӿ�ʹ���˻�����ƣ���������ܡ��������Ч��Ϊ5���ӡ�

> **ע��**
> 
> ���ڶ�ȡ /proc/{pid}/smaps_rollup �ȽϺ�ʱ�����鲻�����߳���ʹ�øýӿڡ�����ͨ��@ohos.taskpool��@ohos.worker�����첽�̣߳��Ա���Ӧ�ÿ��١�

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-hidebug-function getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo--><!--Device-hidebug-function getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| forceRefresh | boolean | No | �Ƿ���Ҫ���ӻ�����Ч�ԣ�ǿ�Ƹ��»���ֵ��Ĭ��ֵ��false�� true��ֱ�ӻ�ȡ��ǰ�ڴ����ݲ����»���ֵ�� false��������Чʱ��ֱ�ӷ��ػ���ֵ������ʧЧʱ��ȡ��ǰ�ڴ����ݲ����»���ֵ�� |

**Return value:**

| Type | Description |
| --- | --- |
| [NativeMemInfo](arkts-performanceanalysis-hidebug-nativememinfo-i.md) | Ӧ�ý����ڴ���Ϣ�� |

## Examples

```TypeScript
let nativeMemInfo: hidebug.NativeMemInfo = hidebug.getAppNativeMemInfoWithCache();
console.info(`pss: ${nativeMemInfo.pss}, vss: ${nativeMemInfo.vss}, rss: ${nativeMemInfo.rss}, ` +
  `sharedDirty: ${nativeMemInfo.sharedDirty}, privateDirty: ${nativeMemInfo.privateDirty}, ` +
  `sharedClean: ${nativeMemInfo.sharedClean}, privateClean: ${nativeMemInfo.privateClean}`);
```

