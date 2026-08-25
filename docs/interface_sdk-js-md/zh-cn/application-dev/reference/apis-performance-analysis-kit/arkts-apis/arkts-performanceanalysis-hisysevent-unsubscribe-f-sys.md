# unsubscribe（系统接口）

## 导入模块

```TypeScript
import { hiSysEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## unsubscribe

```TypeScript
function unsubscribe(): void
```

取消订阅系统事件。

**起始版本：** 10

**需要权限：** ohos.permission.READ_DFX_SYSEVENT

**系统能力：** SystemCapability.HiviewDFX.HiSysEvent

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11200305](../errorcode-hisysevent-sys.md#11200305-取消订阅失败) |
