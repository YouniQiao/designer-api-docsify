# unregisterTraceListener

## 导入模块

```TypeScript
```

## unregisterTraceListener

```TypeScript
function unregisterTraceListener(index: number): number
```

注销通过registerTraceListener()注册的trace捕获开关通知回调函数。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-hiTraceMeter-function unregisterTraceListener(index: int): int--><!--Device-hiTraceMeter-function unregisterTraceListener(index: int): int-End-->

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
// 注销应用trace捕获开关通知回调，index为hiTraceMeter.registerTraceListener返回的回调索引
let ret = hiTraceMeter.unregisterTraceListener(index);
if (ret < 0) {
  // 异常处理......
}
```
