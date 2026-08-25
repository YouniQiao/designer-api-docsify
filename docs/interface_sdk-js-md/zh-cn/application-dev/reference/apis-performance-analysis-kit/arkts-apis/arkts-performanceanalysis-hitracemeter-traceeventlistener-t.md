# TraceEventListener

```TypeScript
type TraceEventListener = (traceStatus: boolean) => void
```

定义应用trace捕获开关状态切换时的回调函数类型。

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| traceStatus | boolean | 是 |
