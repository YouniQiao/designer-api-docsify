# getAppNativeMemInfoAsync

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getAppNativeMemInfoAsync

```TypeScript
function getAppNativeMemInfoAsync(): Promise<NativeMemInfo>
```

��ȡ/proc/{pid}/smaps_rollup��/proc/{pid}/statm�ڵ�������Ի�ȡӦ�ý����ڴ���Ϣ��ʹ��Promise�첽�ص���

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-hidebug-function getAppNativeMemInfoAsync(): Promise<NativeMemInfo>--><!--Device-hidebug-function getAppNativeMemInfoAsync(): Promise<NativeMemInfo>-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;NativeMemInfo&gt; | promise���󣬷���Ӧ�ý����ڴ���Ϣ�� |

## Examples

```TypeScript
hidebug.getAppNativeMemInfoAsync().then((nativeMemInfo: hidebug.NativeMemInfo)=>{
  console.info(`pss: ${nativeMemInfo.pss}, vss: ${nativeMemInfo.vss}, rss: ${nativeMemInfo.rss}, ` +
    `sharedDirty: ${nativeMemInfo.sharedDirty}, privateDirty: ${nativeMemInfo.privateDirty}, ` +
    `sharedClean: ${nativeMemInfo.sharedClean}, privateClean: ${nativeMemInfo.privateClean}`);
});
```

