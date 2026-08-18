# addWatcher（系统接口）

## 导入模块

```TypeScript
```

## addWatcher

```TypeScript
function addWatcher(watcher: Watcher): void
```

订阅系统事件，接收[Watcher](arkts-performanceanalysis-hisysevent-watcher-i-sys.md#watcher系统接口)类型的对象作为事件参数。

**起始版本：** 23

**需要权限：** ohos.permission.READ_DFX_SYSEVENT

<!--Device-hiSysEvent-function addWatcher(watcher: Watcher): void--><!--Device-hiSysEvent-function addWatcher(watcher: Watcher): void-End-->

**系统能力：** SystemCapability.HiviewDFX.HiSysEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| watcher | [Watcher](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-watcher-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [11200102](../errorcode-hisysevent-sys.md#11200102-系统事件监听者包含的监听规则数量超过限制) |
| [11200101](../errorcode-hisysevent-sys.md#11200101-系统事件监听者的数量超过限制) |

**示例**

```TypeScript
import { hiSysEvent } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let watchRules: hiSysEvent.WatchRule[] = [{
    domain: "RELIABILITY",
    name: "STACK",
    tag: "STABILITY",
    ruleType: hiSysEvent.RuleType.WHOLE_WORD,
  } as hiSysEvent.WatchRule];
let watcher: hiSysEvent.Watcher = {
  rules: watchRules,
  onEvent: (info: hiSysEvent.SysEventInfo) => {
    // 处理订阅到的系统事件
  },
  onServiceDied: () => {
    // 处理系统事件服务异常
  }
};
try {
  hiSysEvent.addWatcher(watcher);
} catch (err) {
  // 捕获并打印错误信息
  console.error(`error code: ${(err as BusinessError).code}, error msg: ${(err as BusinessError).message}`);
}
```
