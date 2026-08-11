# getRssInfo

## getRssInfo

```TypeScript
function getRssInfo(): RssInfo
```

��ȡӦ�ó�����̵������ڴ�ʹ����Ϣ����ȡ/proc/{pid}/status�ڵ�����ݡ�

> **ע��**
> 
> ��ȡ/proc/{pid}/status��ʱ�̣ܶ���hidebug.getAppNativeMemInfo�ӿ��л�ȡ��`rss`ֵ��ȴ���һ�������ýӿڸ���������Ϊ����Ӧ�ö�֡�򿨶��Ƽ�ʹ�øýӿڡ�

**起始版本：** 24

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-hidebug-function getRssInfo(): RssInfo--><!--Device-hidebug-function getRssInfo(): RssInfo-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值：**

| 类型 |
| --- |
| [RssInfo](arkts-performanceanalysis-hidebug-rssinfo-i.md) |

## 示例

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';

let rssInfo: hidebug.RssInfo = hidebug.getRssInfo();
console.info(`rss: ${rssInfo.rss}, swapRss: ${rssInfo.swapRss}`);
```
