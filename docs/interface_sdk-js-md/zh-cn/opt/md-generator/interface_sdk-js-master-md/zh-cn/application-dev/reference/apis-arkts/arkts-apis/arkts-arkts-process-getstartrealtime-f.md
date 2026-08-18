# getStartRealtime

## 导入模块

```TypeScript
```

## getStartRealtime

```TypeScript
function getStartRealtime(): number
```

获取系统启动到进程启动的实时时间（以毫秒为单位，不包含系统休眠时间）。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-process-function getStartRealtime(): number--><!--Device-process-function getStartRealtime(): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
let realtime = process.getStartRealtime();
```
