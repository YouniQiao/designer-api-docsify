# exportSysEvents（系统接口）

## exportSysEvents

```TypeScript
function exportSysEvents(queryArg: QueryArg, rules: QueryRule[]): number
```

批量导出系统事件，以文件格式写入应用沙箱固定目录(/data/storage/el2/base/cache/hiview/event/)。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.READ_DFX_SYSEVENT

<!--Device-hiSysEvent-function exportSysEvents(queryArg: QueryArg, rules: QueryRule[]): long--><!--Device-hiSysEvent-function exportSysEvents(queryArg: QueryArg, rules: QueryRule[]): long-End-->

**系统能力：** SystemCapability.HiviewDFX.HiSysEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| queryArg | [QueryArg](arkts-performanceanalysis-hisysevent-queryarg-i-sys.md) | 是 |
| [rules](arkts-performanceanalysis-hisysevent-watcher-i-sys.md) | [QueryRule](arkts-performanceanalysis-hisysevent-queryrule-i-sys.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11200302](../errorcode-hisysevent-sys.md#11200302-非法的查询规则) |
| [11200301](../errorcode-hisysevent-sys.md#11200301-查询规则的数量超过限制) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11200304](../errorcode-hisysevent-sys.md#11200304-查询频率超过限制) |

## 示例

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
import { hiSysEvent } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let customizedParams: Record<string, string | number> = {
    'PID': 487,
    'UID': 103,
    'PACKAGE_NAME': "com.ohos.hisysevent.test",
    'PROCESS_NAME': "syseventservice",
    'MSG': "no msg."
  };
  let eventInfo: hiSysEvent.SysEventInfo = {
    domain: "RELIABILITY",
    name: "STACK",
    eventType: hiSysEvent.EventType.FAULT,
    params: customizedParams
  };
  hiSysEvent.write(eventInfo, (err: BusinessError) => {
    // 处理事件写入成功后的操作
  });

  let queryArg: hiSysEvent.QueryArg = {
    beginTime: -1,
    endTime: -1,
    maxEvents: 1,
  };
  let queryRules: hiSysEvent.QueryRule[] = [{
    domain: "RELIABILITY",
    names: ["STACK"],
  } as hiSysEvent.QueryRule];
  let time = hiSysEvent.exportSysEvents(queryArg, queryRules);
  console.info(`receive export task time is : ${time}`);

  // 等待文件写入完成后读取（建议通过监听文件系统事件或轮询文件大小确认）
  setTimeout(() => {
    let eventDir = '/data/storage/el2/base/cache/hiview/event';
    let filenames = fileIo.listFileSync(eventDir);
    for (let i = 0; i < filenames.length; i++) {
      if (filenames[i].indexOf(time.toString()) != -1) {
        let res = fileIo.readTextSync(eventDir + '/' + filenames[i]);
        let events: string = JSON.parse('[' + res.slice(0, res.length - 1) + ']');
        console.info("read file end, events is :" + JSON.stringify(events));
      }
    }
  }, 10000);
} catch (err) {
  // 捕获并打印错误信息
  console.error(`error code: ${(err as BusinessError).code}, error msg: ${(err as BusinessError).message}`);
}
```
