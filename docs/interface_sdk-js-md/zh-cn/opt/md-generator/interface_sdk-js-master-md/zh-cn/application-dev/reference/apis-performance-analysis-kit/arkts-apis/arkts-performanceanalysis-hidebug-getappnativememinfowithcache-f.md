# getAppNativeMemInfoWithCache

## getAppNativeMemInfoWithCache

```TypeScript
function getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo
```

��ȡӦ�ý����ڴ���Ϣ����`getAppNativeMemInfo`�ӿ���ȣ��ýӿ�ʹ���˻�����ƣ���������ܡ��������Ч��Ϊ5���ӡ�

> **ע��**
> 
> ���ڶ�ȡ /proc/{pid}/smaps_rollup �ȽϺ�ʱ�����鲻�����߳���ʹ�øýӿڡ�����ͨ��@ohos.taskpool��@ohos.worker�����첽�̣߳��Ա���Ӧ�ÿ��١�

**起始版本：** 20

<!--Device-hidebug-function getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo--><!--Device-hidebug-function getAppNativeMemInfoWithCache(forceRefresh?: boolean): NativeMemInfo-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| forceRefresh | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| [NativeMemInfo](arkts-performanceanalysis-hidebug-nativememinfo-i.md) |

## 示例

```TypeScript
let nativeMemInfo: hidebug.NativeMemInfo = hidebug.getAppNativeMemInfoWithCache();
console.info(`pss: ${nativeMemInfo.pss}, vss: ${nativeMemInfo.vss}, rss: ${nativeMemInfo.rss}, ` +
  `sharedDirty: ${nativeMemInfo.sharedDirty}, privateDirty: ${nativeMemInfo.privateDirty}, ` +
  `sharedClean: ${nativeMemInfo.sharedClean}, privateClean: ${nativeMemInfo.privateClean}`);
```
