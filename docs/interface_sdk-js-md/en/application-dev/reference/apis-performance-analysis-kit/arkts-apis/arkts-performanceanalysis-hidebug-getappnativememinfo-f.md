# getAppNativeMemInfo

## getAppNativeMemInfo

```TypeScript
function getAppNativeMemInfo(): NativeMemInfo
```

Obtains the memory information of the application process. This API is implemented by reading data from the  
**\/proc/{pid}/smaps\_rollup and /proc/{pid}/statm** node.
    **NOTE**  
    
    Reading the **\/proc/{pid}/smaps\_rollup** node takes a long time. You are advised to use the asynchronous API  
    [hidebug.getAppNativeMemInfoAsync]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to avoid frame loss or frame freezing.  
    
    You are advised to use the [hidebug.getRssInfo]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API to obtain the RSS information of an  
    application.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-hidebug-function getAppNativeMemInfo(): NativeMemInfo--><!--Device-hidebug-function getAppNativeMemInfo(): NativeMemInfo-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Memory information of the application process. |

**Example**

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let nativeMemInfo: hidebug.NativeMemInfo = hidebug.getAppNativeMemInfo();
console.info(`pss: ${nativeMemInfo.pss}, vss: ${nativeMemInfo.vss}, rss: ${nativeMemInfo.rss}, ` +
  `sharedDirty: ${nativeMemInfo.sharedDirty}, privateDirty: ${nativeMemInfo.privateDirty}, ` +
  `sharedClean: ${nativeMemInfo.sharedClean}, privateClean: ${nativeMemInfo.privateClean}`);
```

