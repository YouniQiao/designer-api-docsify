# setEventParam

## setEventParam

```TypeScript
function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>
```

事件自定义参数设置方法，使用Promise方式作为异步回调。在同一生命周期中，可以通过事件领域和事件名称关联系统事件和应用事件。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-hiAppEvent-function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>--><!--Device-hiAppEvent-function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>-End-->

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | Record&lt;string, [ParamType](arkts-performanceanalysis-hiappevent-paramtype-t.md)&gt; | 是 |
| domain | string | 是 |
| name | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [11101001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101001-非法的事件领域名称) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [11101002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101002-非法的事件名称) |
| [11101005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101005-非法的事件参数名称) |
| [11101004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101004-非法的事件参数字符串长度) |
| [11101007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11101007-非法的事件自定义参数数量) |
| [11100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-performance-analysis-kit/errorcode-hiappevent.md#11100001-打点功能被关闭) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let params: Record<string, hiAppEvent.ParamType> = {
  "int_data": 100,
  "str_data": "strValue",
};

// 给应用事件追加自定义参数
hiAppEvent.setEventParam(params, "test_domain", "test_event").then(() => {
  hilog.info(0x0000, 'hiAppEvent', `success to set event param`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `code: ${err.code}, message: ${err.message}`);
});
```
