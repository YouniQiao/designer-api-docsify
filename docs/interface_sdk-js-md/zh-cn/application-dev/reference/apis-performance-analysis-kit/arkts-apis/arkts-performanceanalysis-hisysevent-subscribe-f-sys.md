# subscribe（系统接口）

## 导入模块

```TypeScript
import { hiSysEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## subscribe

```TypeScript
function subscribe(rules: QueryRule[]): number
```

订阅实时系统事件(事件需满足低频率或偶发性的约束条件)，事件发生时立即以文件格式写入应用沙箱固定目录(/data/storage/el2/base/cache/hiview/event/)。

**起始版本：** 10

**需要权限：** ohos.permission.READ_DFX_SYSEVENT

**系统能力：** SystemCapability.HiviewDFX.HiSysEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rules | [QueryRule](arkts-performanceanalysis-hisysevent-queryrule-i-sys.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11200301](../errorcode-hisysevent-sys.md#11200301-查询规则的数量超过限制) |
| [11200302](../errorcode-hisysevent-sys.md#11200302-非法的查询规则) |
